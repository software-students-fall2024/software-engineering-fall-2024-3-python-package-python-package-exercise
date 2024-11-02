import random

fortunes = [
    "You will have a great day!",
    "You will find love soon.",
    "You will win the lottery.",
    "You will ace that test.",
]

def get_fortune():
    return random.choice(fortunes)
