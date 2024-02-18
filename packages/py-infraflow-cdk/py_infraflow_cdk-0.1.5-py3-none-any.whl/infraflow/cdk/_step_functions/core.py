from aws_cdk import aws_stepfunctions_tasks as tasks
from aws_cdk import aws_stepfunctions as sfn
from aws_cdk import aws_events as events
from aws_cdk.aws_stepfunctions import TaskInput

from infraflow.cdk.core.service_stage import ServiceStageStack


class StepFunctionWorkflow:
    def __init__(self, environment: ServiceStageStack, name: str):
        self.name = name
        self.environment = environment

        tasks.LambdaInvoke(self.environment, )
        start = sfn.Pass(self.environment, 'startSelectionProcessing', input_path='$', output_path='$')
        event = sfn.Activity(self.environment, 'test')
        selection_processing = sfn.StateMachine(self.environment, 'selection-workflow', definition=start)
        start.next()

    def start(self):
        start = sfn
        start = sfn.Pass(self.environment, f"start_${self.name}", input_path='$', output_path='$')

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
