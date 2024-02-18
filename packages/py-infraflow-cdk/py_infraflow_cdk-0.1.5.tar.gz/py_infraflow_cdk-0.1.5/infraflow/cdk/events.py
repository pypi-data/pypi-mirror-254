from typing import Any, Union
from typing import TypeVar, Generic

from infraflow.util import caps_camel

T = TypeVar('T')

from aws_cdk import aws_sqs as sqs
from aws_cdk import aws_sns as sns
from aws_cdk import aws_sns_subscriptions as subscriptions
from aws_cdk import aws_events as events
from aws_cdk import aws_lambda as lambdas
from aws_cdk import aws_events_targets as targets

from infraflow.cdk.lambdas import QueueFunctionConstruct
from infraflow.cdk.core.service_stage import ServiceStageStack


class Rule:
    def __init__(self, property, value=None, values=None, range=None, exists=None, event_bridge=None, sns=None,
                 generic=None):
        self.generic = generic
        self.sns = sns
        self.event_bridge = event_bridge
        self.exists = exists
        self.range = range
        self.value = value
        self.values = values
        self.property = property

    def id(self):
        values = (
            self.value if self.value else
            "Exists" if self.exists else
            "NotExists" if self.exists is False else
            "".join(self.values) if self.values else
            f"{self.range[0]}To{self.range[1]}" if self.range else
            "Other"
        )
        return f"{self.property}{values}"

    def event_bridge_rule(self):
        return self.event_bridge or self.generic or (
            self.values if self.values else [
                self.value if self.value and type(self.value) == str else
                str(self.value) if type(self.value) == bool else
                {"exists": self.exists} if self.exists is not None else
                {"numeric": ["=", self.value]} if self.value and type(self.value) in [int, float] else
                {"numeric": [">=", self.range[0], "<=", self.range[1]]} if self.range else
                None
            ]
        )

    def sns_rule(self):
        return self.sns or self.generic or (
            sns.SubscriptionFilter.string_filter(allowlist=self.values) if self.values else
            sns.SubscriptionFilter.string_filter(allowlist=[self.value]) if self.value and type(self.value) == str else
            sns.SubscriptionFilter.exists_filter(allowlist=[{"exists": self.exists}]) if self.exists is not None else
            sns.SubscriptionFilter.numeric_filter(allowlist=["=", self.value]) if self.value and type(self.value) in [
                int, float] else
            sns.SubscriptionFilter.numeric_filter(
                allowlist=[">=", self.range[0], "<=", self.range[1]]) if self.range else
            None
        )


class Event:
    def __init__(self, stage: ServiceStageStack, bus_id: str, event_key: str):
        self.stage = stage
        self.event_key = event_key
        self.priority = None
        self.filters: list[Rule] = []
        self.bus_id = bus_id

    def express_only(self):
        self.add_filter(Rule("express", True))
        self.priority = "express"
        return self

    def non_express(self):
        self.add_filter(Rule("express", False))
        self.priority = "default"
        return self

    def with_priority(self, priority: int):
        self.add_filter(Rule("priority", priority))
        self.priority = f"priority_{priority}"
        return self

    def with_priorities(self, start: int, stop: int):
        self.add_filter(Rule("priority", [start, stop]))
        self.priority = f"priority_{start}_{stop}"
        return self

    def with_prop(self, key: str):
        self.add_filter(Rule(key, exists=True))
        return self

    def with_true_prop(self, key: str):
        self.add_filter(Rule(key, generic={"equals-ignore-case": "true"}))
        return self

    def with_prop_equal(self, key: str, value: Any):
        self.add_filter(Rule(key, value))
        return self

    def add_filter(self, filter: Rule):
        self.filters.append(filter)

    @property
    def suffix(self):
        return self.priority

    def subscribe(self, *processors: Union[lambdas.Function, QueueFunctionConstruct, sqs.Queue]):
        print("in infraflow/cdk/events/Event.subscribe()")
        subs = []
        for processor in processors:
            print("processor found:", processor)
            if isinstance(processor, QueueFunctionConstruct):
                queue, lam, sub = processor.queue, processor.function, processor.queue
            elif isinstance(processor, sqs.Queue):
                queue, lam, sub = processor, None, processor
            elif isinstance(processor, lambdas.Function):
                queue, lam, sub = None, processor, processor
            else:
                raise TypeError()
            subs.append(sub)
        self._subscribe(*subs)

    @property
    def id(self):
        filters_string = ''.join([f.id() for f in self.filters])
        return f"{caps_camel(self.bus_id)}{caps_camel(self.event_key)}{filters_string}"

    def _subscribe(self, *subscribers: Union[sqs.Queue, lambdas.Function]):
        pass


class SnsEvent(Event):
    def __init__(self, stage: ServiceStageStack, bus_id: str, event_key: str, bus: sns.ITopic):
        super().__init__(stage, bus_id, event_key)
        self.bus = bus

    def _subscribe(self, *subscribers: Union[sqs.Queue, lambdas.Function]):
        for queue in subscribers:
            self.bus.add_subscription(self.get_sns_sqs_subscription(queue))

    def get_sns_sqs_subscription(self, subscriber: Union[sqs.Queue, lambdas.Function]):
        if isinstance(subscriber, sqs.Queue):
            return subscriptions.SqsSubscription(subscriber, filter_policy=self.filter_policy)
        elif isinstance(subscriber, lambdas.Function):
            return subscriptions.LambdaSubscription(subscriber, filter_policy=self.filter_policy)
        else:
            raise TypeError()

    @property
    def filter_policy(self):
        rules = {r.property: r.sns_rule() for r in self.filters}
        return {
            "event": sns.SubscriptionFilter.string_filter(allowlist=[self.event_key]),
            **rules
        }


class EventBridgeEvent(Event):
    def __init__(self, stage: ServiceStageStack, bus_id: str, event_key: str, bus: events.IEventBus):
        super().__init__(stage, bus_id, event_key)
        self.bus = bus

    def _subscribe(self, *subscribers: Union[sqs.Queue, lambdas.Function]):
        targets_ = [get_eb_target(subscriber) for subscriber in subscribers]
        rules = {r.property: r.event_bridge_rule() for r in self.filters}
        return events.Rule(self.stage, self.id, event_bus=self.bus, targets=targets_, event_pattern=events.EventPattern(
            detail={
                "event": [self.event_key],  # [sqs.Queue],  # self.event_key,
                **rules
            }
        ))


def get_eb_target(subscriber: Union[sqs.Queue, lambdas.Function]):
    if isinstance(subscriber, sqs.Queue):
        target = targets.SqsQueue(subscriber)
    elif isinstance(subscriber, lambdas.Function):
        target = targets.LambdaFunction(subscriber)
    else:
        raise TypeError()
    return target


class InfraflowEventBus(Generic[T]):
    def __init__(self, stage: ServiceStageStack, bus_id, bus: T):
        self.bus = bus
        self.bus_id = bus_id
        self.stage = stage

    def event(self, event_key: str) -> Event:
        return Event(stage=self.stage, bus_id=self.bus_id, event_key=event_key)


class EventBridgeEvents(InfraflowEventBus[events.IEventBus]):
    def __init__(self, stage: ServiceStageStack, bus_id, bus: events.IEventBus):
        super().__init__(stage, bus_id, bus)

    def event(self, event_key: str) -> Event:
        return EventBridgeEvent(self.stage, self.bus_id, event_key, self.bus)


class SnsEvents(InfraflowEventBus[sns.ITopic]):
    def __init__(self, stage: ServiceStageStack, bus_id, bus: sns.ITopic):
        super().__init__(stage, bus_id, bus)

    def event(self, event_key: str) -> Event:
        return SnsEvent(self.stage, self.bus_id, event_key, self.bus)

# selection_bus = EventBus()
#
# selection_bus.event('ready').with_true_prop('amplify').express_only().subscribe(
#     context=LambdaContext(...),
#     handler=handle_amplify_selection,
#     suffix='express',
#     queued=True
# )
