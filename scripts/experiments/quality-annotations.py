from itertools import repeat
from json import load
from pathlib import Path
from random import seed, shuffle
from sys import argv

from dotenv import load_dotenv
from openai import OpenAI
from tqdm import tqdm
import pandas as pd

from stpa import (
    classify_raw_scenario_quality,
    classify_raw_unsafe_control_action_quality,
    flatten,
    import_string,
    QualityResponse,
    Scenario,
    UnsafeControlAction,
)

MODEL = argv[1]
SEED = int(argv[2])
TEMPERATURE = float(argv[3])
DIAGRAM_PATHNAME = argv[4]
RAW_SYNTHESES_PATH = Path(argv[5])
FILTERED_RAW_UNSAFE_CONTROL_ACTIONS_PATH = Path(argv[6])
FILTERED_RAW_SCENARIOS_PATH = Path(argv[7])
RAW_UNSAFE_CONTROL_ACTION_QUALITY_ANNOTATIONS_PATH = Path(argv[8])
RAW_SCENARIO_QUALITY_ANNOTATIONS_PATH = Path(argv[9])
DEFINITIONS = tuple(flatten(map(import_string, argv[10:])))
UNSAFE_CONTROL_ACTIONS = tuple(
    filter(UnsafeControlAction.__instancecheck__, DEFINITIONS),
)
SCENARIOS = tuple(filter(Scenario.__instancecheck__, DEFINITIONS))


def main():
    load_dotenv()

    client = OpenAI()

    seed(SEED)

    with open(RAW_SYNTHESES_PATH) as file:
        raw_syntheses = load(file)

    raw_unsafe_control_actions = raw_syntheses['unsafe-control-actions']
    raw_scenarios = raw_syntheses['scenarios']

    for i, raw_unsafe_control_action in enumerate(
            tqdm(raw_unsafe_control_actions),
    ):
        raw_unsafe_control_actions[i] = (
            raw_unsafe_control_action,
            classify_raw_unsafe_control_action_quality(
                client,
                MODEL,
                UNSAFE_CONTROL_ACTIONS,
                raw_unsafe_control_action,
                SEED,
                TEMPERATURE,
            ),
        )

    for i, raw_scenario in enumerate(tqdm(raw_scenarios)):
        raw_scenarios[i] = (
            raw_scenario,
            classify_raw_scenario_quality(
                client,
                MODEL,
                SCENARIOS,
                raw_scenario,
                SEED,
                TEMPERATURE,
            ),
        )

    with open(FILTERED_RAW_UNSAFE_CONTROL_ACTIONS_PATH) as file:
        lines = map(str.strip, file.readlines())

        raw_unsafe_control_actions.extend(
            zip(lines, repeat(QualityResponse.CORRECT_AND_USEFUL)),
        )

    with open(FILTERED_RAW_SCENARIOS_PATH) as file:
        lines = map(str.strip, file.readlines())

        raw_scenarios.extend(
            zip(lines, repeat(QualityResponse.CORRECT_AND_USEFUL)),
        )

    shuffle(raw_unsafe_control_actions)
    shuffle(raw_scenarios)

    df = pd.DataFrame()
    unsafe_control_action, quality = zip(*raw_unsafe_control_actions)
    df['unsafe_control_action'] = unsafe_control_action
    df['quality'] = quality

    df.to_csv(RAW_UNSAFE_CONTROL_ACTION_QUALITY_ANNOTATIONS_PATH)

    df = pd.DataFrame()
    scenario, quality = zip(*raw_scenarios)
    df['scenario'] = scenario
    df['quality'] = quality

    df.to_csv(RAW_SCENARIO_QUALITY_ANNOTATIONS_PATH)


if __name__ == '__main__':
    main()
