# type: ignore

from textwrap import dedent

from stpa.definitions import (
    ControllerConstraint,
    Definition,
    Hazard,
    Loss,
    Responsibility,
    ScenarioType1,
    ScenarioType2,
    SubHazard,
    SystemLevelConstraintType1,
    SystemLevelConstraintType2,
    SystemLevelConstraintType3,
    UnsafeControlAction,
)

LOSSES = (
    Loss('L-1', 'Loss of life or injury to people'),
    Loss('L-2', 'Loss of or damage to vehicle'),
    Loss('L-3', 'Loss of or damage to objects outside the vehicle'),
    Loss(
        'L-4',
        (
            'Loss of mission (e.g. transportation mission, surveillance'
            ' mission, scientific mission, defense mission, etc.)'
        ),
    ),
    Loss('L-5', 'Loss of customer satisfaction'),
    Loss('L-6', 'Loss of sensitive information'),
    Loss('L-7', 'Environmental loss'),
    Loss('L-8', 'Loss of power generation'),
)

HAZARDS = (
    Hazard(
        'H-1',
        'Aircraft',
        'violate minimum separation standards in flight',
        Definition.get_all('L-1', 'L-2', 'L-4', 'L-5'),
    ),
    Hazard(
        'H-2',
        'Aircraft',
        'airframe integrity is lost',
        Definition.get_all('L-1', 'L-2', 'L-4', 'L-5'),
    ),
    Hazard(
        'H-3',
        'Aircraft',
        'leaves designated taxiway, runway, or apron on ground',
        Definition.get_all('L-1', 'L-2', 'L-5'),
    ),
    Hazard(
        'H-4',
        'Aircraft',
        'comes too close to other objects on the ground',
        Definition.get_all('L-1', 'L-2', 'L-5'),
    ),
    Hazard(
        'H-5',
        'Satellite',
        'is unable to collect scientific data',
        Definition.get_all('L-4'),
    ),
    Hazard(
        'H-6',
        'Vehicle',
        'does not maintain safe distance from terrain and other obstacles',
        Definition.get_all('L-1', 'L-2', 'L-3', 'L-4'),
    ),
    Hazard(
        'H-7',
        'UAV',
        'does not complete surveillance mission',
        Definition.get_all('L-4'),
    ),
    Hazard(
        'H-8',
        'Nuclear power plant',
        'releases dangerous materials',
        Definition.get_all('L-1', 'L-4', 'L-7', 'L-8'),
    ),
)

SYSTEM_LEVEL_CONSTRAINTS = (
    SystemLevelConstraintType1(
        'SC-1',
        'Aircraft',
        (
            'must satisfy minimum separation standards from other aircraft and'
            ' objects'
        ),
        Definition.get_all('H-1'),
    ),
    SystemLevelConstraintType1(
        'SC-2',
        'Aircraft',
        'airframe integrity must be maintained under worst-case conditions',
        Definition.get_all('H-2'),
    ),
    SystemLevelConstraintType2(
        'SC-3',
        Definition.get('H-1'),
        (
            'the violation must be detected and measures taken to prevent'
            ' collision'
        ),
        Definition.get_all('H-1'),
    ),
)

SUB_HAZARDS = {
    'H-4': (
        # Deceleration
        SubHazard(
            'H-4.1',
            Definition.get('H-4'),
            (
                'Deceleration is insufficient upon landing, rejected takeoff,'
                ' or during taxiing'
            ),
        ),
        SubHazard(
            'H-4.2',
            Definition.get('H-4'),
            'Asymmetric deceleration maneuvers aircraft toward other objects',
        ),
        SubHazard(
            'H-4.3',
            Definition.get('H-4'),
            'Deceleration occurs after V1 point during takeoff',
        ),
        # Acceleration
        SubHazard(
            'H-4.4',
            Definition.get('H-4'),
            'Excessive acceleration provided while taxiing',
        ),
        SubHazard(
            'H-4.5',
            Definition.get('H-4'),
            'Asymmetric acceleration maneuvers aircraft toward other objects',
        ),
        SubHazard(
            'H-4.6',
            Definition.get('H-4'),
            'Acceleration is insufficient during takeoff',
        ),
        SubHazard(
            'H-4.7',
            Definition.get('H-4'),
            'Acceleration is provided during landing or when parked',
        ),
        SubHazard(
            'H-4.8',
            Definition.get('H-4'),
            'Acceleration continues to be applied during rejected takeoff',
        ),
        # Steering
        SubHazard(
            'H-4.9',
            Definition.get('H-4'),
            (
                'Insufficient steering to turn along taxiway, runway, or apron'
                ' path'
            ),
        ),
        SubHazard(
            'H-4.10',
            Definition.get('H-4'),
            (
                'Steering maneuvers aircraft off the taxiway, runway, or apron'
                ' path'
            ),
        ),
    )
}

SYSTEM_LEVEL_CONSTRAINTS += (
    SystemLevelConstraintType3(
        'SC-6.1',
        Definition.get('H-4.1'),
        (
            'Deceleration must occur within TBD seconds of landing or rejected'
            ' takeoff at a rate of at least TBD m/s^2'
        ),
    ),
    SystemLevelConstraintType3(
        'SC-6.2',
        Definition.get('H-4.2'),
        (
            'Asymmetric deceleration must not lead to loss of directional'
            ' control or cause aircraft to depart taxiway, runway, or apron'
        ),
    ),
    SystemLevelConstraintType3(
        'SC-6.3',
        Definition.get('H-4.3'),
        'Deceleration must not be provided after V1 point during takeoff',
    ),
)

RESPONSIBILITIES = (
    # Physical Wheel Brakes
    Responsibility(
        'R-1',
        'Decelerate wheels when commanded by BSCU or Flight Crew',
        Definition.get_all('SC-6.1'),
    ),
    # BSCU
    Responsibility(
        'R-2',
        'Actuate brakes when requested by flight crew',
        Definition.get_all('SC-6.1'),
    ),
    Responsibility(
        'R-3',
        'Pulse brakes in case of a skid (Anti-skid)',
        Definition.get_all('SC-6.2'),
    ),
    Responsibility(
        'R-4',
        (
            'Automatically engage brakes on landing or rejected takeoff'
            ' (Autobrake)'
        ),
        Definition.get_all('SC-6.1'),
    ),
    # Flight crew
    Responsibility(
        'R-5',
        'Decide when braking is needed',
        Definition.get_all('SC-6.1', 'SC-6.3'),
    ),
    Responsibility(
        'R-6',
        (
            'Decide how braking will be done: Autobrake, normal braking, or'
            ' manual braking'
        ),
        Definition.get_all('SC-6.1'),
    ),
    Responsibility(
        'R-7',
        'Configure BSCU and Autobrake to prepare for braking',
        Definition.get_all('SC-6.1'),
    ),
    Responsibility(
        'R-8',
        (
            'Monitor braking and disable BSCU, manually brake in case of'
            ' malfunction'
        ),
        Definition.get_all('SC-6.1', 'SC-6.2'),
    ),
)

UNSAFE_CONTROL_ACTIONS = (
    # Brake

    # Not providing causes hazard
    UnsafeControlAction(
        'UCA-1',
        'BSCU Autobrake',
        'does not provide',
        'the Brake control action',
        'during landing roll when the BSCU is armed',
        Definition.get_all('H-4.1'),
    ),
    # Providing causes hazard
    UnsafeControlAction(
        'UCA-2',
        'BSCU Autobrake',
        'provides',
        'Brake control action',
        'during a normal takeoff',
        Definition.get_all('H-4.3', 'H-4.6'),
    ),
    UnsafeControlAction(
        'UCA-5',
        'BSCU Autobrake',
        'provides',
        'Brake control action with an insufficient level of braking',
        'during landing roll',
        Definition.get_all('H-4.1'),
    ),
    UnsafeControlAction(
        'UCA-6',
        'BSCU Autobrake',
        'provides',
        'Brake control action with directional or asymmetrical braking',
        'during landing roll',
        Definition.get_all('H-4.1', 'H-4.2'),
    ),
    # Too early, too late, our of order
    UnsafeControlAction(
        'UCA-3',
        'BSCU Autobrake',
        'provides {} too late (>TBD seconds)',
        'the Brake control action',
        'after touchdown',
        Definition.get_all('H-4.1'),
    ),
    # Stopped too soon, applied too long
    UnsafeControlAction(
        'UCA-4',
        'BSCU Autobrake',
        'stops providing {} too early (before TBD taxi speed attained)',
        'the Brake control action',
        'when aircraft lands',
        Definition.get_all('H-4.1'),
    ),

    # Power Off BSCU

    # Not providing causes hazard
    UnsafeControlAction(
        'Crew-UCA-1',
        'Crew',
        'does not provide',
        'BSCU Power Off',
        'when abnormal WBS behavior occurs',
        Definition.get_all('H-4.1', 'H-4.4', 'H-7'),
    ),
    # Providing causes hazard
    UnsafeControlAction(
        'Crew-UCA-2',
        'Crew',
        'provides',
        'BSCU Power Off',
        (
            'when Anti-Skid functionality is needed and WBS is functioning'
            ' normally'
        ),
        Definition.get_all('H-4.1', 'H-7'),
    ),
    # Too early, too late, our of order
    UnsafeControlAction(
        'Crew-UCA-3',
        'Crew',
        (
            'powers off {} too early before Autobrake or Anti-Skid behavior is'
            ' completed'
        ),
        'BSCU',
        'when it is needed',
        Definition.get_all('H-4.1', 'H-7'),
    ),
    # Stopped too soon, applied too long
)

CONTROLLER_CONSTRAINTS = (
    ControllerConstraint(
        'C-1',
        'BSCU Autobrake',
        'must provide',
        'the Brake control action',
        'during landing roll when the BSCU is armed',
        Definition.get_all('UCA-1'),
    ),
    ControllerConstraint(
        'C-2',
        'BSCU Autobrake',
        'must not provide',
        'Brake control action',
        'during a normal takeoff',
        Definition.get_all('UCA-2'),
    ),
    ControllerConstraint(
        'C-3',
        'BSCU Autobrake',
        'must provide {} within TBD seconds',
        'the Brake control action',
        'after touchdown',
        Definition.get_all('UCA-3'),
    ),
    ControllerConstraint(
        'C-4',
        'BSCU Autobrake',
        'must not stop providing {} before TBD taxi speed is attained',
        'the Brake control action',
        'during landing roll',
        Definition.get_all('UCA-4'),
    ),
    ControllerConstraint(
        'C-5',
        'BSCU Autobrake',
        'must not provide',
        'less than TBD level of braking',
        'during landing roll',
        Definition.get_all('UCA-5'),
    ),
    ControllerConstraint(
        'C-6',
        'BSCU Autobrake',
        'must not provide',
        'directional or asymmetrical braking',
        'during landing roll',
        Definition.get_all('UCA-6'),
    ),
)

SCENARIOS = (
    ScenarioType1(
        'Scenario 1 for UCA-1',
        (
            'The BSCU Autobrake physical controller fails during landing roll'
            ' when BSCU is armed, causing the Brake control action to not be'
            ' provided'
        ),
        Definition.get('UCA-1'),
        'insufficient deceleration may be provided upon landing',
        Definition.get('H-4.1'),
    ),
    ScenarioType1(
        'Scenario 1 for UCA-3',
        (
            'The aircraft lands, but processing delays within the BSCU result'
            ' in the Brake control action being provided too late'
        ),
        Definition.get('UCA-3'),
        'insufficient deceleration may be provided upon landing',
        Definition.get('H-4.1'),
    ),
    ScenarioType1(
        'Scenario 1 for Crew-UCA-1',
        (
            'Abnormal WBS behavior occurs and a BSCU fault indication is'
            ' provided to the crew. The crew does not power off the BSCU {}'
            ' because the operating procedures did not specify that the crew'
            ' must power off the BSCU upon receiving a BSCU fault indication.'
        ),
        Definition.get('Crew-UCA-1'),
    ),
    ScenarioType1(
        'Scenario 1 for UCA-2',
        (
            'The BSCU is armed and the aircraft begins landing roll. The BSCU'
            ' does not provide the Brake control action {} because the BSCU'
            ' incorrectly believes the aircraft has already come to a stop.'
            ' This flawed process model will occur if the received feedback'
            ' momentarily indicates zero speed during landing roll. The'
            ' received feedback may momentarily indicate zero speed during'
            ' anti-skid operation, even though the aircraft is not stopped.'
        ),
        Definition.get('UCA-2'),
    ),
    ScenarioType1(
        'Scenario 2 for UCA-2',
        dedent(
            '''\
            The BSCU is armed and the aircraft begins landing roll. The BSCU\
 does not provide the Brake control action {} because the BSCU\
 incorrectly believes the aircraft is in the air and has not\
 touched down. This flawed process model will occur if the\
 touchdown indication is not received upon touchdown. The\
 touchdown indication may not be received when needed if any of\
 the following occur:

            - Wheels hydroplane due to a wet runway (insufficient wheel speed)
            - Wheel speed feedback is delayed due to filtering used
            - Conflicting air/ground indications due to crosswind landing
            - Failure of wheel speed sensors
            - Failure of air/ground switches
            - Etc.

            ''',
        ),
        Definition.get('UCA-2'),
        'insufficient deceleration may be provided upon landing',
        Definition.get('H-4.1'),
    ),
    ScenarioType2(
        'Scenario 1',
        (
            'The BSCU sends the Brake command upon landing, but the brakes are'
            ' not applied due to actuator failure.'
        ),
        'insufficient deceleration may be provided upon landing',
        Definition.get('H-4.1'),
    ),
    ScenarioType2(
        'Scenario 2',
        (
            'The BSCU sends the Brake command upon landing, but insufficient'
            ' braking is applied due to slow actuator response.'
        ),
        'insufficient deceleration may be provided upon landing',
        Definition.get('H-4.1'),
    ),
    ScenarioType2(
        'Scenario 3',
        (
            'The BSCU sends the Brake command upon landing, but it is not'
            ' received by the actuator due to a wiring error.'
        ),
        'insufficient deceleration may be provided upon landing',
        Definition.get('H-4.1'),
    ),
    ScenarioType2(
        'Scenario 4',
        (
            'The BSCU does not send Brake command, but the brakes are applied'
            ' due to hydraulic valve failure.'
        ),
        'acceleration may be insufficient during takeoff',
        Definition.get('H-4.6'),
    ),
    ScenarioType2(
        'Scenario 5',
        (
            'The BSCU sends the Brake command, but the brakes are not applied'
            ' because an adversary executes a denial of service attack that'
            ' blocks the Brake command.'
        ),
        'insufficient deceleration may be provided upon landing',
        Definition.get('H-4.1'),
    ),
    ScenarioType2(
        'Scenario 6',
        (
            'The BSCU sends Brake command, but the brakes are not applied'
            ' because the wheel braking system was previously commanded into'
            ' alternate braking mode (bypassing the BSCU).'
        ),
        'insufficient deceleration may be provided upon landing',
        Definition.get('H-4.1'),
    ),
    ScenarioType2(
        'Scenario 7',
        (
            'The BSCU sends Brake command, but the brakes are not applied due'
            ' to insufficient hydraulic pressure (pump failure, hydraulic'
            ' leak, etc.).'
        ),
        'insufficient deceleration may be provided upon landing',
        Definition.get('H-4.1'),
    ),
    ScenarioType2(
        'Scenario 8',
        (
            'The BSCU sends Brake command, the brakes are applied, but the'
            ' aircraft does not decelerate due to a wet runway (wheels'
            ' hydroplane).'
        ),
        'insufficient deceleration may be provided upon landing',
        Definition.get('H-4.1'),
    ),
    ScenarioType2(
        'Scenario 9',
        (
            'The BSCU sends Brake command, but the brakes are not applied'
            ' because an adversary injected a command that put the wheel'
            ' braking system into alternate braking mode.'
        ),
        'insufficient deceleration may be provided upon landing',
        Definition.get('H-4.1'),
    ),
)
