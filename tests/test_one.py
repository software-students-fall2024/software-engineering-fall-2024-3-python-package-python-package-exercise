import pytest
import random
from unittest.mock import patch, mock_open
from fortunes.random_fortune import get_fortune_cookie

def test_get_fortune_cookie_deterministic_output():
    # Mock content for the 'fortune.txt' file
    mock_fortunes = "Good things come to those who wait.%Patience is a virtue.%Hard work pays off."

    # Mock the file read and the random choice to ensure deterministic output
    with patch('fortunes.random_fortune.importlib.resources.open_text', mock_open(read_data=mock_fortunes)):
        with patch('fortunes.random_fortune.random.choice') as mock_random_choice:
            # Set the mocked random.choice to return the first fortune for consistency
            mock_random_choice.return_value = "Good things come to those who wait."

            result = get_fortune_cookie()
            
            # Verify the output is a formatted string containing the selected fortune and a lucky number
            assert isinstance(result, str)
            assert "🔮 Your Fortune: Good things come to those who wait." in result
            
            # Extract the lucky number and check it falls within the range 0–99
            lucky_number = int(result.split("🍀 Your Lucky Number: ")[1])
            assert 0 <= lucky_number <= 99

def test_get_fortune_cookie_randomness():
    # Provide multiple fortunes to check for varied output
    mock_fortunes = "Fortune favors the bold.%Patience is a virtue.%Hard work pays off."

    with patch('fortunes.random_fortune.importlib.resources.open_text', mock_open(read_data=mock_fortunes)):
        # Call the function multiple times and collect results
        results = {get_fortune_cookie() for _ in range(10)}

        # Ensure that multiple unique fortunes are returned, indicating randomness
        assert len(results) > 1  # Expect at least two different fortunes among the results