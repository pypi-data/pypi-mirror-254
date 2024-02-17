from collections.abc import Callable
from typing import TYPE_CHECKING

from transitions import Machine

from django.db import models
from django.utils import timezone

from django_model_fsm.dataclasses import StateData, WorkflowData
from django_model_fsm.fields import TransitionField

if TYPE_CHECKING:
    from accounts.models import User


class SupportObj:
    pass


class TransitionsMixin(models.Model):
    workflow_data: WorkflowData = None
    workflow_callbacks: list[str] = []

    transition_state = TransitionField(
        "Transition's state stored in database",
        blank=True,
        null=False,
        max_length=100,
    )

    transition_history = models.JSONField(
        "Historique des transitions",
        blank=False,
        null=False,
        default=dict,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        by: User = kwargs.pop("saved_by", None)

        self.transition_state = self.transition_support.state

        if "history" not in self.transition_history:
            self.transition_history["history"] = []

        if self.pk:
            try:
                label_from = self.get_state_as_label(
                    state=self.transition_state_initial_value,
                )
            except Exception:  # NOQA: BLE001
                label_from = ""

            try:
                label_to = self.get_state_as_label(state=self.transition_state)
            except Exception:  # NOQA: BLE001
                label_to = ""

            if self.transition_state_initial_value != self.transition_state:
                self.transition_history["history"].append(
                    {
                        "by": getattr(by, "email", None) if by is not None else None,
                        "date": int(timezone.now().timestamp() * 1000),
                        "state_from": self.transition_state_initial_value,
                        "state_to": self.transition_state,
                        "label_from": label_from,
                        "label_to": label_to,
                    },
                )

        return super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.transition_state:
            self.transition_state = self.workflow_data.initial_state.id

        self.transition_state_initial_value = self.transition_state

        self.__init_support_object_with_callbacks()

        self.fsm = Machine(
            self.transition_support,
            states=self.workflow_data.states,
            transitions=self.workflow_data.transitions,
            initial=self.transition_state,
        )

    def __init_support_object_with_callbacks(self) -> None:
        self.transition_support = SupportObj()
        self.__workflow_add_callbacks()

    def __workflow_add_callbacks(self) -> None:
        for callback in self.workflow_callbacks:
            setattr(self.transition_support, callback, getattr(self, callback))

    def workflow_get_accessible_triggers(self) -> list[str]:
        return self.workflow_data.get_triggers_from_state(state=self.workflow_state)

    def workflow_get_accessible_triggers_with_labels(self) -> list[dict]:
        return self.workflow_data.get_triggers_and_labels_from_state(
            state=self.workflow_state,
        )

    @classmethod
    @property
    def workflow_all_states_data(cls):
        return cls.workflow_data.states_data

    @property
    def workflow_state(self):
        return self.transition_support.state

    @property
    def workflow_state_as_label(self) -> str:
        return self.workflow_data.get_state_as_label(state=self.workflow_state)

    def is_workflow_state_equal(self, state: StateData) -> bool:
        return self.workflow_state == state.id

    @property
    def workflow_trigger(self) -> Callable:
        return self.transition_support.trigger
