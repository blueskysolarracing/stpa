from dataclasses import dataclass
from typing import Union

import xml.etree.ElementTree as ET
import re
from bs4 import BeautifulSoup


@dataclass(repr=False)
class ControlStructure(Definition):
    # id: str
    name: str

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other) -> bool:
        if isinstance(other, ControlStructure):
            return self.name == other.name
        return False


@dataclass(repr=False)
class ActionFeedback(ABC):
    controlled: ControlStructure
    controller: ControlStructure


@dataclass(repr=False)
class ControlAction(ActionFeedback):
    action: str

    def __hash__(self):
        return hash((self.action, self.controlled.name, self.controller.name))

    def __eq__(self, other) -> bool:
        if isinstance(other, ControlAction):
            return self.action == other.action and self.controlled == other.controlled and self.controller == other.controller
        return False


@dataclass(repr=False)
class ControlFeedback(ActionFeedback):
    feedback: str

    def __hash__(self):
        return hash((self.feedback, self.controlled.name, self.controller.name))

    def __eq__(self, other) -> bool:
        if isinstance(other, ControlFeedback):
            return self.feedback == other.feedback and self.controlled == other.controlled and self.controller == other.controller
        return False

controlStructures: dict[str, ControlStructure] = {}
all_cells: dict[str, ET.Element] = {}

def isSameHeight(source_cell: ET.Element, target_cell: ET.Element) -> bool:
    source_geom = source_cell.find('mxGeometry')
    target_geom = target_cell.find('mxGeometry')
    return int(source_geom.attrib['y']) <= int(target_geom.attrib['y']) <= int(source_geom.attrib['y']) + int(source_geom.attrib['height']) or \
        int(target_geom.attrib['y']) <= int(source_geom.attrib['y']) <= int(target_geom.attrib['y']) + int(target_geom.attrib['height'])

def isSourceHigher(source_cell: ET.Element, target_cell: ET.Element) -> bool:
    source_geom = source_cell.find('mxGeometry')
    target_geom = target_cell.find('mxGeometry')
    return int(source_geom.attrib['y']) < int(target_geom.attrib['y'])

def isSourceToLeft(source_cell: ET.Element, target_cell: ET.Element) -> bool:
    source_geom = source_cell.find('mxGeometry')
    target_geom = target_cell.find('mxGeometry')
    return int(source_geom.attrib['x']) < int(target_geom.attrib['x'])

def isSourceController(source_cell: ET.Element, target_cell: ET.Element, arrow_value: str) -> bool:
    if arrow_value.lower().startswith('action'):
        return True
    elif arrow_value.lower().startswith('feedback'):
        return False

    if isSameHeight(source_cell, target_cell):
        return isSourceToLeft(source_cell, target_cell)
    return isSourceHigher(source_cell, target_cell)

def parse_arrow(cell: ET.Element) -> Union[ControlAction, ControlFeedback]:
    arrow_cell = all_cells[cell.attrib['parent']]
    arrow_value = cell.attrib['value']

    target = controlStructures[arrow_cell.attrib['target']]
    target_cell = all_cells[arrow_cell.attrib['target']]
    source = controlStructures[arrow_cell.attrib['source']]
    source_cell = all_cells[arrow_cell.attrib['source']]
    
    if isSourceController(source_cell, target_cell, arrow_value):
        return ControlAction(controlled=target, controller=source, action=arrow_value)
    else:
        return ControlFeedback(controller=target, controlled=source, feedback=arrow_value)
 

def parse_controlStructure(id: str, cell: ET.Element) -> ControlStructure:
    if id in controlStructures:
        raise ValueError(f'The Control Structure with id: {id} and value: {cell.attrib["value"]} has already been found')
    
    strct = ControlStructure(cell.attrib['value'])
    controlStructures[id] = strct
    return strct

def getAllCells(root: ET.Element, cellName='mxCell'):
    cells = []
    for cell in root.findall(cellName): 
        cells.append(cell)
        cells.extend(getAllCells(cell, cellName))
    return cells

def clean_text(html_text):
    # Remove HTML tags using BeautifulSoup
    soup = BeautifulSoup(html_text, "html.parser")
    clean = soup.get_text()
    
    # Remove extra spaces and non-printable characters
    clean = re.sub(r'\s+', ' ', clean)  # Replace multiple spaces with a single space
    clean = clean.strip()  # Remove leading and trailing spaces
    
    return clean

def parse_file(xml_filename: str) -> set[Union[ControlStructure, ControlAction, ControlFeedback]]:
    def iscontrolStructure(cell: ET.Element) -> bool:
        return cell.attrib['parent'] == '1'
    tree = ET.parse(xml_filename)
    root = tree.getroot()[0][0][0]

    diagram_elements = set()
    controlStructures, arrows = [], []

    # for cell in root.findall('mxCell'): 
    cells = getAllCells(root)
    for cell in cells: 
        id = cell.attrib['id'] 
        if id in all_cells: 
            raise ValueError(f'Cell with {id} is not unique') 
        all_cells[id] = cell 
        
        if 'value' in cell.attrib and cell.attrib['value'] != '': 
            cell.attrib['value'] = clean_text(cell.attrib['value'])
            print('Adding cell with value: ', cell.attrib['value'])
            if iscontrolStructure(cell):
                controlStructures.append(cell)
            else:
                arrows.append(cell)

    for cell in controlStructures:
        print(f'Parsing controlStructure with id: {cell.attrib['id']} and value: {cell.attrib['value']}')
        diagram_elements.add(parse_controlStructure(cell.attrib['id'], cell))

    for cell in arrows:
        print(f'Parsing arrow with id: {cell.attrib['id']} and value: {cell.attrib['value']}')
        diagram_elements.add(parse_arrow(cell))

    return diagram_elements


# xml_filename = '/home/aliraeis/Projekte/BlueSkySolarRacing/stpa/examples/handbook_fig2.11.drawio'
# diagram_elements = parse_file(xml_filename)
# print(diagram_elements)
