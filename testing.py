import pytest
from pet import Pet  # Replace `pet` with the filename if it's different

# Test Initialization
def test_pet_initialization():
    pet = Pet(name="Buddy", pet_type="dog")
    assert pet.name == "Buddy"
    assert pet.type == "dog"
    assert pet.emoji == Pet.PET_EMOJIS["dog"]
    assert 15 <= pet.health <= 20  # Health should be a random value between 15 and 20
    assert pet.mood == 5  # Default mood level
    assert pet.level == 1
    assert pet.experience == 0

# Test Feeding with Valid Food Items
@pytest.mark.parametrize("food_item, mood_boost, health_boost, emoji", [
    ("salad", -3, 3, "🥗"),
    ("mushroom", -2, 2, "🍄"),
    ("carrot", -1, 1, "🥕"),
    ("candy", 1, -1, "🍬"),
    ("kfc", 2, -2, "🍗"),
    ("sake", 3, -3, "🍶")
])
def test_feed_valid_food(food_item, mood_boost, health_boost, emoji):
    pet = Pet(name="Buddy", pet_type="dog")
    initial_health = pet.health
    initial_mood = pet.mood

    result = pet.feed(food_item)
    expected_health = min(20, initial_health + health_boost)
    expected_mood = initial_mood + mood_boost

    assert pet.health == expected_health
    assert pet.mood == expected_mood
    assert result == f"Buddy ate {emoji} and their mood changed by {mood_boost}. Their health is now {expected_health}."

# Test Feeding with Invalid Food Item
def test_feed_invalid_food():
    pet = Pet(name="Buddy", pet_type="dog")
    result = pet.feed("pizza")
    assert result == "None is not on the menu!"

# Test Mood Limits (to ensure it doesn’t go below 1 or above 10)
def test_mood_limits():
    pet = Pet(name="Buddy", pet_type="dog")
    
    # Feeding with mood-boosting food to increase mood above 10
    pet.mood = 9
    pet.feed("sake")  # Mood boost of +3 should cap mood at 10
    assert pet.mood == 10

    # Feeding with mood-reducing food to decrease mood below 1
    pet.mood = 2
    pet.feed("salad")  # Mood boost of -3 should cap mood at 1
    assert pet.mood == 1

