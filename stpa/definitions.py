from __future__ import annotations

from abc import ABC, abstractmethod
from collections import Counter
from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Definition(ABC):
    __lookup: ClassVar[dict[str, Definition]] = {}
    __counter: ClassVar[Counter[str]] = Counter()
    _label: ClassVar[str]
    _index: int = field(init=False)

    @classmethod
    def get(self, name: str) -> Definition:
        return self.__lookup[name]

    @classmethod
    def get_all(self, *names: str) -> list[Definition]:
        return list(map(self.get, names))

    def __post_init__(self) -> None:
        count = self.__counter[self._label]
        self._index = count
        self.__counter[self._label] += 1
        self.__lookup[self.name] = self

    def __repr__(self) -> str:
        return self.name

    @abstractmethod
    def __str__(self) -> str:
        pass

    @property
    def name(self) -> str:
        return f'{self._label}{self._index + 1}'


@dataclass(repr=False)
class Loss(Definition):
    _label: ClassVar[str] = 'L-'
    description: str

    def __str__(self) -> str:
        return f'{self.name}: {self.description}'


@dataclass(repr=False)
class Hazard(Definition):
    _label: ClassVar[str] = 'H-'
    system: str
    unsafe_condition: str
    losses: list[Loss]

    def __str__(self) -> str:
        return (
            f'{self.name}:'
            f' {self.system}'
            f' {self.unsafe_condition}'
            f' {self.losses}'
        )


@dataclass(repr=False)
class SystemLevelConstraint(Definition, ABC):
    _label: ClassVar[str] = 'SC-'


@dataclass(repr=False)
class SystemLevelConstraintType1(SystemLevelConstraint):
    system: str
    enforcement_condition: str
    hazards: list[Hazard]

    def __str__(self) -> str:
        return (
            f'{self.name}:'
            f' {self.system}'
            f' {self.enforcement_condition}'
            f' {self.hazards}'
        )


@dataclass(repr=False)
class SystemLevelConstraintType2(SystemLevelConstraint):
    hazard: Hazard
    loss_mitigation: str
    hazards: list[Hazard]

    def __str__(self) -> str:
        return (
            f'{self.name}:'
            ' If'
            f' {self.hazard.system}'
            f' {self.hazard.unsafe_condition},'
            ' then'
            f' {self.loss_mitigation}'
            f' {self.hazards}'
        )


@dataclass(repr=False)
class SubHazard(SystemLevelConstraint):
    hazard: Hazard
    description: str

    def __str__(self) -> str:
        return f'{self.name}: {self.description}'

    @property
    def _label(self) -> str:  # type: ignore[override]
        return f'{self.hazard.name}.'


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
