# type: ignore

from stpa.definitions import Definition, Hazard, Loss

LOSSES = (
    Loss(
        'L-1', 'Two or more vehicles collide.'
    ),
    Loss(
        'L-2', 'Vehicle collides with a non-fixed (mobile) obstacle.'
    ),
    Loss(
        'L-3', 'Vehicle crashes into terrain (fixed obstacle).'
    ),
    Loss(
        'L-4', 'Vehicle occupants injured without a vehicle collision.'
    ),
)

HAZARDS = (
    Hazard(
        'H-1',
        'Vehicle',
        'Does not maintain safe distance from nearby vehicles.',
        Definition.get_all('L-1'),
    ),
    Hazard(
        'H-2',
        'Vehicle',
        'Does not maintain safe distance from terrain and other obstacles.',
        Definition.get_all('L-2', 'L-3'),
    ),
    Hazard(
        'H-3',
        'Vehicle',
        'Enters an uncontrollable/unrecoverable state.',
        Definition.get_all('L-1', 'L-2', 'L-3', 'L-4'),
    ),
    Hazard(
        'H-4',
        'Vehicle',
        'Occupants exposed to harmful effects and/or health hazards.',
        Definition.get_all('L-4'),
    ),
)
