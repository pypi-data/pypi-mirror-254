from typing import Union, Optional
from aws_cdk import Environment as CdkEnv
from enum import Enum
import boto3

from aws_cdk.aws_ec2 import Vpc, CfnInternetGateway, NatProvider, NatInstanceProvider, Subnet, IVpc, ISubnet, \
    SubnetType, InterfaceVpcEndpoint, InterfaceVpcEndpointAwsService, VpcEndpointType, VpcEndpoint, GatewayVpcEndpoint
from constructs import IConstruct, Construct

from infraflow.priv_utils import only_truthy_items

DEFAULT_INTERFACE_SERVICES = [
    InterfaceVpcEndpointAwsService.SQS,
    InterfaceVpcEndpointAwsService.SNS,
    InterfaceVpcEndpointAwsService.S3,
    InterfaceVpcEndpointAwsService.SES,
    InterfaceVpcEndpointAwsService.RDS_DATA
]

class IEnv:
    @property
    def vpc(self) -> IVpc:
        raise NotImplemented()

    def vpc_subnets(self, subnet_type=None) -> list[ISubnet]:
        raise NotImplemented()

    def service_subnets(self, subnet_type: SubnetType):
        raise NotImplemented()

    def get_secret(self, key) -> str:
        raise NotImplemented()

    def get_param(self, key) -> str:
        raise NotImplemented()

    @property
    def environment_vars(self) -> dict:
        raise NotImplemented()

    def service_endpoints(self, services: list[InterfaceVpcEndpointAwsService]) -> list[InterfaceVpcEndpoint]:
        raise NotImplemented()


class EnvConfig:
    def __init__(
            self,
            env: CdkEnv,
            vpc_id: str,
            subnet_map: dict[SubnetType, list[str]] = None,
            environment_variables: dict[str, str] = {}
    ):
        self.env = env
        self.environment_variables = environment_variables
        self.vpc_id = vpc_id
        self.subnet_map = subnet_map


class Env(IEnv):
    def __init__(self, stage_name: str, scope: Construct, config: EnvConfig):
        self.stage_name = stage_name
        self.config = config
        self.scope = scope
        self.secrets_manager = boto3.client('secretsmanager')
        self.ssm = boto3.client('ssm')
        self._vpc = Vpc.from_lookup(self.scope, "VPC", vpc_id=self.config.vpc_id)

    @property
    def vpc(self) -> IVpc:
        return self._vpc

    def vpc_subnets(self, subnet_type: SubnetType=None) -> list[ISubnet]:
        return self.vpc.select_subnets(subnet_type=subnet_type).subnets

    def service_subnets(self, subnet_type: SubnetType):
        vpc_subnets = self.vpc_subnets(subnet_type)
        if not self.config.subnet_map:
            return vpc_subnets

        subnet_ids = self.config.subnet_map[subnet_type]
        return [sn for sn in vpc_subnets for sni in subnet_ids if sni == sn.subnet_id]

    def secret(self, key):
        return self.secrets_manager.get_secret_value(key)

    def param(self, key):
        return self.ssm.get_parameter(key)

    def service_endpoints(self, services: list[InterfaceVpcEndpointAwsService]) -> list[InterfaceVpcEndpoint]:
        return self.interface_endpoints(service_names=[s.name for s in services])

    def _get_endpoints(
            self,
            endpoint_type: VpcEndpointType, *,
            service_names: Optional[list[str]] = None,
    ) -> list[dict]:
        client = boto3.client('ec2')
        results = client.describe_vpc_endpoints(Filters=only_truthy_items([
            {
                "Name": "vpc-id",
                "Values": [self.vpc.vpc_id],
            },
            {
                "Name": "vpc-endpoint-type",
                "Values": [str(endpoint_type).lower().capitalize()],
            },
            {
                "Name": "service-name",
                "Values": service_names
            } if service_names else None
        ]))
        return results

    def interface_endpoints(self, service_names: Optional[list[str]] = None) -> list[InterfaceVpcEndpoint]:
        return [
            InterfaceVpcEndpoint.from_interface_vpc_endpoint_attributes(
                self.scope, '', vpc_endpoint_id=ep.get('VpcEndpointId')
            )
            for ep in self._get_endpoints(endpoint_type=VpcEndpointType.INTERFACE, service_names=service_names)
            if ep.get("VpcEndpointType") == "Interface"
        ]

    def gateway_endpoints(self) -> list[GatewayVpcEndpoint]:
        return [
            GatewayVpcEndpoint.from_gateway_vpc_endpoint_id(
                self.scope, '', vpc_endpoint_id=ep.get('VpcEndpointId')
            )
            for ep in self._get_endpoints(endpoint_type=VpcEndpointType.GATEWAY)
            if ep.get("VpcEndpointType") == "Gateway"
        ]


    @property
    def environment_vars(self):
        return self.config.environment_variables
