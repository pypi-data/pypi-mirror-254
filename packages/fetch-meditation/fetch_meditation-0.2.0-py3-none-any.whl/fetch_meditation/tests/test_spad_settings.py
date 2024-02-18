import pytest
from fetch_meditation.spad_settings import SpadSettings
from fetch_meditation.spad_language import SpadLanguage


def test_constructor():
    settings = SpadSettings(SpadLanguage.English)
    assert settings.language == SpadLanguage.English
