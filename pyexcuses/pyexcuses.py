import random
from typing import Any, Generator, Literal, get_args

from .excuses_en import excuses_en
from .excuses_es import excuses_es
from .exc import LanguageNotFoundError, CategoryNotFoundError

all_excuses = {
    "en": excuses_en,
    "es": excuses_es,
}

SPOKEN_LANGUAGES = Literal["en", "es"]
PROGRAMMING_LANGUAGES = Literal["neutral", "javascript", "python", "matlab", "all"]

SPOKENLANGUAGE_VALUES = set(get_args(SPOKEN_LANGUAGES))
PROGRAMMINGLANGUAGE_VALUES = set(get_args(PROGRAMMING_LANGUAGES))

def generate_excuse(spoken_language: SPOKEN_LANGUAGES = "en", programming_language: PROGRAMMING_LANGUAGES = "neutral") -> str:
    """
    Get a single excuse from the given spoken and programming languages
    """
    try:
        excuses = all_excuses[spoken_language]
    except KeyError:
        raise LanguageNotFoundError("That spoken language isn't in our system ):")    
    
    try:
        return random.choice(excuses[programming_language])
    except KeyError:
        raise CategoryNotFoundError("That programming language isn't in our system ):")
