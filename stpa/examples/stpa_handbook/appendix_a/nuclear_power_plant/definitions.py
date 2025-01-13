# type: ignore

from stpa.definitions import Definition, Hazard, Loss

LOSSES = (
    Loss('L1', 'People injured or killed'),
    Loss('L2', 'Environment contaminated'),
    Loss('L3', 'Equipment damage (economic loss)'),
    Loss('L4', 'Loss of electrical power generation'),
)

HAZARDS = (
    Hazard(
        'H1',
        '',
        'Release of radioactive materials',
        Definition.get_all('L1', 'L2', 'L3', 'L4'),
    ),
    Hazard(
        'H2',
        'Reactor',
        'temperature too high',
        Definition.get_all('L1', 'L2', 'L3', 'L4'),
    ),
    Hazard(
        'H3',
        'Equipment',
        'operated beyond limits',
        Definition.get_all('L3', 'L4'),
    ),
    Hazard('H4', 'Reactor', 'shut down', Definition.get_all('L4')),
)
