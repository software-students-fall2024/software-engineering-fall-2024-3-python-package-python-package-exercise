import pytest
from petpy.src.pet import Pet, feed, check_pet_mood, check_pet_level, check_pet_health, check_pet_stats, create_pet, release_pet, pets

#resetting pets
@pytest.fixture
def reset_pets():
    global pets
    pets = {}  
@pytest.fixture
# Test pet initialization
def sample_pet():
    return Pet(name="Buddy", pet_type="dog")

def test_pet_initialization(sample_pet):
    assert sample_pet.name == "Buddy"
    assert sample_pet.type == "dog"
    assert sample_pet.emoji == '🐕'
    assert sample_pet.level == 1
    assert sample_pet.experience == 0
    assert 15 <= sample_pet.health <= 20  
    assert sample_pet.mood == 5

def test_pet_initialization_with_unknown_type():
    pet = Pet(name="Unknown", pet_type="dragon")
    assert pet.name == "Unknown"
    assert pet.type == "dragon"
    assert pet.emoji == '🐾' 


# Feed tests
def test_feed_valid_food(sample_pet):
    result = feed(sample_pet, "kfc")
    assert "Buddy ate 🍗 and their mood changed to happy 🤗" in result
    assert 1 <= sample_pet.mood <= 10
    assert 0 <= sample_pet.health <= 20

def test_feed_different_foods(sample_pet):
    result_salad = feed(sample_pet, "salad")
    result_candy = feed(sample_pet, "candy")
    assert "Buddy ate 🥗 and their mood changed" in result_salad
    assert "Buddy ate 🍬 and their mood changed" in result_candy

def test_feed_invalid_food(sample_pet):
    result = feed(sample_pet, "pizza")
    assert result == "pizza is not on the menu!"


# Mood checks
def test_check_pet_mood(sample_pet):
    mood_result = check_pet_mood(sample_pet)
    assert f"{sample_pet.name}'s current mood is" in mood_result

def test_check_pet_mood_after_feeding(sample_pet):
    feed(sample_pet, "sake")
    mood_result = check_pet_mood(sample_pet)
    assert f"{sample_pet.name}'s current mood is" in mood_result

def test_check_pet_mood_limits(sample_pet):
    sample_pet.mood = 1  # lowest mood
    result = check_pet_mood(sample_pet)
    assert "crying 😭" in result
    sample_pet.mood = 10  # highest mood
    result = check_pet_mood(sample_pet)
    assert "ecstatic 🤩" in result


# Level checks
def test_check_pet_level(sample_pet):
    level_result = check_pet_level(sample_pet)
    assert level_result == f"{sample_pet.name} is at Level {sample_pet.level} with {sample_pet.experience} XP."

def test_check_pet_level_after_experience(sample_pet):
    sample_pet.level = 2
    sample_pet.experience = 30
    level_result = check_pet_level(sample_pet)
    assert "Level 2" in level_result
    assert "30 XP" in level_result

def test_check_pet_level_no_experience(sample_pet):
    sample_pet.experience = 0
    result = check_pet_level(sample_pet)
    assert "0 XP" in result


# Health checks
def test_check_pet_health(sample_pet):
    health_result = check_pet_health(sample_pet)
    assert f"{sample_pet.name}'s current health is {sample_pet.health}." in health_result

def test_check_pet_health_after_feeding(sample_pet):
    feed(sample_pet, "carrot")
    health_result = check_pet_health(sample_pet)
    assert "current health is" in health_result

def test_check_pet_health_limits(sample_pet):
    sample_pet.health = 0  # lowest health
    health_result = check_pet_health(sample_pet)
    assert "current health is 0" in health_result
    sample_pet.health = 20  # highest health
    health_result = check_pet_health(sample_pet)
    assert "current health is 20" in health_result


# Stats checks
def test_check_pet_stats_correct_name(sample_pet):
    stats_result = check_pet_stats(sample_pet, "Buddy")
    assert "Pet: Buddy 🐕" in stats_result
    assert "Type: Dog" in stats_result
    assert f"Health: {sample_pet.health}/20" in stats_result
    assert f"Mood: {sample_pet.MOOD_LEVELS.get(sample_pet.mood)}" in stats_result

def test_check_pet_stats_wrong_name(sample_pet):
    stats_result = check_pet_stats(sample_pet, "Charlie")
    assert stats_result == "Pet not found."

def test_check_pet_stats_different_pet():
    pet = Pet(name="Whiskers", pet_type="cat")
    stats_result = check_pet_stats(pet, "Whiskers")
    assert "Pet: Whiskers 🐈" in stats_result


# Create pet tests
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


# Release pet tests
def test_release_pet(reset_pets):
    create_pet("Buddy", "dog")
    result = release_pet("Buddy")
    assert result == "Buddy has been released :("
    assert "Buddy" not in pets  

def test_release_pet_not_found(reset_pets):
    result = release_pet("NonExistentPet")
    assert result == "NonExistentPet not found!"

def test_release_pet_not_found(reset_pets):
    result = release_pet("NonExistentPet")
    assert result == "NonExistentPet not found!"

def test_release_multiple_pets(reset_pets):
    create_pet("Buddy", "dog")
    create_pet("Fluffy", "cat")
    release_result_buddy = release_pet("Buddy")
    release_result_fluffy = release_pet("Fluffy")
    assert release_result_buddy == "Buddy has been released :("
    assert release_result_fluffy == "Fluffy has been released :("
    assert "Buddy" not in pets
    assert "Fluffy" not in pets
