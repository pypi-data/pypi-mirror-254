import datetime
from typing import Union

from aws_cdk import aws_lambda, Duration
from aws_cdk import aws_sqs
from aws_cdk import aws_lambda_event_sources as sources
from aws_cdk.aws_ec2 import SubnetType, SubnetSelection
from aws_cdk.aws_events import Rule, Schedule
from aws_cdk.aws_events_targets import LambdaFunction
from aws_cdk.aws_iam import IRole
from aws_cdk.aws_lambda import IEventSource
from constructs import Construct, IConstruct

from infraflow.cdk.core.service_stage import ServiceStageStack
from infraflow.cdk.iam import PolicyBuilder, action_groups
from infraflow.cdk.sg.patterns import SecurityGroupTarget
from infraflow.util import caps_camel

registry = []


class LambdaContext:
    def __init__(self,
                 stage: ServiceStageStack,
                 path: str,
                 role: IRole = None,
                 runtime: aws_lambda.Runtime = aws_lambda.Runtime.PYTHON_3_9,
                 vpc: bool = True,
                 subnet_type: SubnetType = SubnetType.PRIVATE_WITH_EGRESS,
                 tracing=aws_lambda.Tracing.ACTIVE
                 ):
        self.role = role
        self.runtime = runtime
        self.path = path
        self.stage = stage
        self.default_sg = stage.default_sg

    # def to_cdk(self):
    #     return dict(
    #         scope=self.scope,
    #         code=aws_lambda.Code.from_asset(self.path),
    #         runtime=self.runtime
    #     )

    def function(self, handler: str, name=None, suffix=None, scope_override: IConstruct = None):
        constructed_name = self.construct_name(handler, name, suffix)
        func = aws_lambda.Function(
                id=constructed_name,
                handler=handler,
                scope=scope_override or self.stage,
                code=aws_lambda.Code.from_asset(self.path),
                runtime=self.runtime,
                security_groups=[
                    self.stage.security_groups.get_group(target=SecurityGroupTarget(
                        scope_override or self.stage,
                        id=constructed_name,
                        cdk_type=aws_lambda.Function,
                        infraflow_pattern=self,
                    ))
                ],
                vpc_subnets=SubnetSelection(subnets=self.stage.env.vpc_subnets()),
                vpc=self.stage.env.vpc,
                tracing=aws_lambda.Tracing.ACTIVE,
                role=self.role
                # function_name=''
        )
        # if self.role:
        #     func.grant_invoke(self.role)
        return func

    def construct_name(self, handler: str, name: str, suffix: str):
        base_name = name or caps_camel(handler.split(".")[1])
        constructed_name = caps_camel(f"{base_name}_{suffix}" if suffix else base_name)
        return constructed_name

    def queued_function(self, handler, name=None, suffix=None, **queue_config):
        constructed_name = self.construct_name(handler, name, suffix)
        queued_function = QueueFunctionConstruct(self.stage, constructed_name)
        queue = aws_sqs.Queue(queued_function, 'Queue', **queue_config)
        func = self.function(handler, 'Function', scope_override=queued_function)
        func.add_event_source(sources.SqsEventSource(queue))
        queued_function.queue = queue
        queued_function.function = func
        return queued_function

    def scheduled_function(self, handler, schedule: Union[Schedule, Duration, datetime.timedelta], name=None, suffix=None):
        schedule = Duration.seconds(schedule.total_seconds()) if isinstance(schedule, datetime.timedelta) else None
        schedule = Schedule.rate(schedule) if isinstance(schedule, Duration) else None
        constructed_name = self.construct_name(handler, name, suffix)
        func = self.function(handler, name, suffix)
        rule = Rule(self.stage, f"{constructed_name}_schedule", schedule=schedule)
        rule.add_target(LambdaFunction(func))
        return func

    def api_function(self, handler, name=None, suffix=None):
        return self.function(handler, name, suffix)

    def function_with_source(self, handler, event_source: IEventSource, name=None, suffix=None):
        func = self.function(handler, name, suffix)
        func.add_event_source(event_source)
        return func


class QueueFunctionConstruct(Construct):
    function: aws_lambda.Function
    queue: aws_sqs.Queue

    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
