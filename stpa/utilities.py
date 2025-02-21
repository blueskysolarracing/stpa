from enum import StrEnum

from bs4 import BeautifulSoup

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
