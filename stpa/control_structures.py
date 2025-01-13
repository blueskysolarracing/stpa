from __future__ import annotations

from dataclasses import dataclass
from enum import auto, Enum
from pathlib import Path
import xml.etree.ElementTree as ET

from stpa.utilities import clean_html_text

GEOMETRY_TAG_NAME = 'mxGeometry'
CELL_TAG_NAME = 'mxCell'
CONTROL_STRUCTURE_PARENT = '1'


class ControlType(Enum):
    ACTION = auto()
    FEEDBACK = auto()


@dataclass(frozen=True)
class Entity:
    name: str


@dataclass(frozen=True)
class ControlActionOrFeedback:
    description: str
    control_type: ControlType
    controller: Entity
    controlled: Entity


@dataclass(frozen=True)
class ControlStructure:
    @classmethod
    def get_control_type(
            cls,
            source_cell: ET.Element,
            target_cell: ET.Element,
    ) -> ControlType:
        source_geometry = source_cell.find(GEOMETRY_TAG_NAME)
        target_geometry = target_cell.find(GEOMETRY_TAG_NAME)

        assert source_geometry is not None
        assert target_geometry is not None

        source_x = int(source_geometry.attrib['x'])
        source_y = int(source_geometry.attrib['y'])
        source_height = int(source_geometry.attrib['height'])
        target_x = int(target_geometry.attrib['x'])
        target_y = int(target_geometry.attrib['y'])
        target_height = int(source_geometry.attrib['height'])
        status = False

        if (
                source_y <= target_y <= source_y + source_height
                or target_y <= source_y <= target_y + target_height
        ):
            status = source_x < target_x
        else:
            status = source_y < target_y

        return ControlType.ACTION if status else ControlType.FEEDBACK

    @classmethod
    def parse_diagram(cls, source: str | Path) -> ControlStructure:
        tree = ET.parse(source)
        root = tree.getroot()[0][0][0]
        cells = {}
        cleaned_values = {}

        for cell in root.findall(CELL_TAG_NAME):
            id_ = cell.attrib['id']
            cells[id_] = cell

            if 'value' in cell.attrib:
                value = cell.attrib['value']
                cleaned_value = clean_html_text(value)
                cleaned_values[id_] = cleaned_value

        entities = {}
        parent_cleaned_values = {}

        for cell in cells.values():
            id_ = cell.attrib['id']
            cleaned_value = cleaned_values.get(id_, '')
            parent = cell.attrib.get('parent', '')

            if cleaned_value:
                if parent == CONTROL_STRUCTURE_PARENT:
                    entities[id_] = Entity(cleaned_value)
                else:
                    parent_cleaned_values[parent] = cleaned_value

        control_actions_or_feedbacks = []

        for cell in cells.values():
            if (
                    cell.attrib.get('edge') == '1'
                    and 'source' in cell.attrib
                    and 'target' in cell.attrib
            ):
                id_ = cell.attrib['id']
                cleaned_value = parent_cleaned_values.get(id_, '')
                source_cell = cells[cell.attrib['source']]
                target_cell = cells[cell.attrib['target']]

                if cleaned_value.lower().startswith('action'):
                    control_type = ControlType.ACTION
                elif cleaned_value.lower().startswith('feedback'):
                    control_type = ControlType.FEEDBACK
                else:
                    control_type = cls.get_control_type(
                        source_cell,
                        target_cell,
                    )

                source_entity = entities[cell.attrib['source']]
                target_entity = entities[cell.attrib['target']]

                match control_type:
                    case ControlType.ACTION:
                        controller, controlled = source_entity, target_entity
                    case ControlType.FEEDBACK:
                        controller, controlled = target_entity, source_entity
                    case _:
                        raise ValueError(
                            f'unknown control type {repr(control_type)}',
                        )

                control_action_or_feedback = ControlActionOrFeedback(
                    cleaned_value,
                    control_type,
                    controller,
                    controlled,
                )

                control_actions_or_feedbacks.append(control_action_or_feedback)

        return cls(
            frozenset(entities.values()),
            frozenset(control_actions_or_feedbacks),
        )

    entities: frozenset[Entity]
    control_actions_or_feedbacks: frozenset[ControlActionOrFeedback]
