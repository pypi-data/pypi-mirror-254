from typing import Dict, List, Any
import re
import pytz
from datetime import datetime
from bs4 import BeautifulSoup
from fetch_meditation.utilities.http_utility import HttpUtility
from fetch_meditation.jft_entry import JftEntry


def remove_newlines_from_dict(input_dict):
    for key, value in input_dict.items():
        if isinstance(value, str):
            input_dict[key] = value.replace('\n', '')
        elif isinstance(value, dict):
            remove_newlines_from_dict(value)


class SpanishJft:
    def __init__(self, settings: Any) -> None:
        self.settings = settings

    def fetch(self) -> 'JftEntry':
        timezone = pytz.timezone('America/Mexico_City')
        date = datetime.now(timezone)
        url = 'https://fzla.org/wp-content/uploads/meditaciones/' + date.strftime('%m/%d') + '.html'
        data = HttpUtility.http_get(url)
        soup = BeautifulSoup(data, 'html.parser')

        # Get content
        paragraphs = []
        for i in range(1, 4):
            comment = soup.find(string=f'PARRAFO {i}')
            if comment:
                paragraph = comment.find_next('p').get_text(strip=True)
                if not paragraph.startswith("Sólo por Hoy"):
                    paragraphs.append(paragraph.replace("\n", ""))

        # Get Thought
        start_comment = soup.find(string='SOLO X HOY insertar AQUI sin el Solo por Hoy')
        end_comment = soup.find(string='FIN SOLO X HOY')

        extracted_thought = ''
        if start_comment and end_comment:
            start_node = start_comment.find_next_sibling()
            while start_node and start_node != end_comment:
                extracted_thought += str(start_node)
                start_node = start_node.find_next_sibling()

        result = {}
        for element in soup.find_all('p'):
            class_name = element.get('class', [])
            if class_name == ['fecha-sxh']:
                result['date'] = element.get_text()
            elif class_name == ['titulo-sxh']:
                result['title'] = element.get_text()
            elif class_name == ['descripcion-sxh']:
                result['quote'] = element.get_text(strip=True)
            elif class_name == ['numero-pagina-sxh']:
                result['source'] = element.get_text()

        thought_div = soup.find('div', attrs={'id': 'soloxhoycontainer'})
        thought = thought_div.get_text(strip=True).replace("\n", "")
        result['thought'] = re.sub(r'(Sólo por Hoy:)', r'<b>\1 </b> ', thought)

        result['content'] = paragraphs
        result['page'] = ''
        result[
            'copyright'] = 'Servicio del Foro Zonal Latinoamericano, Copyright 2017 NA World Services, Inc. Todos los Derechos Reservados.'
        remove_newlines_from_dict(result)
        return JftEntry(
            result['date'],
            result['title'],
            result['page'],
            result['quote'],
            result['source'],
            result['content'],
            result['thought'],
            result['copyright']
        )
