from stpa import Loss, Hazard, Definition

losses = (
    Loss('L-1', 'Loss of life or serious injury to people'),
    Loss('L-2', 'Damage to the aircraft or objects outside the aircraft'),
)

hazards = (
    Hazard(
        'H-1',
        'Aircraft',
        'violate minimum separation standards in flight',
        Definition.get_all('L-1', 'L-2'),
    ),
    Hazard(
        'H-2',
        '',  
        'Controlled flight of aircraft into terrain',
        Definition.get_all('L-1', 'L-2'),
    ),
    Hazard(
        'H-3',
        '',  
        'Loss of aircraft control',
        Definition.get_all('L-1', 'L-2'),
    ),
    Hazard(
        'H-4',
        'Aircraft',
        'airframe integrity is lost',
        Definition.get_all('L-1', 'L-2'),
    ),
    Hazard(
        'H-5',
        'Aircraft',
        'environment is harmful to human health',
        Definition.get_all('L-1', 'L-2'),
    ),
    Hazard(
        'H-6',
        'Aircraft',
        'departs designated taxiway, runway, or apron on ground',
        Definition.get_all('L-1', 'L-2'),
    ),
    Hazard(
        'H-7',
        'Aircraft',
        'comes too close to other objects on the ground',
        Definition.get_all('L-1', 'L-2'),
    ),
)

def format_hazard(hazard):
    system = f"{hazard.system} " if hazard.system else ""
    losses = ', '.join(loss.name for loss in hazard.losses)
    return f"{hazard.name}: {system}{hazard.unsafe_condition} [{losses}]"


if __name__ == "__main__":
    print('Losses\n------')
    for loss in losses:
        print(loss)

    print('\nHazards\n-------')
    for hazard in hazards:
        print(format_hazard(hazard))
