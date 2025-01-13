# type: ignore

from stpa.definitions import Definition, Hazard, Loss

LOSSES = (
    Loss('L1', 'Loss of life or serious injury to people'),
    Loss('L2', 'Damage to the vehicle or objects outside the vehicle'),
)

HAZARDS = (
    Hazard(
        'H1',
        'Vehicle',
        'does not maintain safe distance from nearby objects',
        Definition.get_all('L1', 'L2'),
    ),
    Hazard(
        'H2',
        'Vehicle',
        'enters dangerous area/region',
        Definition.get_all('L1', 'L2'),
    ),
    Hazard(
        'H3',
        'Vehicle',
        (
            'exceeds safe operating envelope for environment (speed,'
            ' lateral/longitudinal forces)'
        ),
        Definition.get_all('L1', 'L2'),
    ),
    Hazard(
        'H4',
        'Vehicle occupants',
        (
            'exposed to harmful effects and/or health hazards (e.g. fire,'
            ' excessive temperature, inability to escape, door closes on'
            ' passengers, etc.)'
        ),
        Definition.get_all('L1', 'L2'),
    ),
)
