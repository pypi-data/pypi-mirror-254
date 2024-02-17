from dataclasses import dataclass


@dataclass
class StateData:
    id: str  # NOQA: A003
    label: str

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.id
    
