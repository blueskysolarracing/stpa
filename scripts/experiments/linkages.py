from collections.abc import Container
from concurrent.futures import ThreadPoolExecutor
from itertools import product
from pprint import pformat
from sys import argv

from dotenv import load_dotenv
from openai import OpenAI
from tqdm import tqdm
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    recall_score,
    precision_score,
    f1_score,
)

from stpa import (
    ControllerConstraint,
    flatten,
    Hazard,
    import_string,
    Loss,
    query_linkage,
    Responsibility,
    Scenario,
    ScenarioType1,
    ScenarioType2,
    SubHazard,
    SystemLevelConstraint,
    SystemLevelConstraintType1,
    SystemLevelConstraintType2,
    SystemLevelConstraintType3,
    UnsafeControlAction,
)

MODEL = argv[1]
SEED = int(argv[2])
TEMPERATURE = float(argv[3])
DEFINITIONS = tuple(flatten(map(import_string, argv[4:])))
LOSSES = tuple(filter(Loss.__instancecheck__, DEFINITIONS))
HAZARDS = tuple(filter(Hazard.__instancecheck__, DEFINITIONS))
SYSTEM_LEVEL_CONSTRAINTS = tuple(
    filter(SystemLevelConstraint.__instancecheck__, DEFINITIONS),
)
SYSTEM_LEVEL_CONSTRAINT_TYPE_1S = tuple(
    filter(SystemLevelConstraintType1.__instancecheck__, DEFINITIONS),
)
SYSTEM_LEVEL_CONSTRAINT_TYPE_2S = tuple(
    filter(SystemLevelConstraintType2.__instancecheck__, DEFINITIONS),
)
SYSTEM_LEVEL_CONSTRAINT_TYPE_3S = tuple(
    filter(SystemLevelConstraintType3.__instancecheck__, DEFINITIONS),
)
SUB_HAZARDS = tuple(
    filter(SubHazard.__instancecheck__, DEFINITIONS),
)
RESPONSIBILITIES = tuple(filter(Responsibility.__instancecheck__, DEFINITIONS))
UNSAFE_CONTROL_ACTIONS = tuple(
    filter(UnsafeControlAction.__instancecheck__, DEFINITIONS),
)
CONTROLLER_CONSTRAINTS = tuple(
    filter(ControllerConstraint.__instancecheck__, DEFINITIONS),
)
SCENARIOS = tuple(filter(Scenario.__instancecheck__, DEFINITIONS))
SCENARIO_TYPE_1S = tuple(filter(ScenarioType1.__instancecheck__, DEFINITIONS))
SCENARIO_TYPE_2S = tuple(filter(ScenarioType2.__instancecheck__, DEFINITIONS))


def main():
    load_dotenv()

    client = OpenAI()
    definitions = {
        'definition': len(DEFINITIONS),
        'loss': len(LOSSES),
        'hazard': len(HAZARDS),
        'system-level-constraint': len(SYSTEM_LEVEL_CONSTRAINTS),
        'system-level-constraint-type-1s': len(
            SYSTEM_LEVEL_CONSTRAINT_TYPE_1S,
        ),
        'system-level-constraint-type-2s': len(
            SYSTEM_LEVEL_CONSTRAINT_TYPE_2S,
        ),
        'system-level-constraint-type-3s': len(
            SYSTEM_LEVEL_CONSTRAINT_TYPE_3S,
        ),
        'sub-hazard': len(SUB_HAZARDS),
        'responsibility': len(RESPONSIBILITIES),
        'unsafe-control-action': len(UNSAFE_CONTROL_ACTIONS),
        'controller-constraint': len(CONTROLLER_CONSTRAINTS),
        'scenario': len(SCENARIOS),
        'scenario-type-1s': len(SCENARIO_TYPE_1S),
        'scenario-type-2s': len(SCENARIO_TYPE_2S),
    }
    arguments = []

    def add_arguments(definitions, true_links_name, links):
        for definition, link in tuple(product(definitions, links)):
            true_links = getattr(definition, true_links_name)

            if isinstance(true_links, Container):
                label = link in true_links
            else:
                label = link == true_links

            arguments.append((definition, link, label))

    add_arguments(HAZARDS, 'losses', LOSSES)
    add_arguments(SYSTEM_LEVEL_CONSTRAINT_TYPE_1S, 'hazards', HAZARDS)
    add_arguments(SYSTEM_LEVEL_CONSTRAINT_TYPE_2S, 'hazards', HAZARDS)
    add_arguments(SYSTEM_LEVEL_CONSTRAINT_TYPE_3S, 'sub_hazard', SUB_HAZARDS)
    add_arguments(
        RESPONSIBILITIES,
        'system_level_constraints',
        SYSTEM_LEVEL_CONSTRAINTS,
    )
    add_arguments(UNSAFE_CONTROL_ACTIONS, 'hazards', HAZARDS + SUB_HAZARDS)
    add_arguments(
        CONTROLLER_CONSTRAINTS,
        'unsafe_control_actions',
        UNSAFE_CONTROL_ACTIONS,
    )
    add_arguments(
        SCENARIO_TYPE_1S,
        'unsafe_control_action',
        UNSAFE_CONTROL_ACTIONS,
    )
    add_arguments(SCENARIO_TYPE_1S, 'hazard', HAZARDS)
    add_arguments(SCENARIO_TYPE_2S, 'hazard', HAZARDS)

    def add_y(definition_link_label):
        definition, link, label = definition_link_label
        prediction = query_linkage(
            client,
            MODEL,
            definition,
            link,
            SEED,
            TEMPERATURE,
        )

        return label, prediction

    with ThreadPoolExecutor() as executor:
        y_true, y_pred = zip(
            *tqdm(executor.map(add_y, arguments), total=len(arguments)),
        )

    data = {
        'definitions': definitions,
        'count': len(y_true),
        'confusion_matrix': confusion_matrix(y_true, y_pred).tolist(),
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred),
        'recall': recall_score(y_true, y_pred),
        'f1-score': f1_score(y_true, y_pred),
    }

    print(pformat(data).replace('\'', '"').replace(': nan}', ': null}'))


if __name__ == '__main__':
    main()
