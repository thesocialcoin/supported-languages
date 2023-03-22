from typing import Dict, List

from src.constants import COUNTRIES
from src.languages import get_supported_languages


def get_available_countries() -> List[str]:
    languages = get_supported_languages()
    return [k for k, v in COUNTRIES.items() if any(lang in languages for lang in v["languages"])]


def get_countries() -> List[str]:
    return COUNTRIES.keys()


def get_country(alpha_2: str) -> Dict:
    return COUNTRIES.get(alpha_2, {})


def get_languages(alpha_2: str) -> List[str]:
    return COUNTRIES.get(alpha_2, {})["languages"]
