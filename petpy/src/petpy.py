import random as r
from pet import Pet

pets = {}

def create_pet(pet_name, pet_type):
    if pet_name in pets:
        return f"A pet named {pet_name} already exists."
    
    pet = Pet(name=pet_name, pet_type=pet_type)
    pets[pet_name] = pet  
    return pet

def release_pet(pet_name):
    try:
        del pets[pet_name]
    except KeyError:
        return f"{pet_name} not found!"


def feed(pet, food):
    food_item = Pet.FOOD_MENU.get(food)

    if not food_item:
        return f"{food} is not on the menu!"
    
    pet.mood = pet.change_mood(food_item["mood_boost"])
    pet.health = pet.change_health(food_item["health_boost"])

    mood_description = Pet.MOOD_LEVELS.get(pet.mood, 'neutral 😐')
    mood_message = f"{pet.name} ate {food_item['emoji']} and their mood changed to {mood_description}."
    health_message = f"Their health is now {pet.health}."
    return f"{mood_message} {health_message}"

def get_pet_mood(pet):
    mood_description = Pet.MOOD_LEVELS.get(pet.mood, 'neutral 😐')
    return f"{pet.name}'s current mood is '{mood_description}' (Level {pet.mood})."

def get_pet_level(pet):
    return f"{pet.name} is Level {pet.level} with {pet.experience} XP."

def get_pet_health(pet):
    return f"{pet.name}'s current health is {pet.health}."

def get_pet_stats(pet, pet_name):
    if pet.name.lower() != pet_name.lower():
        return "Pet not found."
    
    stats = f"Pet: {pet.name} {pet.emoji}\n"
    stats += f"Type: {pet.type.capitalize()}\n"
    stats += f"Level: {pet.level}\n"
    stats += f"Experience: {pet.experience}\n"
    stats += f"Health: {pet.health}/20\n"
    stats += f"Mood: {Pet.MOOD_LEVELS.get(pet.mood, 'Unknown')}"
    
    return stats

def fight(pet):
    base_odds = 5
    modifier = (5 - pet.mood) * 0.1
    odds = base_odds + modifier
    result = r.randint(0, 10)

    if result < odds:
        print(f"{pet.name} lost the fight. Better luck next time!")
        pet.change_health(-r.randint(1, 3))
        pet.change_mood(-2)

    else:
        exp_gain = r.randint(15, 20)
        print(f"{pet.name} won the fight and gained {exp_gain} XP!")
        pet.gain_exp(exp_gain)
        pet.change_health(-r.randint(1, 3))

def train_pet(pet):
    intensity = r.randint(1, 3)
    pet.change_mood(-intensity)
    pet.gain_exp(intensity * 7)

    