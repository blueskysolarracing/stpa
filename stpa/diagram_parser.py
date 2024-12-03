from typing import Union

import xml.etree.ElementTree as ET
import re
from bs4 import BeautifulSoup

from definitions import ControlStructure, ControlAction, ControlFeedback

class DiagramParser:
    def __init__(self, filename: str):
        self._controlStructures = {}
        self._all_cells = {}
        self._diagram_elements = set()
        self.parse_file(filename)
        ControlStructure.reset_counter()
        ControlAction.reset_counter()
        ControlFeedback.reset_counter()


    def get_elements(self) -> set[Union[ControlStructure, ControlAction, ControlFeedback]]:
        return self._diagram_elements


    def isSameHeight(self, source_cell: ET.Element, target_cell: ET.Element) -> bool:
        source_geom = source_cell.find('mxGeometry')
        target_geom = target_cell.find('mxGeometry')
        return int(source_geom.attrib['y']) <= int(target_geom.attrib['y']) <= int(source_geom.attrib['y']) + int(source_geom.attrib['height']) or \
            int(target_geom.attrib['y']) <= int(source_geom.attrib['y']) <= int(target_geom.attrib['y']) + int(target_geom.attrib['height'])


    def isSourceHigher(self, source_cell: ET.Element, target_cell: ET.Element) -> bool:
        source_geom = source_cell.find('mxGeometry')
        target_geom = target_cell.find('mxGeometry')
        return int(source_geom.attrib['y']) < int(target_geom.attrib['y'])


    def isSourceToLeft(self, source_cell: ET.Element, target_cell: ET.Element) -> bool:
        source_geom = source_cell.find('mxGeometry')
        target_geom = target_cell.find('mxGeometry')
        return int(source_geom.attrib['x']) < int(target_geom.attrib['x'])


    def isSourceController(self, source_cell: ET.Element, target_cell: ET.Element, arrow_value: str) -> bool:
        if arrow_value.lower().startswith('action'):
            return True
        elif arrow_value.lower().startswith('feedback'):
            return False


        if self.isSameHeight(source_cell, target_cell):
            return self.isSourceToLeft(source_cell, target_cell)
        return self.isSourceHigher(source_cell, target_cell)


    def parse_arrow(self, cell: ET.Element) -> Union[ControlAction, ControlFeedback]:
        arrow_cell = self._all_cells[cell.attrib['parent']]
        arrow_value = cell.attrib['value']

        target = self._controlStructures[arrow_cell.attrib['target']]
        target_cell = self._all_cells[arrow_cell.attrib['target']]
        source = self._controlStructures[arrow_cell.attrib['source']]
        source_cell = self._all_cells[arrow_cell.attrib['source']]
        
        if self.isSourceController(source_cell, target_cell, arrow_value):
            return ControlAction(controlled=target, controller=source, action=arrow_value)
        else:
            return ControlFeedback(controller=target, controlled=source, feedback=arrow_value)


    def parse_controlStructure(self, id: str, cell: ET.Element) -> ControlStructure:
        if id in self._controlStructures:
            raise ValueError(f'The Control Structure with id: {id}' + \
                f' and value: {cell.attrib['value']} has already been found')
        
        strct = ControlStructure(cell.attrib['value'])
        self._controlStructures[id] = strct
        return strct


    def getAllCells(self, root: ET.Element, cellName='mxCell'):
        cells = []
        for cell in root.findall(cellName): 
            cells.append(cell)
            cells.extend(self.getAllCells(cell, cellName))
        return cells


    @classmethod
    def clean_text(cls, html_text):
        # Remove HTML tags using BeautifulSoup
        soup = BeautifulSoup(html_text, "html.parser")
        clean = soup.get_text()
        
        # Remove extra spaces and non-printable characters
        clean = re.sub(r'\s+', ' ', clean)  # Replace multiple spaces with a single space
        clean = clean.strip()  # Remove leading and trailing spaces
        
        return clean


    def parse_file(self, xml_filename: str) -> set[Union[ControlStructure, ControlAction, ControlFeedback]]:
        def iscontrolStructure(cell: ET.Element) -> bool:
            return cell.attrib['parent'] == '1'
        tree = ET.parse(xml_filename)
        root = tree.getroot()[0][0][0]

        structures, arrows = [], []

        # for cell in root.findall('mxCell'): 
        cells = self.getAllCells(root)
        for cell in cells: 
            id = cell.attrib['id'] 
            if id in self._all_cells: 
                raise ValueError(f'Cell with {id} is not unique') 
            self._all_cells[id] = cell 
            
            if 'value' in cell.attrib and cell.attrib['value'] != '': 
                cell.attrib['value'] = DiagramParser.clean_text(cell.attrib['value'])
                print('Adding cell with value: ', cell.attrib['value'])
                if iscontrolStructure(cell):
                    structures.append(cell)
                else:
                    arrows.append(cell)

        for cell in structures:
            print(f'Parsing controlStructure with id: {cell.attrib['id']} and value: {cell.attrib['value']}')
            self._diagram_elements.add(self.parse_controlStructure(cell.attrib['id'], cell))

        for cell in arrows:
            print(f'Parsing arrow with id: {cell.attrib['id']} and value: {cell.attrib['value']}')
            self._diagram_elements.add(self.parse_arrow(cell))