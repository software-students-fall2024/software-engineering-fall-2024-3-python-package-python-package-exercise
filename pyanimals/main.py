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
               \` ,\
          __,.-" =__)
        ."        )
     ,_/   ,    \/\_
     \_|    )_-\ \_-`
        `-----` `--`
        """
        )
    # default (no animal entered from our list)
    else:
        output = ""
    
    return output

# print message
# def print_message(message):

# get random message from list
def get_random_message(messages):
    return random.choice(messages)

# primary functions
# move()
def clearScreen():
    # for macOS/linux
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:                # For macOS/Linux
        os.system('clear')

def move(animal):
    availableAnimals = ["cat", "bunny", "elephant", "dog"]
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
    animal = input("Enter an animal (cat, bunny, elephant): ").strip().lower()
    try:
        move(animal)
    except ValueError as e:
        print(e)