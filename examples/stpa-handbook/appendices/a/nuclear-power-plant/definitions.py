from stpa import Loss, Hazard, Definition

losses = (
    Loss('L-1', 'People injured or killed'),
    Loss('L-2', 'Environment contaminated'),
    Loss('L-3', 'Equipment damage (economic loss)'),
    Loss('L-4', 'Loss of electrical power generation'),
)

hazards = (
    Hazard(
        'H-1',
        'Nuclear Power Plant',
        'Release of radioactive materials',
        Definition.get_all('L-1', 'L-2', 'L-3', 'L-4'),
    ),
    Hazard(
        'H-2',
        'Nuclear Power Plant',
        'Reactor temperature too high',
        Definition.get_all('L-1', 'L-2', 'L-3', 'L-4'),
    ),
    Hazard(
        'H-3',
        'Nuclear Power Plant',
        'Equipment operated beyond limits',
        Definition.get_all('L-3', 'L-4'),
    ),
    Hazard(
        'H-4',
        'Nuclear Power Plant',
        'Reactor shut down',
        Definition.get_all('L-4'),
    ),
)

if __name__ == "__main__":
    print('Losses\n------')
    for loss in losses:
        print(loss)

    print('\nHazards\n-------')
    for hazard in hazards:
        print(hazard)
