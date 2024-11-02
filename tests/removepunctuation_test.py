import pytest
from pytextalterations import removepunctuation


class Tests:

    def test_text_sentence(self):
        assert removepunctuation("Hello!") == "hello"

    def test_all_caps(self):
        assert removepunctuation("HELLO") == "hello"

    def test_with_numbers(self):
        assert removepunctuation("Hello1234!") == "hello1234"

    def test_with_spaces(self):
        assert removepunctuation("This is a test Example!") == "this is a test example"

    def test_empty_string(self):
        assert removepunctuation("") == ""

    def test_multiple_punctuation(self):
        assert removepunctuation("!@#$%./,a") == "a"
