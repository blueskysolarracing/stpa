# type: ignore

from stpa import Definition, Hazard, UnsafeControlAction

HAZARDS = (Hazard('H-1', '', '', []),)

UNSAFE_CONTROL_ACTIONS = (
    UnsafeControlAction(
        'UCA-HTV-1',
        'ISS crew',
        'does not provide',
        'Abort Cmd',
        'when emergency condition exists',
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-HTV-2',
        'ISS crew',
        'provides',
        'Abort Cmd',
        'when HTV is captured',
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-HTV-3',
        'ISS crew',
        'provides',
        'Abort Cmd',
        'when ISS is in Abort path',
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-HTV-4',
        'ISS crew',
        'provides {} too late',
        'Abort Cmd',
        'to avoid collision',
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-HTV-5',
        'ISS crew',
        'provides {} too early',
        'Abort Cmd',
        'before capture is released',
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-HTV-6',
        'ISS crew',
        'does not provide',
        'Free Drift Cmd',
        'when HTV is stopped in capture box',
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-HTV-7',
        'ISS crew',
        'provides',
        'Free Drift Cmd',
        'when HTV is approaching ISS',
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-HTV-8',
        'ISS crew',
        'provides {} too late, more than X minutes',
        'Free Drift Cmd',
        'after HTV stops',
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-HTV-9',
        'ISS crew',
        'provides {} too early',
        'Free Drift Cmd',
        'before HTV stops',
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-HTV-10',
        'ISS crew',
        'does not perform',
        'Capture',
        'when HTV is in capture box in free drift',
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-HTV-11',
        'ISS crew',
        'performs',
        'Capture',
        'when HTV is not in free drift',
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-HTV-12',
        'ISS crew',
        'performs',
        'Capture',
        'when HTV is aborting',
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-HTV-13',
        'ISS crew',
        'performs',
        'Capture',
        (
            'with excessive/insufficient movement (can impact HTV, cause'
            ' collision course)'
        ),
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-HTV-14',
        'ISS crew',
        'performs {} too late, more than X minutes',
        'Capture',
        'after HTV deactivated',
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-HTV-15',
        'ISS crew',
        'performs {} too early',
        'Capture',
        'before HTV deactivated',
        Definition.get_all('H-1'),
    ),
    UnsafeControlAction(
        'UCA-HTV-16',
        'ISS crew',
        'continues performing {} too long',
        'Capture',
        'after emergency condition exists',
        Definition.get_all('H-1'),
    ),
)
