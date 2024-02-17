from typing import TypeVar

from aws_cdk.aws_ec2 import SecurityGroup
from constructs import Construct

from infraflow.cdk.core.environment import IEnv


class HasEnv:
    env: IEnv


class HasDefaultSg:
    default_sg: SecurityGroup


ConstructWithEnv = TypeVar('ConstructWithEnv', Construct, HasEnv, HasDefaultSg)
