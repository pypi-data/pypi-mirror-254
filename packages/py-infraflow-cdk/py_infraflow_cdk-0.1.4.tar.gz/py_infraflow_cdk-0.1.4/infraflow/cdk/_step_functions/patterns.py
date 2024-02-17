from aws_cdk import aws_stepfunctions_tasks as tasks
from aws_cdk import aws_stepfunctions as sfn
from aws_cdk import aws_events as events
from aws_cdk.aws_stepfunctions import TaskInput

from infraflow.cdk.environment import ServiceStage


class AwaitBatch:
    def __init__(self, environment: ServiceStage):
        self.environment = environment

        name, data, type, bus = None, None, None, ''
        self.send_event_bridge_event(bus, data, name, type)
        tasks.LambdaInvoke(self.environment.scope, )
        start = sfn.Pass(self.environment.scope, 'startSelectionProcessing', input_path='$', output_path='$')
        event = sfn.Activity(self.environment.scope, 'test')
        selection_processing = sfn.StateMachine(self.environment.scope, 'selection-workflow', definition=start)
        start.next()
    def send_event_bridge_event(
            self,
            bus: events.IEventBus,
            name: str,
            type: str,
            data: list[TaskInput]
    ):
        return tasks.EventBridgePutEvents(self.environment.scope, name, entries=[
            tasks.EventBridgePutEventsEntry(
                detail_type=type,
                detail=x,
                event_bus=bus
            )
            for x in data
        ])
