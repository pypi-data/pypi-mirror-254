from dataclasses import dataclass


@dataclass
class TriggerData:
    id: str  # NOQA: A003
    label: str
    order: int = 0
    need_confirmation: bool = False

    def __str__(self):
        return self.id
