from aws_cdk.aws_ec2 import SecurityGroup, Port
from constructs import Construct, IConstruct
from infraflow.cdk.sg import tier_maps
from infraflow.cdk.sg.ports import all_tcp


class SecurityGroupNeeds:
    def __init__(
            self,
            needs_outbound_internet=None,
            needs_inbound_internet=None
    ):
        self.needs_inbound_internet = needs_inbound_internet
        self.needs_outbound_internet = needs_outbound_internet


class SecurityGroupTarget:
    def __init__(
            self,
            scope: Construct, id: str, *args,
            cdk_type: type = None,
            infraflow_pattern: object = None,
    ):
        self.infraflow_pattern = infraflow_pattern
        self.cdk_type = cdk_type
        self.id = id
        self.scope = scope


class SecurityGroupStructurePattern:
    def __init__(self, stack):
        self.stack = stack

    def get_group(
            self,
            target: SecurityGroupTarget,
            tier: str = None,
            needs: SecurityGroupNeeds = SecurityGroupNeeds()

    ) -> SecurityGroup:
        raise NotImplemented()


class SingleSecurityGroup(SecurityGroupStructurePattern):
    def __init__(self, stack):
        super().__init__(stack)

    def get_group(
            self,
            target: SecurityGroupTarget,
            tier: str = None,
            needs: SecurityGroupNeeds = SecurityGroupNeeds()

    ) -> SecurityGroup:
        return self.stack.default_sg


class SecurityGroupPerResource(SecurityGroupStructurePattern):
    def __init__(self, stack):
        super().__init__(stack)

    def get_group(
            self,
            target: SecurityGroupTarget,
            tier: str = None,
            needs: SecurityGroupNeeds = SecurityGroupNeeds()

    ) -> SecurityGroup:
        return SecurityGroup(scope=target.scope, id=target.id+"Sg")


class Tiered(SecurityGroupStructurePattern):
    def __init__(self, stack, db_ports: list[Port], app_web_ports: list[Port] = [all_tcp], allow_all_within_app_group=True, allow_all_within_group: bool = False):
        super().__init__(stack)
        self.dbs = SecurityGroup(self.stack, 'DbSg', vpc=self.stack.env.vpc)
        self.app = SecurityGroup(self.stack, 'AppSg', vpc=self.stack.env.vpc)
        self.web = SecurityGroup(self.stack, 'WebSg', vpc=self.stack.env.vpc)
        for port in app_web_ports:
            self.web.connections.allow_to(self.app, port)
        for port in db_ports:
            self.app.connections.allow_to(self.dbs, port)

        if allow_all_within_group or allow_all_within_app_group:
            self.app.connections.allow_to(self.app, Port.all_tcp())

        if allow_all_within_group:
            self.dbs.connections.allow_to(self.dbs, Port.all_tcp())
            self.web.connections.allow_to(self.web, Port.all_tcp())

    def get_group(
            self,
            target: SecurityGroupTarget,
            tier: str = None,
            needs: SecurityGroupNeeds = SecurityGroupNeeds()

    ) -> SecurityGroup:
        if tier == 'app':
            return self.app
        elif tier == 'db':
            return self.dbs
        elif tier == 'web':
            return self.web
        elif target.cdk_type in tier_maps.app_services:
            return self.app
        elif target.cdk_type in tier_maps.web_services:
            return self.web
        elif target.cdk_type in tier_maps.db_services:
            return self.dbs
        else:
            return self.stack.default_sg

