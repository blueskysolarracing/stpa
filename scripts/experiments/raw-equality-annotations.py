from concurrent.futures import ThreadPoolExecutor
from functools import partial
from itertools import combinations
from json import load
from pathlib import Path
from random import seed, shuffle
from sys import argv

from dotenv import load_dotenv
from openai import OpenAI
from tqdm import tqdm
import pandas as pd

from stpa import query_raw_equality

MODEL = argv[1]
SEED = int(argv[2])
TEMPERATURE = float(argv[3])
RAW_SYNTHESES_PATH = Path(argv[4])
RAW_UNSAFE_CONTROL_ACTION_RAW_EQUALITY_ANNOTATIONS_PATH = Path(argv[5])
RAW_SCENARIO_RAW_EQUALITY_ANNOTATIONS_PATH = Path(argv[6])


def query(client, definitions):
    return query_raw_equality(
        client,
        MODEL,
        *definitions,
        seed=SEED,
        temperature=TEMPERATURE,
    )


def main():
    load_dotenv()

    client = OpenAI()

    seed(SEED)

    with open(RAW_SYNTHESES_PATH) as file:
        raw_syntheses = load(file)

    raw_unsafe_control_actions = raw_syntheses['unsafe-control-actions']
    raw_scenarios = raw_syntheses['scenarios']

    raw_unsafe_control_action_pairs = list(
        combinations(raw_unsafe_control_actions, 2),
    )
    raw_scenario_pairs = list(combinations(raw_scenarios, 2))

    shuffle(raw_unsafe_control_action_pairs)
    shuffle(raw_scenario_pairs)

    df = pd.DataFrame()
    unsafe_control_action_0, unsafe_control_action_1 = zip(
        *raw_unsafe_control_action_pairs,
    )
    df['unsafe_control_action_0'] = unsafe_control_action_0
    df['unsafe_control_action_1'] = unsafe_control_action_1

    with ThreadPoolExecutor() as executor:
        df['equality'] = tuple(
            tqdm(
                executor.map(
                    partial(query, client),
                    raw_unsafe_control_action_pairs,
                ),
                total=len(raw_unsafe_control_action_pairs),
            ),
        )

    df.to_csv(RAW_UNSAFE_CONTROL_ACTION_RAW_EQUALITY_ANNOTATIONS_PATH)

    df = pd.DataFrame()
    scenario_0, scenario_1 = zip(*raw_scenario_pairs)
    df['scenario_0'] = scenario_0
    df['scenario_1'] = scenario_1

    with ThreadPoolExecutor() as executor:
        df['equality'] = tuple(
            tqdm(
                executor.map(partial(query, client), raw_scenario_pairs),
                total=len(raw_scenario_pairs),
            ),
        )

    df.to_csv(RAW_SCENARIO_RAW_EQUALITY_ANNOTATIONS_PATH)


if __name__ == '__main__':
    main()
