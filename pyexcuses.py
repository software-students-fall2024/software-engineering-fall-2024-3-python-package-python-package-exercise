import random
from typing import Any, Generator, Literal, get_args

from .excuses_en import excuses_en
from .excuses_es import excuses_es
from .exc import LanguageNotFoundError, CategoryNotFoundError


all_excuses = {
    "en": excuses_en,
    "es": excuses_es,
}


LANGUAGES = Literal["en", "es"]
CATEGORIES = Literal["neutral", "javascript", "python", "matlab", "all"]

LANGUAGE_VALUES = set(get_args(LANGUAGES))
CATEGORY_VALUES = set(get_args(CATEGORIES))


def get_excuses(language: LANGUAGES = "en", category: CATEGORIES = "neutral") -> list[str]:
    """
    Get a list of excuses from the given language and category
    """
    try:
        excuses = all_excuses[language]
    except KeyError:
        raise LanguageNotFoundError(f"No such language: {language}")

    try:
        return excuses[category]
    except KeyError:
        raise CategoryNotFoundError("No such category %s in language %s" % (category, language))


def get_excuse(language: LANGUAGES = "en", category: CATEGORIES = "neutral") -> str:
    """
    Get a single excuse from the given language and category
    """
    excuses = get_excuses(language, category)
    return random.choice(excuses)


def forever(language: LANGUAGES = "en", category: CATEGORIES = "neutral") -> Generator[str, Any, Any]:
    """
    Generate excuses forever
    """
    while True:
        yield get_excuse(language, category)
