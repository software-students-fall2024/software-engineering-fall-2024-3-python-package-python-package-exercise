import random as r 
from petpy import release_pet

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


    def change_health(self, amount):
        self.health = min(self.health + amount, self.MAX_HEALTH)

        if self.health <= 0:
            release_pet(self.name)
            print(f"{self.name} is in a better place. Perhaps you were too harsh.")

    def gain_exp(self, exp):
        self.experience += exp
        print(f"{self.name} has gained {exp} XP!")

        if self.experience >= 100:
            self.level += 1
            self.experience = 0
            print(f"Congratulations! {self.name} has leveled up to {self.level}!")

