from diagram_parser import parse_file
from diagrams import ControlStructure, ControlAction, ControlFeedback

# def test_example():
    # xml_filename = '/home/aliraeis/Projekte/BlueSkySolarRacing/stpa/examples/simple_control_structure.drawio'

def test_fig2_11():
    flightcrew = ControlStructure('Flight Crew')
    aircraft = ControlStructure('Aircraft')
    wbs = ControlStructure('Wheel Braking Subsytem (WBS)')
    othersubsystems = ControlStructure('Other subsystems')
    bscu = ControlStructure('Brake System Control Unit(BSCU)')
    physicalbrakes = ControlStructure('Physical Wheel Brakes')

    ac1 = ControlAction(controlled=othersubsystems, controller=flightcrew, action='Manual controls (Engine throttle, Steer, Reverse thrust, etc.)')
    ac2 = ControlAction(controlled=bscu, controller=flightcrew, action='Arm and Set, Disarm, Brake')
    ac3 = ControlAction(controlled=physicalbrakes, controller=bscu, action='Brake')
    ac4 = ControlAction(controlled=physicalbrakes, controller=flightcrew, action='Manual Braking')

    expected_diagrams = {flightcrew, aircraft, wbs, othersubsystems, bscu, physicalbrakes, ac1, ac2, ac3, ac4}

    xml_filename = '/home/aliraeis/Projekte/BlueSkySolarRacing/stpa/examples/handbook_fig2.11.drawio'
    diagram_elements = parse_file(xml_filename)
    print(diagram_elements)

    assert(expected_diagrams == diagram_elements)