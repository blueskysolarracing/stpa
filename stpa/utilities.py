from bs4 import BeautifulSoup

HTML_PARSER = 'html.parser'


def clean_html_text(html_text: str) -> str:
    soup = BeautifulSoup(html_text, HTML_PARSER)

    return soup.get_text(strip=True)
