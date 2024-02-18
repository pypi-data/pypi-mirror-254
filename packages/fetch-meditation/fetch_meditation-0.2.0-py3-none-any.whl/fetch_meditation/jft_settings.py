from dataclasses import dataclass
from fetch_meditation.jft_language import JftLanguage


@dataclass
class JftSettings:
    language: JftLanguage
