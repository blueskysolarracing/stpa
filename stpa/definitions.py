from abc import ABC, abstractmethod
from collections import Counter
from dataclasses import dataclass, field
from operator import attrgetter
from typing import ClassVar


@dataclass(frozen=True)
class Definition(ABC):
    __counter: ClassVar[Counter[str]] = Counter()
    _label: ClassVar[str]
    _index: int = field(init=False)

    def __post_init__(self) -> None:
        count = self.__counter[self._label]
        # self._index = count
        object.__setattr__(self, '_index', count)
        # self.__counter[self._label] += 1
        object.__setattr__(self, '__counter[self._label]', self.__counter[self._label] + 1)
    
    def __repr__(self) -> str:
        return f'{self._label}{self._index + 1}'

    @abstractmethod
    def __str__(self) -> str:
        pass


@dataclass(repr=False, frozen=True)
class Loss(Definition):
    _label: ClassVar[str] = 'L-'
    description: str

    def __str__(self) -> str:
        return f'{repr(self)}: {self.description}'


@dataclass(repr=False, frozen=True)
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


@dataclass(repr=False, frozen=True)
class SystemLevelConstraint(Definition, ABC):
    _label: ClassVar[str] = 'SC-'

    # def __init__(self, if_then: bool, *args) -> None:
    #     if if_then:
    #         self.system, self.enforcement_condition, self.hazards = args
    #     else:
    #         self.hazards, self.loss_mitigation = args


@dataclass(repr=False, frozen=True)
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


@dataclass(repr=False, frozen=True)
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


@dataclass(repr=False, frozen=True)
class SubHazard(SystemLevelConstraint):
    hazard: Hazard
    description: str

    def __str__(self) -> str:
        return f'{repr(self)}: {self.description}'

    @property
    def _label(self) -> str:  # type: ignore[override]  # TODO
        return f'{repr(self.hazard)}.'


@dataclass(repr=False, frozen=True)
class ControlStructure(Definition):
    # id: str
    name: str

    _label: ClassVar[str] = 'CS-'

    def __str__(self) -> str:
        return f'ControlStructure: {self.name}'


@dataclass(repr=False, frozen=True)
class ActionFeedback(ABC):
    controlled: ControlStructure
    controller: ControlStructure


@dataclass(repr=False, frozen=True)
class ControlAction(ActionFeedback, Definition):
    _label: ClassVar[str] = 'Action-'

    action: str

    def __str__(self) -> str:
        return f'{repr(self.controller)} -> {self.action} -> {repr(self.controlled)}'


@dataclass(repr=False, frozen=True)
class ControlFeedback(ActionFeedback, Definition):
    _label: ClassVar[str] = 'Feedback-'

    feedback: str

    def __str__(self) -> str:
        return f'{repr(self.controller)} <- {self.feedback} <- {repr(self.controlled)}'


@dataclass(repr=False, frozen=True)
class UnsafeControlAction(Definition, ABC):
    _label: ClassVar[str] = 'UCA-'

    # todo just use an enum for this
    _type_uca: ClassVar[str]

    source: ControlStructure
    hazard: Hazard
    controlAction: ControlAction 
    context: str

    def __str__(self) -> str:
        return (
            f'{self._label}: {repr(self.source)}'
            f' {self._type_uca} {repr(self.controlAction)}'
            f' {self.context}'
            f' [{self.hazard._label}]'
        )

# todo convert this design to enum
@dataclass(repr=False, frozen=True)
class UnsafeControlAction_notProviding(UnsafeControlAction):
    _type_uca = 'does not provide'


@dataclass(repr=False, frozen=True)
class UnsafeControlAction_providing(UnsafeControlAction):
    _type_uca = 'provides'


@dataclass(repr=False, frozen=True)
class UnsafeControlAction_providingEarly(UnsafeControlAction):
    _type_uca = 'provides too early the'


@dataclass(repr=False, frozen=True)
class UnsafeControlAction_providingLate(UnsafeControlAction):
    _type_uca = 'provides too late the'


@dataclass(repr=False, frozen=True)
class UnsafeControlAction_providingOutOfOrder(UnsafeControlAction):
    _type_uca = 'provides out of order the'


@dataclass(repr=False, frozen=True)
class UnsafeControlAction_stoppedSoon(UnsafeControlAction):
    _type_uca= 'stops providing too soon the'


@dataclass(repr=False, frozen=True)
class UnsafeControlAction_appliedLong(UnsafeControlAction):
    _type_uca = 'applied too long the'