# type: ignore

from stpa.definitions import Definition, Hazard, Loss, SubHazard

LOSSES = (
    Loss(
        'L1',
        (
            'The patient is injured or killed from overexposure or'
            ' undertreatment.'
        ),
    ),
    Loss('L2', 'A nonpatient is injured or killed by radiation.'),
    Loss('L3', 'Damage or loss of equipment.'),
    Loss('L4', 'Physical injury to a patient or nonpatient during treatment.'),
)

HAZARDS = (
    Hazard(
        'H1',
        'Dose delivered to patient',
        (
            'Wrong dose: {} is wrong in either amount,'
            ' location, or timing'
        ),
        Definition.get_all('L1'),
    ),
    Hazard(
        'H2',
        'A nonpatient',
        'is unnecessarily exposed to radiation',
        Definition.get_all('L2'),
    ),
    Hazard(
        'H3',
        'Equipment',
        'is subject to unnecessary stress',
        Definition.get_all('L3'),
    ),
    Hazard(
        'H4',
        'Persons',
        'are subjected to nonradiological injury',
        Definition.get_all('L4'),
    ),
)

SUB_HAZARDS = {
    'H1': (
        SubHazard(
            'H1a',
            Definition.get('H1'),
            'Right patient, right dose, wrong location.',
        ),
        SubHazard(
            'H1b',
            Definition.get('H1'),
            'Right patient, wrong dose, right location.',
        ),
        SubHazard(
            'H1c',
            Definition.get('H1'),
            'Right patient, wrong dose, wrong location.',
        ),
        SubHazard('H1d', Definition.get('H1'), 'Wrong patient.'),
    ),
}
