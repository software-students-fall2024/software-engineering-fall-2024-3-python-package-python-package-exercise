import pytest
from pyexcuses import pyexcuses


class Tests:

    def test_generate_excuse(self):
        """
        Verify generate_excuse() returns a non-empty string.
        """
        actual = (
            pyexcuses.generate_excuse()
        )  # get the actual return value of generate_excuse()
        assert isinstance(
            actual, str
        ), f"Expected generate_excuse() to return a string. Instead, it returned {actual}"
        assert (
            len(actual) > 0
        ), f"Expected generate_excuse() not to be empty. Instead, it returned a string with {len(actual)} characters"

    def test_suggest_solution(self):
        """
        Verify that suggest_solution() returns a non-empty string.
        """
        actual = (
            pyexcuses.suggest_solution()
        )  # get the actual return value of suggest_solution()
        assert isinstance(
            actual, str
        ), f"Expected suggest_solution() to return a string. Instead, it returned {actual}"
        assert (
            len(actual) > 0
        ), f"Expected suggest_solution() not to be empty. Instead, it returned a string with {len(actual)} characters"
