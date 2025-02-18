# type: ignore

from stpa.definitions import Definition, Hazard, SubHazard, UnsafeControlAction
from stpa.examples.stpa_handbook.chapter_3 import definitions 

UNSAFE_CONTROL_ACTIONS = (
    UnsafeControlAction(
        'CREW.1a1',
        'Crew',
        'does not provide',
        'manual braking',
        (
            'during landing, RTO, or taxiing when Autobrake is not providing'
            ' braking or is providing insufficient braking'
        ),
        Definition.get_all('H4.1'),
    ),
    UnsafeControlAction(
        'CREW.1b1',
        'Crew',
        'provides',
        'manual braking',
        'with insufficient pedal pressure',
        Definition.get_all('H4.1'),
    ),
    UnsafeControlAction(
        'CREW.1b2',
        'Crew',
        'provides',
        'manual braking',
        (
            'with excessive pedal pressure (resulting in loss of control,'
            ' passenger/crew injury, brake overheating, brake fade or tire'
            ' burst during landing)'
        ),
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'CREW.1b3',
        'Crew',
        'provides',
        'manual braking',
        'provided during normal takeoff',
        Definition.get_all('H4-2', 'H4-5'),
    ),
    UnsafeControlAction(
        'CREW.1c1',
        'Crew',
        'provides',
        'manual braking',
        'before touchdown (causes wheel lockup, loss of control, tire burst)',
        Definition.get_all('H4.1'),
    ),
    UnsafeControlAction(
        'CREW.1c2',
        'Crew',
        'provides {} too late (TBD)',
        'manual braking',
        (
            'to avoid collision or conflict with another object (can overload'
            ' braking capability given aircraft weight, speed, distance to'
            ' object (conflict), and tarmac conditions)'
        ),
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'CREW.1d1',
        'Crew',
        'stops providing',
        'manual braking command',
        'before safe taxi speed (TBD) is reached',
        Definition.get_all('H4.1', 'H4.4'),
    ),
    UnsafeControlAction(
        'CREW.1d2',
        'Crew',
        'provides {} too long',
        'manual braking',
        '(resulting in stopped aircraft on runway or active taxiway)',
        Definition.get_all('H4-1'),
    ),
    UnsafeControlAction(
        'CREW.2a1',
        'Crew',
        'does not arm',
        'Autobrake',
        (
            'before landing (causing loss of automatic brake operation when'
            ' spoilers deploy. Crew reaction time may lead to overshoot.)'
        ),
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'CREW.2a2',
        'Crew',
        'does not arm',
        'Autobrake',
        (
            'prior to takeoff (resulting in insufficient braking during'
            ' rejected takeoff, assuming that Autobrake is responsible for'
            ' braking during RTO after crew throttle down)'
        ),
        Definition.get_all('H4-2'),
    ),
    UnsafeControlAction(
        'CREW.2b1',
        'Crew',
        'does not arm',
        'Autobrake',
        (
            'to maximum level during takeoff. (assumes that maximum braking'
            ' force is necessary for rejected takeoff)'
        ),
        Definition.get_all('H4-2'),
    ),
    UnsafeControlAction(
        'CREW.2b2',
        'Crew',
        'armed {} with too high of a deceleration rate',
        'autobrake',
        (
            'for runway conditions (resulting in loss of control and passenger'
            ' or crew injury).'
        ),
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'CREW.2c1',
        'Crew',
        'provides {} too late (TBD)',
        'arm command',
        '(resulting in insufficient time for BSCU to apply brakes)',
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'CREW.3a1',
        'Crew',
        'does not disarm',
        'Autobrake',
        'during TOGA (resulting in loss of acceleration during (re)takeoff)',
        Definition.get_all('H4-1', 'H4-2', 'H4-5'),
    ),
    UnsafeControlAction(
        'CREW.3b1',
        'Crew',
        'disarms',
        'Autobrake',
        (
            'during landing or RTO (resulting in loss of automatic brake'
            ' operation when spoilers deploy. Crew reaction time may lead to'
            ' overshoot)'
        ),
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'CREW.3c1',
        'Crew',
        'disarms {} more than TBD seconds',
        'Autobrake',
        (
            'after (a) aircraft descent exceeds TBD fps, (b) visibility is'
            ' less than TBD ft, (c) etc…, (resulting in either loss of control'
            ' of aircraft or loss of acceleration during (re)takeoff)'
        ),
        Definition.get_all('H4-1', 'H4-2', 'H4-5'),
    ),
    UnsafeControlAction(
        'CREW.4a1',
        'Crew',
        'does not power off',
        'BSCU',
        (
            'in the event of abnormal WBS behavior (needed to enable alternate'
            ' braking mode)'
        ),
        Definition.get_all('H4-1', 'H4-2', 'H4-5'),
    ),
    UnsafeControlAction(
        'CREW.4b1',
        'Crew',
        'powers off',
        'BSCU',
        'when Autobraking is needed and WBS functioning normally',
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'CREW.4b2',
        'Crew',
        'powers off',
        'BSCU',
        (
            'when Autobrake is needed (or about to be used) and WBS if'
            ' funtioning normally'
        ),
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'CREW.4b3',
        'Crew',
        'powers off',
        'BSCU',
        (
            'when Anti-Skid functionality is needed (or will be needed) and'
            ' WBS is functioning normally'
        ),
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'CREW.4c1',
        'Crew',
        'powers off {} too late',
        'BSCU',
        (
            '(TBD) to enable alternate braking mode in the event of abnormal'
            ' WBS behavior'
        ),
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'CREW.4c2',
        'Crew',
        'powers off {} too early',
        'BSCU',
        (
            'before Autobrake or Anti-Skid behavior is completed when it is'
            ' needed'
        ),
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'CREW.5a1',
        'Crew',
        'does not power on',
        'BSCU',
        (
            'when Normal braking mode, Autobrake, or Anti-Skid is to be used'
            ' and WBS functioning normally'
        ),
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'CREW.5c1',
        'Crew',
        'powers on {} too late',
        'BSCU',
        'after Normal braking mode, Autobrake, or Anti-Skid is needed',
        Definition.get_all('H4-1', 'H4-5'),
    ),
)
