import random as r 

class Pet:
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
        self.name = name
        self.type = pet_type.lower()
        self.emoji = self.PET_EMOJIS.get(self.type, '🐾')
        self.level = 1
        self.experience = 0
        self.health = r.randint(15, 20)
        self.mood = 5

def feed(pet, food):
    food_item = Pet.FOOD_MENU.get(food)

    if not food_item:
        return f"{food} is not on the menu!"

    pet.mood = min(10, max(1, pet.mood + food_item["mood_boost"]))
    pet.health = min(20, max(0, pet.health + food_item["health_boost"]))

    mood_message = f"{pet.name} ate {food_item['emoji']} and their mood changed by {food_item['mood_boost']}."
    health_message = f"Their health is now {pet.health}."
    return f"{mood_message} {health_message}"



