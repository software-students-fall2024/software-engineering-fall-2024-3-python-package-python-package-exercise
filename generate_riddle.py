import json
import random


def generate_riddle(difficulty: int) -> dict:
    if type(difficulty) is not int:
        raise TypeError("Difficulty should be an integer.")
    if difficulty < 1 or difficulty > 4:
        raise ValueError("Difficulty should be between 1 and 4.")

    with open('./riddleLibrary.json', 'r') as file:
        riddle_lib = json.load(file)

    riddles = []
    for riddle in riddle_lib:
        if riddle['difficulty'] == difficulty:
            riddles.append(riddle)

    random_element = random.choice(riddles)
    return random_element


# print(generate_riddle(4))
