from typing import Dict, List

from src.constants import AVAILABLE_COUNTRIES
from src.languages import get_supported_languages


def get_available_countries() -> List[str]:
    languages = get_supported_languages()
    return [k for k, v in AVAILABLE_COUNTRIES.items() if any(lang in languages for lang in v["official_languages"])]


def get_countries() -> List[str]:
    return AVAILABLE_COUNTRIES.keys()


def get_country(alpha_2: str) -> Dict:
    return AVAILABLE_COUNTRIES.get(alpha_2, {})


def get_official_languages(alpha_2: str) -> List[str]:
    return AVAILABLE_COUNTRIES.get(alpha_2, {})["official_languages"]
