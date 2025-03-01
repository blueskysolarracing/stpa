from sys import argv

from dotenv import load_dotenv
from openai import OpenAI

from stpa import (
    flatten,
    generate_filtered_raw_scenarios,
    Hazard,
    import_string,
    Loss,
    Scenario,
    SubHazard,
    UnsafeControlAction,
)

MODEL = argv[1]
AUXILIARY_MODEL = argv[2]
SEED = int(argv[3])
TEMPERATURE = float(argv[4])
COUNT = int(argv[5])
DIAGRAM_PATHNAME = argv[6]
DEFINITIONS = tuple(flatten(map(import_string, argv[7:])))
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

    for raw_unsafe_control_action in (
            generate_filtered_raw_scenarios(
                client,
                MODEL,
                AUXILIARY_MODEL,
                COUNT,
                LOSSES,
                HAZARDS,
                UNSAFE_CONTROL_ACTIONS,
                SCENARIOS,
                DIAGRAM_PATHNAME,
                SEED,
                TEMPERATURE,
            )
    ):
        print(raw_unsafe_control_action, flush=True)


if __name__ == '__main__':
    main()
