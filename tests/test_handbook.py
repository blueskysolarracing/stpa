from dataclasses import dataclass, field

from diagram_parser import DiagramParser
from definitions import Loss, Hazard
from definitions import ControlStructure, ControlAction, ControlFeedback
from definitions import UnsafeControlAction_notProviding

class handbook_example:
    flightcrew = ControlStructure('Flight Crew')
    aircraft = ControlStructure('Aircraft')
    wbs = ControlStructure('Wheel Braking Subsytem (WBS)')
    othersubsystems = ControlStructure('Other subsystems')
    bscu = ControlStructure('Brake System Control Unit(BSCU)')
    physicalbrakes = ControlStructure('Physical Wheel Brakes')
    ControlStructure.reset_counter()

    ac1 = ControlAction(controlled=othersubsystems, controller=flightcrew, action='Manual controls (Engine throttle, Steer, Reverse thrust, etc.)')
    ac2 = ControlAction(controlled=bscu, controller=flightcrew, action='Arm and Set, Disarm, Brake')
    ac3 = ControlAction(controlled=physicalbrakes, controller=bscu, action='Brake')
    ac4 = ControlAction(controlled=physicalbrakes, controller=flightcrew, action='Manual Braking')
    ControlAction.reset_counter()

    diagrams = {flightcrew, aircraft, wbs, othersubsystems, bscu, physicalbrakes, ac1, ac2, ac3, ac4}

example = handbook_example()

def test_fig2_11():
    xml_filename = '/home/aliraeis/Projekte/BlueSkySolarRacing/stpa/examples/handbook_fig2.11.drawio'
    parser2 = DiagramParser(xml_filename)
    diagram_elements = parser2.get_elements()

    assert(example.diagrams == diagram_elements)


def test_UCA_definitions():
    pass

