from dataclasses import dataclass, field

from diagram_parser import DiagramParser
from definitions import Loss, Hazard
from definitions import ControlStructure, ControlAction, ControlFeedback
from definitions import UnsafeControlAction_notProviding

class handbook_example:
    loss1 = Loss('Loss of life or injury to people')
    loss2 = Loss('Loss of or damage to vehicle')
    loss3 = Loss('Loss of or damage to objects outside the vehicle')
    loss4 = Loss('Loss of mission (e.g. transportation mission, surveillance mission, scientific mission, defense mission, etc.)')
    loss5 = Loss('Loss of customer satisfaction')
    loss6 = Loss('Loss of sensitive information')
    loss7 = Loss('Environmental loss')
    loss8 = Loss('Loss of power generation')
    Loss.reset_counter()

    losses = [loss1, loss2, loss3, loss4, loss5, loss6, loss7, loss8]

    hazard1 = Hazard('Aircraft', 'violate minimum separation standards in flight', [loss1, loss2, loss4, loss5])
    hazard2 = Hazard('Aircraft', 'airframe integrity is lost', [loss1, loss2, loss4, loss5])
    hazard3 = Hazard('Aircraft', 'leaves designated taxiway, runway, or apron on ground', [loss1, loss2, loss5])
    hazard4 = Hazard('Aircraft', 'comes too close to other objects on the ground', [loss1, loss2, loss5])
    hazard5 = Hazard('Satellite', 'is unable to collect scientific data', [loss4])
    hazard6 = Hazard('Vehicle',  'does not maintain safe distance from terrain and other obstacles', [loss1, loss2, loss3, loss4])
    hazard7 = Hazard('UAV', 'does not complete surveillance mission', [loss4])
    hazard8 = Hazard('Nuclear power plant', 'releases dangerous materials', [loss1, loss4, loss7, loss8])
    Hazard.reset_counter()

    hazards = [hazard1, hazard2, hazard3, hazard4, hazard5, hazard6, hazard7, hazard8]

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

def test_losses():
    for i, loss in enumerate(example.losses, start=1):
        assert(f'L-{i}' == loss.get_label())
        assert(f'L-{i}: {loss.description}' == str(loss))

def test_hazards():
    for i, hazard in enumerate(example.hazards, start=1):
        assert(f'H-{i}' == hazard.get_label())
    
    assert(str(example.hazard1) == 'H-1: Aircraft violate minimum separation standards in flight [L-1, L-2, L-4, L-5]')
    assert(str(example.hazard2) == 'H-2: Aircraft airframe integrity is lost [L-1, L-2, L-4, L-5]')
    assert(str(example.hazard3) == 'H-3: Aircraft leaves designated taxiway, runway, or apron on ground [L-1, L-2, L-5]')
    assert(str(example.hazard4) == 'H-4: Aircraft comes too close to other objects on the ground [L-1, L-2, L-5]')
    assert(str(example.hazard5) == 'H-5: Satellite is unable to collect scientific data [L-4]')
    assert(str(example.hazard6) == 'H-6: Vehicle does not maintain safe distance from terrain and other obstacles [L-1, L-2, L-3, L-4]')
    assert(str(example.hazard7) == 'H-7: UAV does not complete surveillance mission [L-4]')
    assert(str(example.hazard8) == 'H-8: Nuclear power plant releases dangerous materials [L-1, L-4, L-7, L-8]')


def test_fig2_11():
    xml_filename = '/home/aliraeis/Projekte/BlueSkySolarRacing/stpa/examples/handbook_fig2.11.drawio'
    parser2 = DiagramParser(xml_filename)
    diagram_elements = parser2.get_elements()

    assert(example.diagrams == diagram_elements)


def test_UCA_definitions():
    pass

