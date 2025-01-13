from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from re import compile, fullmatch, Pattern
from typing import ClassVar
from warnings import warn


@dataclass(repr=False)
class Definition(ABC):
    _NAME_PATTERN: ClassVar[Pattern[str]]
    __lookup: ClassVar[dict[str, Definition]] = {}
    name: str

    @classmethod
    def clear(cls) -> None:
        cls.__lookup.clear()

    @classmethod
    def get(cls, name: str) -> Definition:
        return cls.__lookup[name]

    @classmethod
    def get_all(cls, *names: str) -> list[Definition]:
        return list(map(cls.get, names))

    def __post_init__(self) -> None:
        if self.name in self.__lookup:
            warn(f'name {repr(self.name)} is already defined')

        if not fullmatch(self._NAME_PATTERN, self.name):
            warn('name {repr(self.name)} doesn\'t follow the standard pattern')

        self.__lookup[self.name] = self

    def __repr__(self) -> str:
        return self.name

    @abstractmethod
    def __str__(self) -> str:
        pass


@dataclass(repr=False)
class Loss(Definition):
    _NAME_PATTERN = compile(r'L-\d+')
    description: str

    def __str__(self) -> str:
        return f'{self.name}: {self.description}'


@dataclass(repr=False)
class Hazard(Definition):
    _NAME_PATTERN = compile(r'H-\d+')
    system: str
    unsafe_condition: str
    losses: list[Loss]

    def __str__(self) -> str:
        if not self.system:
            str_ = f'{self.name}: {self.unsafe_condition} {self.losses}'
        elif '{}' in self.unsafe_condition:
            str_ = (
                f'{self.name}:'
                f' {self.unsafe_condition.format(self.system)}'
                f' {self.losses}'
            )
        else:
            str_ = (
                f'{self.name}:'
                f' {self.system}'
                f' {self.unsafe_condition}'
                f' {self.losses}'
            )

        return str_


@dataclass(repr=False)
class SystemLevelConstraint(Definition, ABC):
    _NAME_PATTERN = compile(r'SC-\d+')
    pass


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
class SystemLevelConstraintType3(SystemLevelConstraint):
    _NAME_PATTERN = compile(r'SC-\d+\.\d+')
    sub_hazard: SubHazard
    enforcement_condition: str

    def __str__(self) -> str:
        return f'{self.name}: {self.enforcement_condition}'


@dataclass(repr=False)
class SubHazard(SystemLevelConstraint):
    _NAME_PATTERN = compile(r'H-\d+\.\d+')
    hazard: Hazard
    description: str

    def __str__(self) -> str:
        return f'{self.name}: {self.description}'


@dataclass(repr=False)
class Responsibility(Definition):
    _NAME_PATTERN = compile(r'R-\d+')
    description: str
    system_level_constraints: list[SystemLevelConstraint]

    def __str__(self) -> str:
        return (
            f'{self.name}:'
            f' {self.description}'
            f' {self.system_level_constraints}'
        )


@dataclass(repr=False)
class UnsafeControlAction(Definition):
    _NAME_PATTERN = compile(r'UCA-\d+')
    source: str
    type_: str
    control_action: str
    context: str
    hazards: list[Hazard | SubHazard]

    def __str__(self) -> str:
        if '{}' in self.type_:
            str_ = (
                f'{self.name}:'
                f' {self.source}'
                f' {self.type_.format(self.control_action)}'
                f' {self.context}'
                f' {self.hazards}'
            )
        else:
            str_ = (
                f'{self.name}:'
                f' {self.source}'
                f' {self.type_}'
                f' {self.control_action}'
                f' {self.context}'
                f' {self.hazards}'
            )

        return str_


@dataclass(repr=False)
class ControllerConstraint(Definition):
    _NAME_PATTERN = compile(r'C-\d+')
    source: str
    type_: str
    control_action: str
    context: str
    unsafe_control_actions: list[UnsafeControlAction]

    def __str__(self) -> str:
        if '{}' in self.type_:
            str_ = (
                f'{self.name}:'
                f' {self.source}'
                f' {self.type_.format(self.control_action)}'
                f' {self.context}'
                f' {self.unsafe_control_actions}'
            )
        else:
            str_ = (
                f'{self.name}:'
                f' {self.source}'
                f' {self.type_}'
                f' {self.control_action}'
                f' {self.context}'
                f' {self.unsafe_control_actions}'
            )

        return str_


@dataclass(repr=False)
class Scenario(Definition):
    pass


@dataclass(repr=False)
class ScenarioType1(Scenario):
    _NAME_PATTERN = compile(r'Scenario \d+ for UCA-\d+')
    description: str
    unsafe_control_action: UnsafeControlAction | None
    result: str | None = None
    hazard: Hazard | None = None

    def __post_init__(self) -> None:
        super().__post_init__()

        if (self.result is None) != (self.hazard is None):
            raise ValueError('result and hazard nullnesses must be the same')

    def __str__(self) -> str:
        if '{}' in self.description:
            str_ = (
                f'{self.name}:'
                f' {self.description.format([self.unsafe_control_action])}'
            )
        else:
            str_ = (
                f'{self.name}:'
                f' {self.description}'
                f' {[self.unsafe_control_action]}.'
            )

        if self.result is not None:
            if not str_[-1].isspace():
                str_ += ' '

            str_ += f'As a result, {self.result} {[self.hazard]}.'

        return str_


@dataclass(repr=False)
class ScenarioType2(Scenario):
    _NAME_PATTERN = compile(r'Scenario \d+')
    description: str
    result: str
    hazard: Hazard

    def __str__(self) -> str:
        return (
            f'{self.name}:'
            f' {self.description}'
            f' As a result, {self.result}'
            f' {[self.hazard]}.'
        )
