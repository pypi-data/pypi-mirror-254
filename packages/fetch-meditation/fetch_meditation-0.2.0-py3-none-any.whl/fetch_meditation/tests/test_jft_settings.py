import pytest
from fetch_meditation.jft_settings import JftSettings
from fetch_meditation.jft_language import JftLanguage


def test_constructor():
    settings = JftSettings(JftLanguage.English)
    assert settings.language == JftLanguage.English
