import pytest
from pyquotes.quote_of_the_day import get_quote_of_the_day

def test_get_quote_of_the_day_returns_string():
    quote = get_quote_of_the_day()
    assert isinstance(quote, str), "Quote of the Day should be a string"
