from stpa import Loss, Hazard, Definition

losses = (
    Loss('M-1', 'Loss of or damage to the aircraft or equipment on the aircraft'),
    Loss('M-2', 'Serious injury or fatality to personnel'),
    Loss('M-3', 'Inability to complete the mission'),
)

hazards = (
    Hazard(
        'H-1',
        'Military Aviation',
        'Violation of minimum separation standards from fixed or moving objects',
        Definition.get_all('M-1', 'M-2', 'M-3'),
    ),
    Hazard(
        'H-2',
        'Military Aviation',
        'Inability to control the aircraft',
        Definition.get_all('M-1', 'M-2', 'M-3'),
    ),
    Hazard(
        'H-3',
        'Military Aviation',
        'Loss of airframe integrity',
        Definition.get_all('M-1', 'M-2', 'M-3'),
    ),
    Hazard(
        'H-4',
        'Weapon System',
        'Uncommanded detonation',
        Definition.get_all('M-1', 'M-2', 'M-3'),
    ),
    Hazard(
        'H-5',
        'Weapon System',
        'Uncommanded launch',
        Definition.get_all('M-1', 'M-2', 'M-3'),
    ),
    Hazard(
        'H-6',
        'Weapon System',
        'Collateral damage or friendly fire',
        Definition.get_all('M-1', 'M-2', 'M-3'),
    ),
    Hazard(
        'H-7',
        'Weapon System',
        'Non-deployment (detonation and/or launch) of ordinance when commanded',
        Definition.get_all('M-3'),
    ),
)

if __name__ == "__main__":
    print("Mishaps\n-------")
    for loss in losses:
        print(loss)

    print("\nHazards\n-------")
    for hazard in hazards:
        print(hazard)
