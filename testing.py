import pytest
from pet import Pet, feed, check_pet_mood, check_pet_level, check_pet_health

@pytest.fixture
def sample_pet():
    # Create a sample pet for testing
    return Pet(name="Buddy", pet_type="dog")

def test_pet_initialization(sample_pet):
    assert sample_pet.name == "Buddy"
    assert sample_pet.type == "dog"
    assert sample_pet.emoji == '🐕'
    assert sample_pet.level == 1
    assert sample_pet.experience == 0
    assert 15 <= sample_pet.health <= 20  
    assert sample_pet.mood == 5

def test_feed_valid_food(sample_pet):
    result = feed(sample_pet, "kfc")
    assert "Buddy ate 🍗 and their mood changed to happy 🤗" in result
    assert 1 <= sample_pet.mood <= 10
    assert 0 <= sample_pet.health <= 20

def test_feed_invalid_food(sample_pet):
    result = feed(sample_pet, "pizza")
    assert result == "pizza is not on the menu!"

def test_check_pet_mood(sample_pet):
    mood_result = check_pet_mood(sample_pet)
    assert f"{sample_pet.name}'s current mood is" in mood_result

def test_check_pet_level(sample_pet):
    level_result = check_pet_level(sample_pet)
    assert level_result == f"{sample_pet.name} is at Level {sample_pet.level}."

def test_check_pet_health(sample_pet):
    health_result = check_pet_health(sample_pet)
    assert f"{sample_pet.name}'s current health is {sample_pet.health}." in health_result