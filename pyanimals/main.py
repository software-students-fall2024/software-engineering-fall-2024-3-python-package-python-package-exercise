import random
from textwrap import dedent
import os
import time

# helper functions

# print animal
def get_animal(animal):
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
    #replace with other animal
    elif (animal == "bunny"):
        output = dedent(r"""
              () ()
             ( 0x0 )
              (   ) 
              (")(")
        """)
    #replace with other animal
    elif (animal == "elephant"):
        output = dedent(r"""
                 ____
        ________(     \––-  ♥
     /''         \ ,_ ,   • \  _
    /  |               \___ U /
    ^   \    ______    | 
        |_,,|      |_,,|
        """)
    #replace with other animal
    elif (animal == "dog"):
        output = dedent("""
       \   ^__^
        \  (oo)\_______
           (__)\       )\/\\
               ||----w |
               ||     ||
        """)
    elif (animal == "rabbit"):
        output = dedent(
        """
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
        output = ""
    
    return output

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

        "dog": [
            "Did you know that dogs can be trained to detect diseases like cancer?",
            "Did you know that a dog's nose print is as unique as a human fingerprint?",
            "Did you know that dogs have about 18 muscles controlling their ears."
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
    # for macOS/linux
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:                # For macOS/Linux
        os.system('clear')

def move(animal):
    availableAnimals = ["cat", "bunny", "elephant", "dog", "rabbit"]
    if animal not in availableAnimals:
        raise ValueError("Invalid animal!")
    
    animalText = get_animal(animal)
    if not animalText:
        print("No ASCII art available for this animal.")
        return
    
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
    animal = input("Enter an animal (cat, bunny, elephant, dog, rabbit): ").strip().lower()
    try:
        move(animal)
        print_fact()
    except ValueError as e:
        print(e)