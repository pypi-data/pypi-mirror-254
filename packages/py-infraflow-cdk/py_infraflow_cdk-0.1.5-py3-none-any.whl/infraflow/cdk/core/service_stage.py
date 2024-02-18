from aws_cdk import Stack, App
from aws_cdk.aws_ec2 import SecurityGroup

from infraflow.cdk.core.construct import HasEnv, HasDefaultSg
from infraflow.cdk.core.environment import EnvConfig, Env
from infraflow.cdk.sg.patterns import SecurityGroupStructurePattern, SecurityGroupTarget


class ServiceStageStack(Stack, HasEnv, HasDefaultSg):
    def __init__(
            self,
            app: App,
            service_name: str,
            stage_name: str,
            env: EnvConfig,
            **kwargs
    ):
        super().__init__(app, f"{stage_name}-{service_name}", env=env.env, **kwargs)
        self.service_name = service_name
        self.stage_name = stage_name
        self.scope = app
        self.env = Env(stage_name, self, env)
        self.default_sg: SecurityGroup = None
        self.security_groups: SecurityGroupStructurePattern = None

    def get_sg(self, id=None, cdk_type: type = None):
        return self.security_groups.get_group(SecurityGroupTarget(self.scope, id=id, cdk_type=cdk_type))
