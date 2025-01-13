from stpa import Loss, Hazard, SubHazard, Definition

losses = (
    Loss('L-1', 'The patient is injured or killed from overexposure or undertreatment.'),
    Loss('L-2', 'A nonpatient is injured or killed by radiation.'),
    Loss('L-3', 'Damage or loss of equipment.'),
    Loss('L-4', 'Physical injury to a patient or nonpatient during treatment.'),
)

hazards = (
    Hazard(
        'H-1',
        'Radiation Therapy',
        'Wrong dose: Dose delivered to patient is wrong in either amount, location, or timing',
        Definition.get_all('L-1'),
    ),
    Hazard(
        'H-2',
        'Radiation Therapy',
        'A nonpatient is unnecessarily exposed to radiation',
        Definition.get_all('L-2'),
    ),
    Hazard(
        'H-3',
        'Radiation Therapy',
        'Equipment is subject to unnecessary stress',
        Definition.get_all('L-3'),
    ),
    Hazard(
        'H-4',
        'Radiation Therapy',
        'Persons are subjected to nonradiological injury',
        Definition.get_all('L-4'),
    ),
)

sub_hazards = {
    'H-1': (
        SubHazard(
            'H-1a',
            Definition.get('H-1'),
            'Right patient, right dose, wrong location.',
        ),
        SubHazard(
            'H-1b',
            Definition.get('H-1'),
            'Right patient, wrong dose, right location.',
        ),
        SubHazard(
            'H-1c',
            Definition.get('H-1'),
            'Right patient, wrong dose, wrong location.',
        ),
        SubHazard(
            'H-1d',
            Definition.get('H-1'),
            'Wrong patient.',
        ),
    ),
}

if __name__ == "__main__":
    print('Losses\n------')
    for loss in losses:
        print(loss)

    print('\nHazards\n-------')
    for hazard in hazards:
        print(hazard)

    print('\nSub-Hazards for H-1\n-------------------')
    for sub_hazard in sub_hazards['H-1']:
        print(sub_hazard)
