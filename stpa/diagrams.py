from abc import ABC
from collections import Counter
from dataclasses import dataclass, field
from operator import attrgetter
from typing import ClassVar


@dataclass
class ControlStructure():
    # id: str
    name: str

    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other) -> bool:
        if isinstance(other, ControlStructure):
            return self.name == other.name
        return False

@dataclass
class ActionFeedback(ABC):
    controlled: ControlStructure
    controller: ControlStructure

@dataclass
class ControlAction(ActionFeedback):
    action: str

    def __hash__(self):
        return hash((self.action, self.controlled.name, self.controller.name))

    def __eq__(self, other) -> bool:
        if isinstance(other, ControlAction):
            return self.action == other.action and self.controlled == other.controlled and self.controller == other.controller
        return False

@dataclass
class ControlFeedback(ActionFeedback):
    feedback: str

    def __hash__(self):
        return hash((self.feedback, self.controlled.name, self.controller.name))
    
    def __eq__(self, other) -> bool:
        if isinstance(other, ControlFeedback):
            return self.feedback == other.feedback and self.controlled == other.controlled and self.controller == other.controller
        return False