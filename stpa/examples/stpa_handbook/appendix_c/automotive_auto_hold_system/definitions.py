# type: ignore

from stpa import Definition, Hazard, UnsafeControlAction

HAZARDS = Hazard('H-1', '', '', []), Hazard('H-2', '', '', [])

UNSAFE_CONTROL_ACTIONS = (
    # Hold Command
    UnsafeControlAction(
        'UCA-AH-1',
        'AH',
        'does not provide',
        'HOLD',
        'when vehicle stops and brake pedal released',
        Definition.get_all('H-1', 'H-2'),
    ),
    UnsafeControlAction(
        'UCA-AH-2',
        'AH',
        'provides',
        'HOLD',
        'when driver is applying the accelerator',
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-AH-3',
        'AH',
        'provides',
        'HOLD',
        'when AH is DISABLED',
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-AH-4',
        'AH',
        'provides',
        'HOLD',
        'when vehicle is moving',
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-AH-5',
        'AH',
        'provides',
        'HOLD',
        'when driver is not applying brake',
        Definition.get_all('H-1', 'H-2'),
    ),
    UnsafeControlAction(
        'UCA-AH-6',
        'AH',
        'provides {} too early',
        'HOLD',
        'before the required time at rest has not been met',
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-AH-7',
        'AH',
        'provides {} too late',
        'HOLD',
        'after vehicle stops, begins to roll',
        Definition.get_all('H-1'),
    ),
    # Release Command
    UnsafeControlAction(
        'UCA-AH-10',
        'AH',
        'does not provide',
        'RELEASE',
        'when driver applies accelerator pedal',
        Definition.get_all('H-1', 'H-2'),
    ),
    UnsafeControlAction(
        'UCA-AH-12',
        'AH',
        'provides',
        'RELEASE',
        'when driver is not applying accelerator',
        Definition.get_all('H-1', 'H-2'),
    ),
    UnsafeControlAction(
        'UCA-AH-13',
        'AH',
        'provides {} too early',
        'RELEASE',
        'before there is sufficient wheel torque',
        Definition.get_all('H-1', 'H-2'),
    ),
    UnsafeControlAction(
        'UCA-AH-13',
        'AH',
        'provides {} too late',
        'RELEASE',
        'after accelerator applied, engine torque exceeds wheel torque',
        Definition.get_all('H-1', 'H-2'),
    ),
    # Additional Pressure Command
    UnsafeControlAction(
        'UCA-AH-14',
        'AH',
        'does not provide',
        'ADDITIONALPRESSURE',
        'when vehicle is slipping and AH is active',
        Definition.get_all('H-1', 'H-2'),
    ),
    UnsafeControlAction(
        'UCA-AH-15',
        'AH',
        'provides',
        'ADDITIONALPRESSURE',
        'when AH is not active',
        Definition.get_all('H-1', 'H-2'),
    ),
    UnsafeControlAction(
        'UCA-AH-16',
        'AH',
        'provides',
        'ADDITIONALPRESSURE',
        'when brake system specs are exceeded',
        Definition.get_all('H-1', 'H-2'),
    ),
    UnsafeControlAction(
        'UCA-AH-16',
        'AH',
        'provides {} too late',
        'ADDITIONAL-PRESSURE',
        'after vehicle is slipping',
        Definition.get_all('H-1', 'H-2'),
    ),
)
