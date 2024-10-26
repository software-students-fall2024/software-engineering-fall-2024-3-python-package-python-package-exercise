import random
from textwrap import dedent

# helper functions

# print animal
def print_animal(animal):
    if (animal == "cat"):
        output = dedent(
        """
          _
         | |__			  /\__/\
         |__  |			 ( o . o) 
            | |___________ > ^ < 
            |   		      /
             /  ___________  \
            /_/			    \_\
         """
        )
    #replace with other animal
    elif (animal == "bunny"):
        output = dedent(
        """
              () ()
             ( 0x0 )
              (   ) 
              (")(")
        """
        )
    #replace with other animal
    elif (animal == "elephant"):
        output = dedent(
        """
                 ____
        ________(     \––-  ♥
     /''         \ ,_ ,   • \  _
    /  |               \___ U /
    ^   \    ______    | 
        |_,,|      |_,,|
        """
        )
    #replace with other animal
    elif (animal == "dog"):
        output = dedent(
        """
       \   ^__^
        \  (oo)\_______
           (__)\       )\/\\
               ||----w |
               ||     ||
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