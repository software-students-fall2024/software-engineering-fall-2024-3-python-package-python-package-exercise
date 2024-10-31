import pytest
from PIL import Image
from tamagotchi import get_ascii_art, getpet, G_SCALE_1, G_SCALE_2
import os

# Mock data
test_image_path = "test_image.png"
ascii_art_sample = "This is a sample ASCII art"

@pytest.fixture
def create_test_image():
    """Fixture to create a temporary grayscale image for testing."""
    image = Image.new("L", (50, 50), color=128)  
    image.save(test_image_path)
    yield test_image_path
    os.remove(test_image_path)  

def test_get_ascii_art_valid_image(create_test_image):
    """Test get_ascii_art with a valid image."""
    ascii_art = get_ascii_art(create_test_image, scale=0.1, character_map=G_SCALE_1)
    assert ascii_art is not None
    assert isinstance(ascii_art, str)
    assert len(ascii_art) > 0

def test_get_ascii_art_invalid_path():
    """Test get_ascii_art with an invalid image path."""
    ascii_art = get_ascii_art("non_existent_image.png", scale=0.1, character_map=G_SCALE_1)
    assert ascii_art is None

def test_get_ascii_art_different_character_map(create_test_image):
    """Test get_ascii_art with a different character map."""
    ascii_art = get_ascii_art(create_test_image, scale=0.1, character_map=G_SCALE_2)
    assert ascii_art is not None
    assert isinstance(ascii_art, str)
    assert len(ascii_art) > 0

def test_getpet_valid_file():
    """Test getpet with a valid pet file."""
    number = 1
    pet_art = getpet(number)
    assert pet_art is not None
    assert isinstance(pet_art, str)
    assert len(pet_art) > 0

def test_getpet_invalid_file():
    """Test getpet with an invalid file number."""
    pet_art = getpet(999)  
    assert pet_art is None

def test_getpet_non_numeric_input():
    """Test getpet with a non-numeric input to check error handling."""
    with pytest.raises(TypeError):
        getpet("not_a_number")
