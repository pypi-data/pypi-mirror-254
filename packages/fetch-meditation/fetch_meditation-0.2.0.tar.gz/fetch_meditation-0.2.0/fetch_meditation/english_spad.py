from typing import Dict, List, Any
from bs4 import BeautifulSoup
from fetch_meditation.utilities.http_utility import HttpUtility
from fetch_meditation.spad_entry import SpadEntry


class EnglishSpad:
    def __init__(self, settings: Any) -> None:
        self.settings = settings

    def fetch(self) -> 'SpadEntry':
        url = 'https://www.spadna.org/'
        data = HttpUtility.http_get(url)
        soup = BeautifulSoup(data, 'html.parser')
        td_elements = soup.find_all('td')
        spad_keys = ['date', 'title', 'page', 'quote', 'source',
                     'content', 'divider', 'thought', 'copyright']
        result: Dict[str, Any] = {}

        for i, td in enumerate(td_elements):
            if spad_keys[i] == 'content':
                inner_html = ''.join(str(child) for child in td.children)
                result['content'] = [line.strip()
                                     for line in inner_html.split('<br/>') if line.strip()]
            else:
                result[spad_keys[i]] = td.text.strip()

        result["copyright"] = ' '.join(result["copyright"].split())

        return SpadEntry(
            result['date'],
            result['title'],
            result['page'],
            result['quote'],
            result['source'],
            result['content'],
            result['thought'],
            result['copyright']
        )
