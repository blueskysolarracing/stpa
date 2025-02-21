from base64 import b64encode
from collections.abc import Iterable, Iterator
from re import compile, findall, MULTILINE, sub

from openai import OpenAI

from stpa.definitions import (
    Definition,
    Hazard,
    Loss,
    Scenario,
    SubHazard,
    UnsafeControlAction,
)
from stpa.utilities import QualityResponse, YesOrNoResponse

_DEFINITION_LINKS_PATTERN = compile(r'\s+\[.*?\]$')
_DEFINITION_NAME_PATTERN = compile(r'^.+?:\s+')


def _get_definition_name_body(definition: Definition | str) -> str:
    return sub(_DEFINITION_LINKS_PATTERN, '', str(definition))


def _get_definition_body_links(definition: Definition | str) -> str:
    return sub(_DEFINITION_NAME_PATTERN, '', str(definition))


def _get_definition_body(definition: Definition | str) -> str:
    return _get_definition_name_body(_get_definition_body_links(definition))


def _number_lines(lines: Iterable[str]) -> Iterator[str]:
    for i, line in enumerate(lines):
        line = ' '.join(line.splitlines())

        yield f'{i + 1}. {line}'


def _number_definitions(definitions: Iterable[Definition]) -> Iterator[str]:
    return _number_lines(map(_get_definition_body_links, definitions))


_NUMBER_PATTERN = compile(r'^\d+\. ')


def _unnumber_lines(lines: Iterable[str]) -> Iterator[str]:
    for line in lines:
        yield sub(_NUMBER_PATTERN, '', line)


_RAW_DEFINITION_PATTERN = compile(r'^\d+\. .+$', MULTILINE)


def _get_raw_definitions(raw_definitions: str) -> Iterator[str]:
    return map(str.strip, findall(_RAW_DEFINITION_PATTERN, raw_definitions))


_EQUALITY_QUERY_PROMPT = '''
Are the STPA Definitions {} and {} saying similar things?

{}
{}

Answer only "YES" or "NO" (without quotes).
'''.strip()


def query_equality(
        client: OpenAI,
        model: str,
        definition_0: Definition,
        definition_1: Definition,
        seed: int | None = None,
        temperature: int | None = None,
) -> bool:
    prompt = _EQUALITY_QUERY_PROMPT.format(
        definition_0.name,
        definition_1.name,
        definition_0,
        definition_1,
    )
    completion = client.chat.completions.create(
        model=model,
        messages=[{'role': 'user', 'content': prompt}],
        seed=seed,
        temperature=temperature,
    )
    content = completion.choices[0].message.content

    assert content is not None

    content = content.strip().strip('"')
    response = YesOrNoResponse(content)

    return response == YesOrNoResponse.YES


_LINKAGE_QUERY_PROMPT = '''
Is the STPA Definition {} directly linked to Definition {}?

{}
{}

Answer only "YES" or "NO" (without quotes).
'''.strip()


def query_linkage(
        client: OpenAI,
        model: str,
        definition: Definition,
        link: Definition,
        seed: int | None = None,
        temperature: int | None = None,
) -> bool:
    prompt = _LINKAGE_QUERY_PROMPT.format(
        definition.name,
        link.name,
        _get_definition_name_body(definition),
        _get_definition_name_body(link),
    )
    completion = client.chat.completions.create(
        model=model,
        messages=[{'role': 'user', 'content': prompt}],
        seed=seed,
        temperature=temperature,
    )
    content = completion.choices[0].message.content

    assert content is not None

    content = content.strip().strip('"')
    response = YesOrNoResponse(content)

    return response == YesOrNoResponse.YES


_RAW_UNSAFE_CONTROL_ACTIONS_GENERATION_PROMPT = '''
Generate {} unsafe control actions of the system shown in the control\
 structure diagram.

An unsafe control action is linked to a single (sub)hazard and follows one of\
 the four patterns: 1) not providing causes hazard 2) providing causes hazard\
 3) too early, too late, out of order or 4) stopped too soon, applied too long.

Losses:

{}

Hazards:

{}

Examples unsafe control actions:

{}

Write each unsafe control action in a single line, preceded by a number.
'''.strip()


def generate_raw_unsafe_control_actions(
        client: OpenAI,
        model: str,
        count: int,
        losses: Iterable[Loss],
        hazards: Iterable[Hazard | SubHazard],
        unsafe_control_actions: Iterable[UnsafeControlAction],
        diagram_pathname: str,
        seed: int | None = None,
        temperature: int | None = None,
) -> list[str]:
    prompt = _RAW_UNSAFE_CONTROL_ACTIONS_GENERATION_PROMPT.format(
        count,
        '\n'.join(map(str, losses)),
        '\n'.join(map(str, hazards)),
        '\n'.join(_number_definitions(unsafe_control_actions)),
    )

    with open(diagram_pathname, 'rb') as file:
        base64_image = b64encode(file.read()).decode('utf-8')

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                'role': 'user',
                'content': [
                    {
                        'type': 'text',
                        'text': prompt,
                    },
                    {
                        'type': 'image_url',
                        'image_url': {
                            'url': f'data:image/jpeg;base64,{base64_image}',
                        },
                    },
                ],
            },
        ],
        seed=seed,
        temperature=temperature,
    )
    response = completion.choices[0].message.content

    assert isinstance(response, str)

    raw_unsafe_control_actions = list(
        _unnumber_lines(_get_raw_definitions(response)),
    )

    return raw_unsafe_control_actions


_RAW_SCENARIO_GENERATION_PROMPT = '''
Generate {} loss scenarios of the system shown in the control structure\
 diagram.

A scenario must link to a single hazard. It may optionally also link to an\
 unsafe control action.

Losses:

{}

Hazards:

{}

Unsafe control actions:

{}

Example loss scenarios:

{}

Write each unsafe control action in a single line, preceded by a number.
'''.strip()


def generate_raw_scenarios(
        client: OpenAI,
        model: str,
        count: int,
        losses: Iterable[Loss],
        hazards: Iterable[Hazard | SubHazard],
        unsafe_control_actions: Iterable[UnsafeControlAction],
        scenarios: Iterable[Scenario],
        diagram_pathname: str,
        seed: int | None = None,
        temperature: int | None = None,
) -> list[str]:
    prompt = _RAW_SCENARIO_GENERATION_PROMPT.format(
        count,
        '\n'.join(map(str, losses)),
        '\n'.join(map(str, hazards)),
        '\n'.join(map(str, unsafe_control_actions)),
        '\n'.join(_number_definitions(scenarios)),
    )

    with open(diagram_pathname, 'rb') as file:
        base64_image = b64encode(file.read()).decode('utf-8')

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                'role': 'user',
                'content': [
                    {
                        'type': 'text',
                        'text': prompt,
                    },
                    {
                        'type': 'image_url',
                        'image_url': {
                            'url': f'data:image/jpeg;base64,{base64_image}',
                        },
                    },
                ],
            },
        ],
        seed=seed,
        temperature=temperature,
    )
    response = completion.choices[0].message.content

    assert isinstance(response, str)

    raw_scenarios = list(_unnumber_lines(_get_raw_definitions(response)))

    return raw_scenarios


_RAW_UNSAFE_CONTROL_ACTION_QUALITY_CLASSIFICATION_PROMPT = '''
An unsafe control action is linked to a single (sub)hazard and follows one of\
 the four patterns: 1) not providing causes hazard 2) providing causes hazard\
 3) too early, too late, out of order or 4) stopped too soon, applied too long.

Examples:

{}

Classify the quality of the following unsafe control action (UCA).

UCA: {}

Answer only "CORRECT_AND_USEFUL", "CORRECT_BUT_USELESS", or "INCORRECT"\
 (without quotes).
'''.strip()


def classify_raw_unsafe_control_action_quality(
        client: OpenAI,
        model: str,
        example_unsafe_control_actions: Iterable[UnsafeControlAction],
        raw_unsafe_control_action: str,
        seed: int | None = None,
        temperature: int | None = None,
) -> QualityResponse:
    prompt = _RAW_UNSAFE_CONTROL_ACTION_QUALITY_CLASSIFICATION_PROMPT.format(
        '\n'.join(map(str, example_unsafe_control_actions)),
        raw_unsafe_control_action,
    )
    completion = client.chat.completions.create(
        model=model,
        messages=[{'role': 'user', 'content': prompt}],
        seed=seed,
        temperature=temperature,
    )
    content = completion.choices[0].message.content

    assert content is not None

    content = content.strip().strip('"')
    response = QualityResponse(content)

    return response


_RAW_SCENARIO_QUALITY_CLASSIFICATION_PROMPT = '''
A scenario must link to a single hazard. It may optionally also link to an\
 unsafe control action.

Examples:

{}

Classify the quality of the following loss scenario.

Scenario: {}

Answer only "CORRECT_AND_USEFUL", "CORRECT_BUT_USELESS", or "INCORRECT"\
 (without quotes).
'''.strip()


def classify_raw_scenario_quality(
        client: OpenAI,
        model: str,
        example_scenarios: Iterable[Scenario],
        raw_scenario: str,
        seed: int | None = None,
        temperature: int | None = None,
) -> QualityResponse:
    prompt = _RAW_SCENARIO_QUALITY_CLASSIFICATION_PROMPT.format(
        '\n'.join(map(str, example_scenarios)),
        raw_scenario,
    )
    completion = client.chat.completions.create(
        model=model,
        messages=[{'role': 'user', 'content': prompt}],
        seed=seed,
        temperature=temperature,
    )
    content = completion.choices[0].message.content

    assert content is not None

    content = content.strip().strip('"')
    response = QualityResponse(content)

    return response
