from typing import Dict, List

from src.constants import SUPPORTED_LANGUAGES


def get_supported_languages() -> List[str]:
    """
    Get supported languages.

    Returns:
        List[str]: List of languages in ISO 639-1 alpha-2 format
    """
    return [k for k, v in SUPPORTED_LANGUAGES.items() if all(v["webhooks"].values())]


def get_languages() -> List[str]:
    """
    Get all languages.

    Returns:
        List[str]: List of languages in ISO 639-1 alpha-2 format
    """
    return SUPPORTED_LANGUAGES.keys()


def get_language(language_code: str) -> Dict:
    """
    Get language's information.

    Args:
        language_code (str): Language code in ISO 639-1 alpha-2 format

    Returns:
        Dict: Language's information
    """
    return SUPPORTED_LANGUAGES.get(language_code, {})
