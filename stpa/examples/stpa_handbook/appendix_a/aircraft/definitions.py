# type: ignore

from stpa.definitions import Definition, Hazard, Loss

LOSSES = (
    Loss('L1', 'Loss of life or serious injury to people'),
    Loss('L2', 'Damage to the aircraft or objects outside the aircraft'),
)

HAZARDS = (
    Hazard(
        'H-1',
        'Aircraft',
        'violate minimum separation standards in flight',
        Definition.get_all('L1', 'L2'),
    ),
    Hazard(
        'H-2',
        'aircraft',
        'Controlled flight of {} into terrain',
        Definition.get_all('L1', 'L2'),
    ),
    Hazard(
        'H-3',
        'aircraft',
        'Loss of {} control',
        Definition.get_all('L1', 'L2'),
    ),
    Hazard(
        'H-4',
        'Aircraft',
        'airframe integrity is lost',
        Definition.get_all('L1', 'L2'),
    ),
    Hazard(
        'H-5',
        'Aircraft',
        'environment is harmful to human health',
        Definition.get_all('L1', 'L2'),
    ),
    Hazard(
        'H-6',
        'Aircraft',
        'departs designated taxiway, runway, or apron on ground',
        Definition.get_all('L1', 'L2'),
    ),
    Hazard(
        'H-7',
        'Aircraft',
        'comes too close to other objects on the ground',
        Definition.get_all('L1', 'L2'),
    ),
)
