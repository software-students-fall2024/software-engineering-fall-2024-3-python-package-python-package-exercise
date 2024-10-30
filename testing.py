import pytest
from pet import Pet, feed, check_pet_mood, check_pet_level, check_pet_health, check_pet_stats, create_pet, release_pet, pets

#resetting pets
@pytest.fixture
def reset_pets():
    global pets
    pets = {}  
@pytest.fixture
def sample_pet():
    # sample pet for testing
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
def test_check_pet_stats_correct_name(sample_pet):
    stats_result = check_pet_stats(sample_pet, "Buddy")
    assert "Pet: Buddy 🐕" in stats_result
    assert "Type: Dog" in stats_result
    assert f"Health: {sample_pet.health}/20" in stats_result
    assert f"Mood: {sample_pet.MOOD_LEVELS.get(sample_pet.mood)}" in stats_result

def test_check_pet_stats_wrong_name(sample_pet):
    stats_result = check_pet_stats(sample_pet, "Charlie")
    assert stats_result == "Pet not found."

def test_create_pet():
    pet = create_pet("Fluffy", "cat")
    assert isinstance(pet, Pet)  
    assert pet.name == "Fluffy"  
    assert pet.type == "cat"     
    assert pet.emoji == '🐈'    
    assert pet.level == 1        
    assert 15 <= pet.health <= 20  
    assert pet.mood == 5      
    assert "Fluffy" in pets  

def test_create_pet_invalid_type(reset_pets):
    pet = create_pet("Unknown", "dragon")
    assert pet.emoji == '🐾'  
    assert pet.type == "dragon" 

def test_create_duplicate_pet(reset_pets):
    create_pet("Fluffy", "cat")
    result = create_pet("Fluffy", "dog")
    assert result == "A pet named Fluffy already exists."

def test_release_pet(reset_pets):
    create_pet("Buddy", "dog")
    
    result = release_pet("Buddy")
    assert result == "Buddy has been released :("
    assert "Buddy" not in pets  

def test_release_pet_not_found(reset_pets):
    result = release_pet("NonExistentPet")
    assert result == "NonExistentPet not found!"
