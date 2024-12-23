from stpa import *

losses = (
    Loss('Loss of life or injury to people'),
    Loss('Loss of or damage to vehicle'),
    Loss('Loss of or damage to objects outside the vehicle'),
    Loss(
        (
            'Loss of mission (e.g. transportation mission, surveillance'
            ' mission, scientific mission, defense mission, etc.)'
        ),
    ),
    Loss('Loss of customer satisfaction'),
    Loss('Loss of sensitive information'),
    Loss('Environmental loss'),
    Loss('Loss of power generation'),
)

hazards = (
    Hazard(
        'Aircraft',
        'violate minimum separation standards in flight',
        Definition.get_all('L-1', 'L-2', 'L-4', 'L-5'),
    ),
    Hazard(
        'Aircraft',
        'airframe integrity is lost',
        Definition.get_all('L-1', 'L-2', 'L-4', 'L-5'),
    ),
    Hazard(
        'Aircraft',
        'leaves designated taxiway, runway, or apron on ground',
        Definition.get_all('L-1', 'L-2', 'L-5'),
    ),
    Hazard(
        'Aircraft',
        'comes too close to other objects on the ground',
        Definition.get_all('L-1', 'L-2', 'L-5'),
    ),
    Hazard(
        'Satellite',
        'is unable to collect scientific data',
        Definition.get_all('L-4'),
    ),
    Hazard(
        'Vehicle',
        'does not maintain safe distance from terrain and other obstacles',
        Definition.get_all('L-1', 'L-2', 'L-3', 'L-4'),
    ),
    Hazard(
        'UAV',
        'does not complete surveillance mission',
        Definition.get_all('L-4'),
    ),
    Hazard(
        'Nuclear power plant',
        'releases dangerous materials',
        Definition.get_all('L-1', 'L-4', 'L-7', 'L-8'),
    ),
)

system_level_constraints = (
    SystemLevelConstraintType1(
        'Aircraft',
        'must satisfy minimum separation standards from other aircraft and objects',
        Definition.get_all('H-1'),
    ),
    SystemLevelConstraintType1(
        'Aircraft',
        'airframe integrity must be maintained under worst-case conditions',
        Definition.get_all('H-2'),
    ),
    SystemLevelConstraintType2(
        Definition.get('H-1'),
        (
            'the violation must be detected and measures taken to prevent'
            ' collision'
        ),
        Definition.get_all('H-1'),
    ),
)

sub_hazards = {
    'H-4': (
        # Deceleration
        SubHazard(
            Definition.get('H-4'),
            (
                'Deceleration is insufficient upon landing, rejected takeoff,'
                ' or during taxiing'
            ),
        ),
        SubHazard(
            Definition.get('H-4'),
            'Asymmetric deceleration maneuvers aircraft toward other objects',
        ),
        SubHazard(
            Definition.get('H-4'),
            'Deceleration occurs after V1 point during takeoff',
        ),
        # Acceleration
        SubHazard(
            Definition.get('H-4'),
            'Excessive acceleration provided while taxiing',
        ),
        SubHazard(
            Definition.get('H-4'),
            'Asymmetric acceleration maneuvers aircraft toward other objects',
        ),
        SubHazard(
            Definition.get('H-4'),
            'Acceleration is insufficient during takeoff',
        ),
        SubHazard(
            Definition.get('H-4'),
            'Acceleration is provided during landing or when parked',
        ),
        SubHazard(
            Definition.get('H-4'),
            'Acceleration continues to be applied during rejected takeoff',
        ),
        # Steering
        SubHazard(
            Definition.get('H-4'),
            'Insufficient steering to turn along taxiway, runway, or apron path',
        ),
        SubHazard(
            Definition.get('H-4'),
            'Steering maneuvers aircraft off the taxiway, runway, or apron path',
        ),
    )
}

print('Losses\n------\n')

for loss in losses:
    print(loss)

print('\nHazards\n-------\n')

for hazard in hazards:
    print(hazard)

print('\nSystem Level Constraints\n------------------------\n')

for system_level_constraint in system_level_constraints:
    print(system_level_constraint)

print('\nSub hazards\n------------------------\n')

for key, value in sub_hazards.items():
    print(Definition.get(key))

    for sub_hazard in value:
        print('\t', end='')
        print(sub_hazard)
