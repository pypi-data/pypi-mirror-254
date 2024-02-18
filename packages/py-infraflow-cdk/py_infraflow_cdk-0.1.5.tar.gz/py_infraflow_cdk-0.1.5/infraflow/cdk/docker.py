from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_ecs_patterns as ecs_patterns
from aws_cdk import aws_ecr_assets as assets
from aws_cdk.aws_ec2 import SubnetSelection
from aws_cdk.aws_ecs import Cluster

from infraflow.cdk import ServiceStageStack
from infraflow.cdk.sg.patterns import SecurityGroupTarget


class EcsCluster:
    def __init__(self, scope: ServiceStageStack, cluster_name: str):
        self.scope = scope
        vpc = self.scope.env.vpc

        self.cluster = ecs.Cluster(self.scope, cluster_name, vpc=vpc)

    def service(self,
                name,
                ecr_image: str = None,
                path: str = None,
                command=None,
                count=1,
                cpu=256,
                memory_limit_mib=512
                ):
        if path:
            image_asset = assets.DockerImageAsset(self.scope, f"{name}_image", directory=path)
            image = ecs.ContainerImage.from_docker_image_asset(image_asset)
        else:
            image = None

        return ecs_patterns.ApplicationLoadBalancedFargateService(
            self.scope, f"{name}_service",
            cluster=self.cluster,  # Required
            cpu=cpu,  # Default is 256
            desired_count=count,  # Default is 1
            listener_port=80,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry(ecr_image) if ecr_image else image if path else None,
                container_name=f"{name}_task",
                container_port=80,
                command=command
            ),
            security_groups=[
                self.scope.security_groups.get_group(target=SecurityGroupTarget(
                    self.cluster,
                    id=name,
                    cdk_type=Cluster,
                    infraflow_pattern=self,
                ))
            ],
            task_subnets=SubnetSelection(subnets=self.scope.env.vpc_subnets()),
            memory_limit_mib=memory_limit_mib,  # Default is 512
            public_load_balancer=True
        )  # Default is True

