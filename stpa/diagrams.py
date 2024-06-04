from abc import ABC, abstractmethod
from collections import Counter
from dataclasses import dataclass, field
from operator import attrgetter
from typing import ClassVar


@dataclass
class ControlStructure(ABC):
    pass


@dataclass
class ControlAction(Definition):
    pass

@dataclass
class ControlFeedback(Definition):
    pass