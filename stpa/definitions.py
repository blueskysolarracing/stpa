from abc import ABC, abstractmethod
from collections import Counter
from dataclasses import dataclass, field
from operator import attrgetter
from typing import ClassVar


@dataclass
class Definition(ABC):
    __counter: ClassVar[Counter[str]] = Counter()
    _label: ClassVar[str]
    _index: int = field(init=False)

    def __post_init__(self) -> None:
        count = self.__counter[self._label]
        self._index = count
        self.__counter[self._label] += 1
    
    def __repr__(self) -> str:
        return f'{self._label}{self._index + 1}'

    @abstractmethod
    def __str__(self) -> str:
        pass


@dataclass(repr=False)
class Loss(Definition):
    _label: ClassVar[str] = 'L-'
    description: str

    def __str__(self) -> str:
        return f'{repr(self)}: {self.description}'


@dataclass(repr=False)
class Hazard(Definition):
    _label: ClassVar[str] = 'H-'
    system: str
    unsafe_condition: str
    losses: list[Loss]

    def __str__(self) -> str:
        return (
            f'{repr(self)}:'
            f' {self.system}'
            f' {self.unsafe_condition}'
            f' {self.losses}'
        )


@dataclass(repr=False)
class SystemLevelConstraint(Definition, ABC):
    _label: ClassVar[str] = 'SC-'

    # def __init__(self, if_then: bool, *args) -> None:
    #     if if_then:
    #         self.system, self.enforcement_condition, self.hazards = args
    #     else:
    #         self.hazards, self.loss_mitigation = args


@dataclass(repr=False)
class SystemLevelConstraintType1(SystemLevelConstraint):
    system: str
    enforcement_condition: str
    hazards: list[Hazard]

    def __str__(self) -> str:
        return (
            f'{repr(self)}:'
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
            'If'
            f' \'{self.hazard.system}\''
            f' \'{self.hazard.unsafe_condition}\','
            ' then'
            f' \'{self.loss_mitigation}\''
            f' {self.hazards}'
        )


@dataclass(repr=False)
class SubHazard(SystemLevelConstraint):
    hazard: Hazard
    description: str

    def __str__(self) -> str:
        return f'{repr(self)}: {self.description}'

    @property
    def _label(self) -> str:  # type: ignore[override]  # TODO
        return f'{repr(self.hazard)}.'
