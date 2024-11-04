import random as r 

pets = {}

class Pet:
    MAX_MOOD = 10

    PET_EMOJIS = {
        'python': '🐍',
        'dog': '🐕',
        'cat': '🐈',
        'frog': '🐸',
        'panda': '🐼',
        't-rex': '🦖',
        'shark': '🦈',
        'chicken': '🐓',
        'unicorn': '🦄',
        'pig': '🐖',
        'octopus': '🐙',
        'otter': '🦦'
    }

    MOOD_LEVELS = {
        1: 'crying 😭',  
        2: 'sad 😞', 
        3: 'angry 😡', 
        4: 'unhappy 😕',
        5: 'neutral 😐',
        6: 'smiling 🙂',
        7: 'happy 🤗', 
        8: 'cheerful 🥳',
        9: 'extremely happy 🫨',
        10: 'ecstatic 🤩'
    }

    FOOD_MENU = {
        'salad': {
            'emoji': '🥗',
            'mood_boost': -3,
            'health_boost': 3
        },
        'mushroom': {
            'emoji': '🍄',
            'mood_boost': -2,
            'health_boost': 2
        },
        'carrot': {
            'emoji': '🥕',
            'mood_boost': -1,
            'health_boost': 1
        },
        'candy': {
            'emoji': '🍬',
            'mood_boost': 1,
            'health_boost': -1
        },
        'kfc': {
            'emoji': '🍗',
            'mood_boost': 2,
            'health_boost': -2
        },
        'sake': {
            'emoji': '🍶',
            'mood_boost': 3,
            'health_boost': -3
        }
    }

    def __init__(self, name, pet_type):
        self.MAX_HEALTH = r.randint(15, 20)

        self.name = name
        self.type = pet_type.lower()
        self.emoji = self.PET_EMOJIS.get(self.type, '🐾')
        self.level = 1
        self.experience = 0
        self.health = self.MAX_HEALTH
        self.mood = 5

    def change_mood(self, amount):
        self.mood += amount
        
        if self.mood > Pet.MAX_MOOD:
            release_pet(self.name)
            print(f"{self.name} has entered a state of euphoric madness and has left you forever.")
        elif self.mood <= 0:
            release_pet(self.name)
            print(f"{self.name}'s spirit is broken and has left you forever.")

        return self.mood


    def change_health(self, amount):
        self.health = min(self.health + amount, self.MAX_HEALTH)

        if self.health <= 0:
            release_pet(self.name)
            print(f"{self.name} is in a better place. Perhaps you were too harsh.")

        return self.health

    def gain_exp(self, exp):
        print(f"{self.name} has gained {exp} XP!")
        self.experience += exp

        if self.experience >= 100:
            self.level += 1
            self.experience -= 100
            print(f"Congratulations! {self.name} has leveled up to {self.level}!")
    
        return self.experience

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
    food_item = pet.FOOD_MENU.get(food)

    if not food_item:
        return f"{food} is not on the menu!"
    
    prev_pet_count = len(pets)
    pet.mood = pet.change_mood(food_item["mood_boost"])
    pet.health = pet.change_health(food_item["health_boost"])

    if (prev_pet_count - len(pets)) > 0:
        return f"{pet.name} left you while eating."

    mood_description = Pet.MOOD_LEVELS.get(pet.mood)
    mood_message = f"{pet.name} ate {food_item['emoji']} and their mood changed to {mood_description}."
    health_message = f"Their health is now {pet.health}."
    return f"{mood_message} {health_message}"

def get_pet_mood(pet):
    mood_description = Pet.MOOD_LEVELS.get(pet.mood)
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
        print(f"{pet.name} won the fight!")
        pet.gain_exp(exp_gain)
        pet.change_health(-r.randint(1, 3))

def train_pet(pet):
    intensity = r.randint(1, 3)
    intensity_names = ["light", "moderate", "intense"]
    print(f"{pet.name} did some {intensity_names[intensity - 1]} training.")
    print(f"I don't think pets like training... {pet.name}'s mood decreased by {intensity}.")
    pet.gain_exp(intensity * 7)
    pet.change_mood(-intensity)

