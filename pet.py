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
        self.mood = "happy 😁"
        
    def feed(self, food):
        food = self.FOOD_MENU.get(food)
        
        if not food:
            return f"{food} is not on the menu!"
        
        self.mood += food["mood_boost"]
        self.health = min(20, self.health + food["health_boost"]) 
        
        mood_message = f"{self.name} ate {food['emoji']} and their mood changed by {food['mood_boost']}."
        health_message = f"Their health is now {self.health}."
        return f"{mood_message} {health_message}"