from unittest.mock import patch
import pytest
from pyanimals.main import *

# move test #1: handles valid animals
@pytest.mark.parametrize("validAnimal", ["cat", "bunny", "elephant", "rabbit"])
def test_move_validAnimal(validAnimal):
    # check that there aren't any errors
    move(validAnimal)

# move test #2: screen is cleared
@pytest.mark.parametrize("animal", ["cat", "bunny", "elephant", "rabbit"])
@patch("pyanimals.main.clearScreen")
def test_move_clearscreen(mockClearScreen, animal):
    move(animal)
    # check that clearScreen is called the expected number of times
    assert mockClearScreen.call_count == 25

# move test #3: animal didn't move off screen
@pytest.mark.parametrize("animal", ["cat", "bunny", "elephant", "rabbit"])
@patch("pyanimals.main.clearScreen")
@patch("builtins.print")
def test_move_inBounds(mockInBounds, mockClearScreen, animal):
    screenWidth = 80
    move(animal)
    
    for call in mockInBounds.call_args_list:
        printedText = call[0][0]
        
        if printedText.strip():
            leadingSpaces = len(printedText) - len(printedText.lstrip())
            # check that leading spaces + animal width <= screen width
            assert leadingSpaces + len(printedText.lstrip().splitlines()[0]) <= screenWidth, \
                "Animal moved off screen"