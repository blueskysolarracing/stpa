from collections.abc import Iterable, Iterator, Mapping, Sequence
from enum import StrEnum
from importlib import import_module
from typing import Any, TypeVar

from bs4 import BeautifulSoup

_T = TypeVar('_T')
HTML_PARSER = 'html.parser'


def clean_html_text(html_text: str) -> str:
    soup = BeautifulSoup(html_text, HTML_PARSER)

    return soup.get_text(strip=True)


class YesOrNoResponse(StrEnum):
    YES = 'YES'
    NO = 'NO'


class QualityResponse(StrEnum):
    CORRECT_AND_USEFUL = 'CORRECT_AND_USEFUL'
    CORRECT_BUT_USELESS = 'CORRECT_BUT_USELESS'
    INCORRECT = 'INCORRECT'


def import_string(dotted_path: str) -> Any:
    module_path, class_name = dotted_path.rsplit('.', 1)
    module = import_module(module_path)

    return getattr(module, class_name)


def flatten(
        values: Iterable[_T | Sequence[_T] | Mapping[Any, _T]],
) -> Iterator[_T]:
    for value in values:
        if isinstance(value, Sequence):
            yield from value
        elif isinstance(value, Mapping):
            yield from flatten(value.values())
        else:
            yield value
