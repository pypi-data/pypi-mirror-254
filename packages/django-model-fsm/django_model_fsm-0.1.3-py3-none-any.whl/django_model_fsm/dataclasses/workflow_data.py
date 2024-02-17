from dataclasses import dataclass

from transitions import State

from .state_data import StateData
from .trigger_data import TriggerData


@dataclass
class WorkflowData:
    initial_state: str
    transitions_data: list[dict]

    @property
    def labels(self) -> dict:
        return {x.id: x.label for x in self.states_data}

    @property
    def states(self) -> list[State]:
        return [State(name=x.id) for x in self.states_data]

    @property
    def states_data(self) -> list[StateData]:
        states = []
        for x in self.transitions_data:
            if x["source"] not in states:
                states.append(x["source"])
            if x["dest"] not in states:
                states.append(x["dest"])
        return states

    @property
    def triggers(self) -> dict:
        return {x.id: x for x in self.triggers_data}

    @property
    def triggers_data(self) -> list[TriggerData]:
        triggers = []
        for x in self.transitions_data:
            if x["trigger"] not in triggers:
                triggers.append(x["trigger"])

        return triggers

    def get_labels_for_triggers(self) -> dict:
        return {key: value.label for key, value in self.triggers.items()}

    def get_state_as_label(self, state: str) -> str:
        return self.labels[state]

    def get_triggers_and_labels_from_state(self, state: str) -> list[dict]:
        ordered_triggers = self.get_triggers_from_state(state=state)
        return {
            x: {
                "label": self.triggers[x].label,
                "need_confirmation": self.triggers[x].need_confirmation,
            }
            for x in ordered_triggers
        }

    def get_triggers_from_state(self, state: str) -> list[str]:
        triggers = [x["trigger"] for x in self.transitions if x["source"] == state]
        # ordered triggers
        return [
            x[0]
            for x in sorted(
                [(x, self.triggers[x].order) for x in triggers],
                key=lambda x: x[1],
            )
        ]

    @property
    def transitions(self) -> list[dict]:
        return [
            {key: x[key].id if key in ["trigger", "source", "dest"] else x[key] for key in x}
            for x in self.transitions_data
        ]
