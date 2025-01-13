# type: ignore

from stpa.definitions import Definition, Hazard, Loss

LOSSES = (
    Loss(
        'M-1',
        'Loss of or damage to the aircraft or equipment on the aircraft',
    ),
    Loss('M-2', 'Serious injury or fatality to personnel'),
    Loss('M-3', 'Inability to complete the mission'),
)

HAZARDS = (
    Hazard(
        'H-1',
        'minimum separation standards',
        'Violation of {} from fixed or moving objects',
        Definition.get_all('M-1', 'M-2', 'M-3'),
    ),
    Hazard(
        'H-2',
        'aircraft',
        'Inability to control the {}',
        Definition.get_all('M-1', 'M-2', 'M-3'),
    ),
    Hazard(
        'H-3',
        'airframe',
        'Loss of {} integrity',
        Definition.get_all('M-1', 'M-2', 'M-3'),
    ),
    Hazard(
        'H-4',
        '',
        'Uncommanded detonation',
        Definition.get_all('M-1', 'M-2', 'M-3'),
    ),
    Hazard(
        'H-5',
        '',
        'Uncommanded launch',
        Definition.get_all('M-1', 'M-2', 'M-3'),
    ),
    Hazard(
        'H-6',
        '',
        'Collateral damage or friendly fire',
        Definition.get_all('M-1', 'M-2', 'M-3'),
    ),
    Hazard(
        'H-7',
        'ordinance',
        'Non-deployment (detonation and/or launch) of {} when commanded',
        Definition.get_all('M-3'),
    ),
)
