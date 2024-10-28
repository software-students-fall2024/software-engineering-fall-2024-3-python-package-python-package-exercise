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

    def __init__(self, name, pet_type):
        self.name = name
        self.type = pet_type.lower()
        self.emoji = self.PET_EMOJIS.get(self.type, '🐾')
        self.level = 1
        self.mood = "happy"
        self.hunger = 5 # 0 - 10