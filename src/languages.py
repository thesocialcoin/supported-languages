from typing import Dict, List

from src.constants import SUPPORTED_LANGUAGES


def get_supported_languages() -> List[str]:
    return [k for k, v in SUPPORTED_LANGUAGES.items() if all(v["webhooks"].values())]


def get_languages() -> List[str]:
    return SUPPORTED_LANGUAGES.keys()


def get_language(alpha_2: str) -> Dict:
    return SUPPORTED_LANGUAGES.get(alpha_2, {})
