from stpa import Loss, Hazard, Definition

losses = (
    Loss('L-1', 'Loss of life or serious injury to people'),
    Loss('L-2', 'Damage to the vehicle or objects outside the vehicle'),
)

hazards = (
    Hazard(
        'H-1',
        'Automotive',
        'Vehicle does not maintain safe distance from nearby objects',
        Definition.get_all('L-1', 'L-2'),
    ),
    Hazard(
        'H-2',
        'Automotive',
        'Vehicle enters dangerous area/region',
        Definition.get_all('L-1', 'L-2'),
    ),
    Hazard(
        'H-3',
        'Automotive',
        'Vehicle exceeds safe operating envelope for environment (speed, lateral/longitudinal forces)',
        Definition.get_all('L-1', 'L-2'),
    ),
    Hazard(
        'H-4',
        'Automotive',
        'Vehicle occupants exposed to harmful effects and/or health hazards (e.g. fire, excessive temperature, inability to escape, door closes on passengers, etc.)',
        Definition.get_all('L-1', 'L-2'),
    ),
)

if __name__ == "__main__":
    print("Losses\n------")
    for loss in losses:
        print(loss)

    print("\nHazards\n-------")
    for hazard in hazards:
        print(hazard)
