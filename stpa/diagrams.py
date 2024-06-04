from abc import ABC, abstractmethod
from collections import Counter
from dataclasses import dataclass, field
from operator import attrgetter
from typing import ClassVar


@dataclass
class ControlStructure():
    id: str
    value: str


@dataclass
class ControlActionFeedback():
    controller: ControlStructure
    controlled: ControlStructure

    action: str
    feedback: str