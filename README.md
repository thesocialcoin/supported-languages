# supported_languages

This library helps all Citibeats projects to centralize the supported languages and the available countries.

## Format of the data

### Countries

The country [codes](https://restcountries.com/v3.1/independent?status=true&fields=name,cca2,languages) follows the [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) international standard and they are formatted as an Alpha-2 code.

### Languages

The language [codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) follows the [ISO 639-1](https://www.iso.org/standard/39534.html) international standard and they are formatted as an Alpha-2 code.

## Usage

### `supported_languages.countries`

- `get_supported_languages`

```python
def get_supported_languages() -> List[str]:
    """
    Get supported languages.

    Returns:
        List[str]: List of languages in ISO 639-1 alpha-2 format
    """
```

- `get_countries`

```python
def get_countries() -> List[str]:
    """
    Get all countries.

    Returns:
        List[str]: List of countries in ISO 3166 alpha-2 format
    """
```

- `get_country`

```python
def get_country(country_code: str) -> Dict:
    """
    Get information of a country.

    Args:
        country_code (str): Country code in ISO 3166 alpha-2 format

    Returns:
        Dict: Country's information
    """
```

- `get_languages`

```python
def get_languages(country_code: str) -> List[str]:
    """
    Get all languages from a country.

    Args:
        country_code (str): Country code in ISO 3166 alpha-2 format

    Returns:
        List[str]: List of languages in ISO 639-1 alpha-2 format
    """
```

### `supported_languages.languages`

- `get_supported_languages`

```python
def get_supported_languages() -> List[str]:
    """
    Get supported languages.

    Returns:
        List[str]: List of languages in ISO 639-1 alpha-2 format
    """
```

- `get_languages`

```python
def get_languages() -> List[str]:
    """
    Get all languages.

    Returns:
        List[str]: List of languages in ISO 639-1 alpha-2 format
    """
```

- `get_language`

```python
def get_language(language_code: str) -> Dict:
    """
    Get language's information.

    Args:
        language_code (str): Language code in ISO 639-1 alpha-2 format

    Returns:
        Dict: Language's information
    """
```
