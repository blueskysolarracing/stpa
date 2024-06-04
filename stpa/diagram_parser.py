import xml.etree.ElementTree as ET

from diagrams import ControlStructure, ControlActionFeedback 

def parse_process(cell: ET.Element) -> ControlStructure:
    return ControlStructure(cell.attrib['id'], cell.attrib['value'])

def parse(root: ET.Element):
    cells = []
    for cell in root.findall('mxCell'):
        if 'value' in cell.attrib and cell.attrib['value'] != '':
            cells.append(cell)
            print(cell.attrib['value'])
            if cell.attrib['parent'] == '1':
                print('\tprocess')
                structure = parse_process(cell)
                print(structure)
            else:
                print('\tarrow')

if __name__ == '__main__':
    xml_filename = '/home/aliraeis/Projekte/BlueSkySolarRacing/stpa/examples/simple_control_structure.drawio'
    tree = ET.parse(xml_filename)
    root = tree.getroot()[0][0][0]

    parse(root)