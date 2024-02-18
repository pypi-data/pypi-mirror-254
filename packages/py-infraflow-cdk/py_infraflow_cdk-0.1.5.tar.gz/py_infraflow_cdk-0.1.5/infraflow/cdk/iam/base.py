from aws_cdk import IResource
import aws_cdk.aws_iam as iam
from aws_cdk.aws_iam import Policy, PolicyProps
from constructs import Construct

from infraflow.cdk.arns import arn_for_resource, service_key_for_resource


class IamResource:
    def __init__(self, resource: IResource = None, service=None, pattern: str = None, all: bool = False):
        if (int(bool(resource)) + int(bool(pattern)) + int(all)) > 1:
            raise ValueError('Must only provide one parameter for: resource, pattern, or all')
        self.all = all
        self.resource = resource

        if pattern:
            if service:
                self.resource_string = f"{service}:pattern"
            else:
                self.resource_string = pattern
        elif all:
            self.resource_string = f'{service}:*'
        elif resource:
            self.resource_string = arn_for_resource(resource)

        if resource:
            self.service = service_key_for_resource(resource)
        else:
            self.service = service


class IamAction:
    def __init__(self, service: str, all: bool = False, pattern: str = None):
        """
        :param service: What AWS service this action is for
        :param all: whether to allow all actions for this service, can't be true/set if pattern is set
        :param pattern: the pattern to use for this service, can't be set if all is true
        """
        if all and pattern:
            raise ValueError('Must only provide one parameter for: pattern, or all')
        self.all = all
        if pattern:
            self.pattern = pattern
        elif all:
            self.pattern = '*'
        self.service = service
        self.action_string = f"{self.service}:{self.pattern}"


class IamStatement:
    def __init__(self,
                 effect: iam.Effect = iam.Effect.ALLOW,
                 resources: list[IamResource] = [],
                 actions: list[IamAction] = []):
        self.effect = effect
        self.actions = actions
        self.resources = resources

    def allow(self):
        self.effect = iam.Effect.ALLOW
        return self

    def deny(self):
        self.effect = iam.Effect.DENY
        return self

    def action(self, action: IamAction):
        self.actions.append(action)

    def for_actions(self, *actions: IamAction):
        self.actions.extend(actions)

    def to_cdk(self):
        return iam.PolicyStatement(
            actions=[a.action_string for a in self.actions],
            resources=[r.resource_string for r in self.resources],
            effect=self.effect
        )


class PolicyBuilder:
    def __init__(self):
        self.statements: list[IamStatement] = []

    def allow_resource(self, resource: IResource):
        statement = IamStatement(
            effect=iam.Effect.ALLOW,
            resources=[IamResource(resource)]
        )
        self.statements.append(statement)
        return statement

    def allow_resources(self, resources: list[IResource]):
        statement = IamStatement(
            effect=iam.Effect.ALLOW,
            resources=[IamResource(resource) for resource in resources]
        )
        self.statements.append(statement)
        return statement

    def allow_on_all(self, service: str):
        statement = IamStatement(
            effect=iam.Effect.ALLOW,
            resources=[IamResource(service=service, all=True)]
        )
        self.statements.append(statement)
        return statement

    def allow_pattern(self, service: str, pattern: str):
        statement = IamStatement(
            effect=iam.Effect.ALLOW,
            resources=[IamResource(service=service, pattern=pattern)]
        )
        self.statements.append(statement)
        return statement

    def deny_resource(self, resource: IResource):
        statement = IamStatement(
            effect=iam.Effect.DENY,
            resources=[IamResource(resource)]
        )
        self.statements.append(statement)
        return statement

    def deny_resources(self, resources: list[IResource]):
        statement = IamStatement(
            effect=iam.Effect.DENY,
            resources=[IamResource(resource) for resource in resources]
        )
        self.statements.append(statement)
        return statement

    def deny_on_all(self, service: str):
        statement = IamStatement(
            effect=iam.Effect.DENY,
            resources=[IamResource(service=service, all=True)]
        )
        self.statements.append(statement)
        return statement

    def deny_pattern(self, service: str, pattern: str):
        statement = IamStatement(
            effect=iam.Effect.DENY,
            resources=[IamResource(service=service, pattern=pattern)]
        )
        self.statements.append(statement)
        return statement

    def build_cdk_policy(self, parent: Construct, id: str) -> Policy:
        return Policy(parent, id, PolicyProps(statements=[s.to_cdk() for s in self.statements]))
