import random
from textwrap import dedent
import os
import time

# helper functions

# print animal
def get_animal(animal):
    if animal not in ["cat", "bunny", "elephant", "rabbit"]:
        print("No ASCII art available for " + animal + ". Please choose from:\n'cat'\n'bunny'\n'elephant'\n'rabbit")
        return ""
    
    if (animal == "cat"):
        output = dedent(r"""
          _
         | |__               /\__/\
         |__  |             ( o . o) 
            | |_____________ > ^ <
            |                  /
             /  ___________   /
            /_/             \_\
        """)
    elif (animal == "bunny"):
        output = dedent(r"""
              () ()
             ( 0x0 )
              (   ) 
              (")(")
        """)
    elif (animal == "elephant"):
        output = dedent(r"""
                 ____
        ________(     \––-     ♥
     /''         \ ,_ ,   • \  _
    /  |               \___ U /
    ^   \    ______    | 
        |_,,|      |_,,|
        """)
    elif (animal == "rabbit"):
        output = dedent(r"""
            ,\\
              \\\,_
               \` ,\\
          __,.-" =__)
        ."        )
     ,_/   ,    \/\_
     \_|    )_-\ \_-`
        `-----` `--`
        """)
    # default (no animal entered from our list)
    else:
        return ""
    
    return output

# print animal emoji
def get_animal_emoji(animal):
    animal_emojis = {
        "cat": "🐈",
        "bunny": "🐰",
        "elephant": "🐘",
        "rabbit": "🐇"
    }
    return animal_emojis[animal]

# print out fact for chosen animal
def print_fact():
    fact = get_random_fact(animal)
    print(f"\nRandom Fact: {fact}\n")

# get random message for animal
def get_random_fact(animal):
    animalFacts = {
        "cat": [
            "Did you know domestic cats can run up to 30 mph in short bursts?",
            "Did you know a group of cats is called a clowder?",
            "Did you know cats sleep for about 13-16 hours a day?"
        ],

        "elephant": [
            "Did you know an elephant's trunk has more than 40,000 muscles?",
            "Did you know that elephants are the largest land animals on Earth?",
            "Did you know elephants can recognize themselves in a mirror, showing signs of self-awareness?"
        ],

        "bunny": [
            "Did you know people often call pet rabbits bunnies because it makes them seem more approachable and cute?",
            "Did you know the Easter Bunny tradition dates back to the 1700s, originating from German folklore?",
            "Did you know bunnies are often featured in folklore and children's stories as symbols of fertility and spring"
        ],

        "rabbit": [
            "Did you know a rabbit's ears help regulate body temperature, especially in warm climates?",
            "Did you know a rabbits' teeth never stop growing, unlike human teeth?",
            "Did you know rabbits are social and should ideally be adopted in pairs?"
        ]
    }
    fact = animalFacts.get(animal)
    return random.choice(fact)

# primary functions

# move()
def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def move(animalText):
    spaces = 0
    try:
        while spaces < 50:
            clearScreen()
            for line in animalText.split('\n'):
                print(" " * spaces + line)
            time.sleep(0.1)
            spaces += 2
            
    except KeyboardInterrupt:
        clearScreen()
        print("\nAnimation stopped.")

# for debugging purposes
if __name__ == "__main__":
    animal = input("Enter an animal (cat, bunny, elephant, rabbit): ").strip().lower()
    animalText = get_animal(animal)
    
    if animalText == "":
        exit()
    else:
        try:
            move(animalText)
            print_fact()
        except ValueError as e:
            print(e)