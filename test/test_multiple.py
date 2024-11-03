import pytest
from unittest.mock import patch, mock_open
from src.fortune.get_multiple_fortunes import getMultipleFortunes

# Mock data for fortune.txt content
mock_fortune_content = """
Good things are coming your way!
%
Happiness is around the corner.
%
Success is in your future.
""".strip()

# Test for single fortune retrieval
@patch("builtins.open", new_callable=mock_open, read_data=mock_fortune_content)
@patch("random.choice")
@patch("random.randint")
def test_get_multiple_fortunes_single(mock_randint, mock_choice, mock_file):
    mock_choice.side_effect = [
        "Good things are coming your way!"
    ]
    mock_randint.side_effect = [42]  # Mocked lucky number

    result = getMultipleFortunes(1)
    expected_result = [["Good things are coming your way!", 42]]

    assert result == expected_result, f"Expected {expected_result}, got {result}"

# Test for multiple fortunes retrieval
@patch("builtins.open", new_callable=mock_open, read_data=mock_fortune_content)
@patch("random.choice")
@patch("random.randint")
def test_get_multiple_fortunes_multiple(mock_randint, mock_choice, mock_file):
    mock_choice.side_effect = [
        "Good things are coming your way!",
        "Happiness is around the corner.",
        "Success is in your future."
    ]
    mock_randint.side_effect = [12, 24, 36]  # Mocked lucky numbers

    result = getMultipleFortunes(3)
    expected_result = [
        ["Good things are coming your way!", 12],
        ["Happiness is around the corner.", 24],
        ["Success is in your future.", 36]
    ]

    assert result == expected_result, f"Expected {expected_result}, got {result}"

# Test for unique fortunes when requesting more than available in one file
@patch("builtins.open", new_callable=mock_open, read_data=mock_fortune_content)
@patch("random.choice")
@patch("random.randint")
def test_get_multiple_fortunes_unique(mock_randint, mock_choice, mock_file):
    mock_choice.side_effect = [
        "Good things are coming your way!",
        "Happiness is around the corner.",
        "Success is in your future.",
        "Good things are coming your way!"  # Should skip if already in result
    ]
    mock_randint.side_effect = [55, 66, 77]  # Mocked lucky numbers

    result = getMultipleFortunes(3)
    expected_result = [
        ["Good things are coming your way!", 55],
        ["Happiness is around the corner.", 66],
        ["Success is in your future.", 77]
    ]

    assert result == expected_result, f"Expected {expected_result}, got {result}"