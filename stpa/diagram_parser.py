import xml.etree.ElementTree as ET

def parse(root: ET.Element):
    cells = []
    for cell in root.findall('mxCell'):
        if 'value' in cell.attrib and cell.attrib['value'] != '':
            cells.append(cell)
            print(cell.attrib['value'])
            if cell.attrib['parent'] == '1':
                print('\tprocess')
            else:
                print('\tarrow')

if __name__ == '__main__':
    xml_filename = '/home/aliraeis/Projekte/BlueSkySolarRacing/stpa/examples/simple_control_structure.drawio'
    tree = ET.parse(xml_filename)
    root = tree.getroot()[0][0][0]

    parse(root)