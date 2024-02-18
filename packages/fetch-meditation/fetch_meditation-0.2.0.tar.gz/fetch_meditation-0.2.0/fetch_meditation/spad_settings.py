from dataclasses import dataclass
from fetch_meditation.spad_language import SpadLanguage


@dataclass
class SpadSettings:
    language: SpadLanguage
