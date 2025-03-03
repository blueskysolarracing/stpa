from collections import Counter
from json import load
from pathlib import Path
from pprint import pformat
from sys import argv

import pandas as pd

RAW_SYNTHESES_PATH = Path(argv[1])
FILTERED_RAW_UNSAFE_CONTROL_ACTIONS_PATH = Path(argv[2])
FILTERED_RAW_SCENARIOS_PATH = Path(argv[3])
HUMAN_ANNOTATION_PATHS = tuple(map(Path, argv[4:]))


def main():
    with open(RAW_SYNTHESES_PATH) as file:
        raw_syntheses = load(file)

    raw_unsafe_control_actions = raw_syntheses['unsafe-control-actions']
    raw_scenarios = raw_syntheses['scenarios']

    with open(FILTERED_RAW_UNSAFE_CONTROL_ACTIONS_PATH) as file:
        filtered_raw_unsafe_control_actions = tuple(
            map(str.strip, file.readlines()),
        )

    with open(FILTERED_RAW_SCENARIOS_PATH) as file:
        filtered_raw_scenarios = tuple(map(str.strip, file.readlines()))

    dfs = tuple(map(pd.read_csv, HUMAN_ANNOTATION_PATHS))
    qualities = {}

    for df in dfs:
        try:
            qualities.update(zip(df['unsafe_control_action'], df['quality']))
        except KeyError:
            qualities.update(zip(df['scenario'], df['quality']))

    data = {
        'raw-unsafe-control-actions': dict(
            Counter(map(qualities.get, raw_unsafe_control_actions)),
        ),
        'raw-scenarios': dict(Counter(map(qualities.get, raw_scenarios))),
        'filtered-raw-unsafe-control-actions': dict(
            Counter(map(qualities.get, filtered_raw_unsafe_control_actions)),
        ),
        'filtered-raw-scenarios': dict(
            Counter(map(qualities.get, filtered_raw_scenarios)),
        ),
    }

    print(pformat(data).replace('\'', '"').replace(': nan}', ': null}'))


if __name__ == '__main__':
    main()
