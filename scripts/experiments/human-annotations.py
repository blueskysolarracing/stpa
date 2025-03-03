from pathlib import Path
from pprint import pformat
from sys import argv

from sklearn.metrics import (
    accuracy_score,
    cohen_kappa_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
import pandas as pd

PATHS = tuple(map(Path, argv[1:]))


def main():
    data = []

    for human_path, llm_path in zip(PATHS[::2], PATHS[1::2]):
        human_df = pd.read_csv(human_path)
        llm_df = pd.read_csv(llm_path)

        try:
            y_true = human_df['equality']
            y_pred = llm_df['equality']
        except KeyError:
            y_true = human_df['quality']
            y_pred = llm_df['quality']

        y_pred = y_pred[:len(y_true)]

        data.append(
            {
                'human_name': human_path.name,
                'llm_name': llm_path.name,
                'count': len(y_true),
                'accuracy': accuracy_score(y_true, y_pred),
                'kappa': cohen_kappa_score(y_true, y_pred).item(),
            },
        )

    print(pformat(data).replace('\'', '"').replace(': nan}', ': null}'))


if __name__ == '__main__':
    main()
