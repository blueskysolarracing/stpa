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
        # print(self._label, 'Count: ', count)
        object.__setattr__(self, '_index', count)
        Definition.__counter[self._label] += 1

    def get_label(self) -> str:
        return repr(self)
    
    def __repr__(self) -> str:
        return f'{self._label}{self._index + 1}'

    @abstractmethod
    def __str__(self) -> str:
        pass
    
    @classmethod
    def reset_counter(cls):
        for label in cls.__counter:
            cls.__counter[label] = 0


@dataclass(repr=False, frozen=True)
class Loss(Definition):
    _label: ClassVar[str] = 'L-'
    description: str
    
    def __str__(self) -> str:
        return f'{self.get_label()}: {self.description}'


@dataclass(repr=False, frozen=True)
class Hazard(Definition):
    _label: ClassVar[str] = 'H-'
    system: str
    unsafe_condition: str
    losses: list[Loss]

    def __str__(self) -> str:
        return (
            f'{self.get_label()}:'
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
            f'{self.get_label()}:'
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
        return f'{self.get_label()}: {self.description}'

    @property
    def _label(self) -> str:  # type: ignore[override]  # TODO
        return f'{repr(self.hazard)}.'


@dataclass(repr=False, frozen=True)
class ControlStructure(Definition):
    # id: str
    name: str

    _label: ClassVar[str] = 'CS-'

    def __str__(self) -> str:
        return f'{self.get_label()}: {self.name}'
    
    def __eq__(self, other):
        if not isinstance(other, ControlStructure):
            return False
        return self.name == other.name


@dataclass(repr=False, frozen=True)
class ActionFeedback(ABC):
    controlled: ControlStructure
    controller: ControlStructure


@dataclass(repr=False, frozen=True)
class ControlAction(ActionFeedback, Definition):
    _label: ClassVar[str] = 'Action-'

    action: str

    def __str__(self) -> str:
        return f'{self.controller} -> {self.action} -> {self.controlled}'
    
    def __eq__(self, other):
        if not isinstance(other, ControlAction):
            return False
        return self.action == other.action


@dataclass(repr=False, frozen=True)
class ControlFeedback(ActionFeedback, Definition):
    _label: ClassVar[str] = 'Feedback-'

    feedback: str

    def __str__(self) -> str:
        return f'{self.controller} <- {self.feedback} <- {self.controlled}'
    
    def __eq__(self, other):
        if not isinstance(other, ControlFeedback):
            return False
        return self.feedback == other.feedback


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
            f'{self.get_label()}: {self.source}'
            f' {self._type_uca} {self.controlAction.action}'
            f' {self.context}'
            f' [{self.hazard.get_label()}]'
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