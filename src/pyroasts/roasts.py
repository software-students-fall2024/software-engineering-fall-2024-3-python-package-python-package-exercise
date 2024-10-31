import random
#----------------------------------------------------------------------------------------------------------------------------------

# returns a personalized roast given a name and severity level.
def personal_roast(name: str, severity: int) -> str:
    
    name = name.lower().capitalize()
    
    roasts = {
        1: f"{name}, you're like a Monday morning — nobody likes you, we put up with you.",
        2: f"{name}, if you were any more average, you'd be a mean.",
        3: f"{name}, I'd explain how awful you are, but it's more fun to watch you figure it out.",
        4: f"{name}, you're the reason we can't have nice things.",
        5: f"{name}, even your reflection is disappointed when it sees you."
    }
    
    # return a default roast if severity value not found in dictionary.
    return roasts.get(severity, f"{name}, you're so bland that even a salt shaker thinks you're boring.")

#----------------------------------------------------------------------------------------------------------------------------------

# returns a roast for an inputted skill and degree of sarcasm
def skill_roast(skill: str, sarcasm_level: int) -> str:
    
    if sarcasm_level == 2:
        skill = skill.lower().capitalize()
    else:
        skill = skill.lower()
    
    roasts = {
        1: f"Your {skill} skills are like a WiFi signal in the middle of nowhere — nonexistent.",
        2: f"{skill}... You're joking right?",
        3: f"I've seen toddlers with better {skill} skills than you... and they can't even talk."
    }
    
    # return a default roast if sarcasm_level not found in dictionary.
    return roasts.get(sarcasm_level, f"Your {skill} skills are a whole new level of disappointment.")

#----------------------------------------------------------------------------------------------------------------------------------

# returns a roast for choosing one thing over another.
def comparison_roast(thing1: str, thing2: str) -> str:
    
    thing1 = thing1.lower().capitalize()
    thing2 = thing2.lower()
    
    roasts = [
        f"{thing1} instead of {thing2}? I'd rather sit on a cactus.",
        f"{thing1} over {thing2}? I'd rather star in a documentary called 'How Far Can the Human Body be Stretched'.",
        f"{thing1} over {thing2}? I'd rather step on a LEGO."
    ]
    
    # return a randomly selected roast from the list.
    return random.choice(roasts)

#----------------------------------------------------------------------------------------------------------------------------------

# returns a roast that gives sarcastic advice based on given topic and sarcasm level.
def advice_roast(topic: str, sarcasm_level: int) -> str:
    
    topic = topic.lower()
    
    roasts = {
        1: f"Trying to learn {topic}? Just keep doing the bare minimum, I'm sure it'll work out... somehow.",
        2: f"Your attempt at {topic} is so inspiring, it's a shame nobody's watching.",
        3: f"Maybe if you spent half as much time on {topic} as you do scrolling on social media, you'd actually get somewhere."
    }
    
    # return a default roast if sarcasm_level not found in dictionary.
    return roasts.get(sarcasm_level, f"You call that effort in {topic}? I've seen potatoes put in more work.")

#----------------------------------------------------------------------------------------------------------------------------------
"""
Inspiration for many of the "roasts"
https://markkuperala.com/wp-content/uploads/2024/05/A-List-of-Funny-Insults.pdf
https://aok.heavengames.com/cgi-bin/forums/display.cgi?action=st&fn=22&tn=33840&st=25
"""
from helper import generic_roasts, names, roast_templates
def get_roast():
    """
    Get a single random roast from the list of roasts
    """
    return random.choice(generic_roasts)

def get_n_names(n=2):
    """
    Get n random insulting names from the list of insulting names
    """
    return [name.lower() for name in random.sample(names, min(n, len(names)))]

def get_roast_template():
    """
    Get a single random roast template from the list of roast templates
    """
    return random.choice(roast_templates)

def roast(mode=1):
    """
    Generate a roast given the desired mode of roasting selected
    """
    if mode == 1:
        return get_roast()
    else:
        return get_roast_template().format(*get_n_names(10))
    
## example for how to test these out
# for i in range(10):
#     print(roast(1))
#     print(roast(2))


#----------------------------------------------------------------------------------------------------------------------------------