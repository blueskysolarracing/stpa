from json import dump
from sys import argv, stdout

from dotenv import load_dotenv
from openai import OpenAI

from stpa import (
    flatten,
    generate_raw_scenarios,
    generate_raw_unsafe_control_actions,
    Hazard,
    import_string,
    Loss,
    Scenario,
    SubHazard,
    UnsafeControlAction,
)

MODEL = argv[1]
SEED = int(argv[2])
TEMPERATURE = float(argv[3])
COUNT = int(argv[4])
DIAGRAM_PATHNAME = argv[5]
DEFINITIONS = tuple(flatten(map(import_string, argv[6:])))
LOSSES = tuple(filter(Loss.__instancecheck__, DEFINITIONS))
HAZARDS = tuple(filter(Hazard.__instancecheck__, DEFINITIONS))
SUB_HAZARDS = tuple(
    filter(SubHazard.__instancecheck__, DEFINITIONS),
)
UNSAFE_CONTROL_ACTIONS = tuple(
    filter(UnsafeControlAction.__instancecheck__, DEFINITIONS),
)
SCENARIOS = tuple(filter(Scenario.__instancecheck__, DEFINITIONS))


def main():
    load_dotenv()

    client = OpenAI()
    raw_unsafe_control_actions = generate_raw_unsafe_control_actions(
        client,
        MODEL,
        COUNT,
        LOSSES,
        HAZARDS,
        UNSAFE_CONTROL_ACTIONS,
        DIAGRAM_PATHNAME,
        SEED,
        TEMPERATURE,
    )
    raw_scenarios = generate_raw_scenarios(
        client,
        MODEL,
        COUNT,
        LOSSES,
        HAZARDS,
        UNSAFE_CONTROL_ACTIONS,
        SCENARIOS,
        DIAGRAM_PATHNAME,
        SEED,
        TEMPERATURE,
    )
    data = {
        'unsafe-control-actions': raw_unsafe_control_actions,
        'scenarios': raw_scenarios,
    }

    dump(data, stdout)


if __name__ == '__main__':
    main()
