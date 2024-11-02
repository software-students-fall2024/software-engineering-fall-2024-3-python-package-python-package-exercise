import random
"""This file should contains the code that will be implemented"""

def main_function() -> None:
    """the main function to implement the interaction with the user"""
    print("Welcome to the Guess the Fact Game!")
    print("In this game, you'll be presented with two statements about a chosen topic.")
    print("Your task is to guess which statement is true.")
    print("Let's get started")
    print("Please choose a category:")
    categories = {"1": "Music","2": "Coffee","3": "Food"}
    for key, value in categories.items():
        print(f"{key}: {value}")
    category_choice = input("Enter the number of your chosen category: ")
    while True:
        if category_choice_validation(category_choice):
            break
        category_choice = input("Please enter the number 1, 2, or 3 to choose the category").strip()
    print("Please choose a sub-category:")
    if category_choice=="1":
        sub_categories = {"1": "Classical","2": "Jazz","3": "Pop"}
        for key, value in sub_categories.items():
            print(f"{key}: {value}")
        sub_choice = input("Enter the number of your chosen sub-category: ")
        while True:
            if category_choice_validation(sub_choice):
                break
            sub_choice = input(
                "Please enter the number 1, 2, or 3 to choose the sub-category").strip()
        Music(sub_choice)
    elif category_choice=="2":#historical tales; coffee culture; scientific facts
        sub_categories = {"1": "historical tales","2": "coffee culture","3": "scientific facts"}
        for key, value in sub_categories.items():
            print(f"{key}: {value}")
        sub_choice = input("Enter the number of your chosen sub-category: ")
        while True:
            if category_choice_validation(sub_choice):
                break
            sub_choice = input(
                "Please enter the number 1, 2, or 3 to choose the sub-category").strip()
        Coffee(sub_choice)
    else: # Food category
        sub_categories = {"1": "Desserts","2": "International Cuisines","3": "Street Food"}
        for key, value in sub_categories.items():
            print(f"{key}: {value}")
        sub_choice = input("Enter the number of your chosen sub-category: ")
        while True:
            if category_choice_validation(sub_choice):
                break
            sub_choice = input(
                "Please enter the number 1, 2, or 3 to choose the sub-category").strip()
        Food(sub_choice)

def category_choice_validation(category_choice: str) -> bool:
    """the function the check whether the user enter a valid category choice: 
    true if valid, false otherwise"""
    return (category_choice in {"1","2","3"})

def Music(sub_choice: int) -> None:
    """argument: sub_choice (int), which will be 1, 2, or 3
    
    the function should do the following:
    
    1. store the two groups of statements 
    (one fact & one fabrication + another fact & another fabrication) 
    and their corresponding explanations
    
    2. randomly print one group to user, which will be two statements
    
    3. prompt user to enter 1 or 2 to choose the fact
    
    4. use while loop and fact_choice_validation function below to prompt again 
    until the fact_choice is valid
    
    5. check whether the user's answer correct
    
    6. tell the user whether she/he is correct or not
    
    7. give a little bit explanation for both statements
    
    8. write >= 3 tests for this function in the test_code.py"""

    facts = {
        1: [
            "Fact 1: Beethoven continued to compose even after he lost his hearing.\nFact 2: Wolfgang Amadeus Mozart wrote over 1,000 symphonies in his lifetime.\n",
            "Fact 1: Frédéric Chopin was known for his operas and symphonies.\nFact 2: Johann Sebastian Bach had 20 children.\n"
        ],
        2: [
            "Fact 1: Louis Armstrong’s influential trumpet playing helped shape modern jazz.\nFact 2: Jazz originated in London during the 19th century.\n",
            "Fact 1: Duke Ellington was primarily known as a classical pianist and rarely performed jazz.\nFact 2: Louis Armstrong, one of the most influential figures in jazz, was also known for his distinctive gravelly voice and popularized scat singing.\n"
        ],
        3: [
            "Fact 1: Michael Jackson’s album Thriller is the best-selling album of all time.\nFact 2: The Rolling Stones were originally known as The Blueberries.\n",
            "Fact 1: The Beatles were the first band to perform on the moon.\nFact 2: The Beatles were originally known as The Quarrymen.\n"
        ]
    }

    truths = {
        1: [ 1, 1 ],
        2: [ 1, 2 ],
        3: [ 1, 2 ]
    }

    explanations = {
        1: ["Beethoven composed the moonlight sonata after his loss of hearing.", "Chopin was known primarily for his piano compositions, not his symphony work."],
        2: ["Armstrongs influence on jazz extends even to today.", "Armstrongs distinctive singing captured the attention of audiences country wide."],
        3: ["Michael Jacksons album hit the best sellers list at the time.", "The beatles were not the first band to perform on the moon."]
    }

    sub_choice = int(sub_choice)
    
    statements = facts[sub_choice]
    statementIndex = random.randint(0, 1)
    selected_statement = statements[statementIndex]

    while True:
        choice = input("Which of the following statements is true? Please enter 1 or 2:\n" + selected_statement)
        if fact_choice_validation(choice):
            break
        print("Invalid choice. Please enter either 1 or 2.")

    if int(choice) == truths[sub_choice][statementIndex]:
        print("You are right!")
    else:
        print("You are wrong!")

    print("Explanation: " + explanations[sub_choice][statementIndex])

def Coffee(sub_choice: int) -> None:

    #subcategories: 1.historical tales; 2.coffee culture; 3.scientific facts
    """
    1.1.
        1.According to legend, coffee was coffee was discovered when a goat herder noticed his goats’ energy after eating coffee berries
        2.In 15th-century Yemen, coffee beans were so valuable that merchants would trade them for gemstones.
    1.2
        1.In medieval Ethiopia, coffee was once taxed under a 'wakefulness tax'
        2.The Arabic root word for coffe -- qahwa -- originally refered to a type of wine
    2.1
        1.According to global trade data, coffee is indeed one of the most traded commodities, second only to oil
        2.2.In a remote mountain village in Nepal, monks practice “coffee meditation
    2.2
        1.Finland consistently ranks first in coffee consumption per capita
        2.In a small town in France, it’s customary to clink coffee mugs before every sip. Local folklore says it helps people “toast” the spirit of the coffee bean for good energy
    3.1
        1.In the highlands of Peru, there is a rare coffee plant that only blooms at midnight on full moons, releasing an unusually sweet aroma. The coffee from these “Lunar Beans” is said to have a mellow, caramel flavor
        2.Coffee is one of the richest sources of antioxidants in the average diet, even more than some fruits and vegetables
    3.2
        1.Studies have found that just holding a warm cup of coffee can affect your perception and behavior.
        2.In a lab experiment, researchers in Iceland developed coffee beans that change color according to the drinker’s mood. These “Mood Beans” are still in development but are said to go from green (calm) to red (excited) as you take a sip

    """

    facts = ["1.According to legend, coffee was coffee was discovered when a goat herder noticed his 'goats' energy after eating coffee berries"\
            "\n2.In 15th-century Yemen, coffee beans were so valuable that merchants would trade them for gemstones", 

            "1.In medieval Ethiopia, coffee was once taxed under a 'wakefulness tax'"\
            "\n2.The Arabic root word for coffe -- qahwa -- originally refered to a type of wine", 

            "1.According to global trade data, coffee is indeed one of the most traded commodities, second only to oil”\
            \n2.In a remote mountain village in Nepal, monks practice “coffee meditation", 
            
            "1.Finland consistently ranks first in coffee consumption per capita"\
            "\n2.In a small town in France, it’s customary to clink coffee mugs before every sip. Local folklore says it helps people “toast” the spirit of the coffee bean for good energy", 
            
            "1.In the highlands of Peru, there is a rare coffee plant that only blooms at midnight on full moons, releasing an unusually sweet aroma. The coffee from these “Lunar Beans” is said to have a mellow, caramel flavor"\
            "\n2.Coffee is one of the richest sources of antioxidants in the average diet, even more than some fruits and vegetables", 
            
            "1.Studies have found that just holding a warm cup of coffee can affect your perception and behavior."\
            "\n2.In a lab experiment, researchers in Iceland developed coffee beans that change color according to the drinker’s mood. These “Mood Beans” are still in development but are said to go from green (calm) to red (excited) as you take a sip"]
    explanation = ["11", "12", "21", "22", "31", "32"]
    truth = [1, 2, 1, 1, 2, 1]
    
    #randomly generate 0 or 1
    random_value = int(__import__('time').time() * 1000) % 2

    sub_choice = int(sub_choice)
    #print facts
    print(facts[(sub_choice -1)*2+random_value])

    while True:
        fact_choice = input("Which fun fact do you think is true? Please type 1 or 2: ")
        if fact_choice_validation(fact_choice):
            break
        fact_choice = input("Invalid input. Please enter either 1 or 2.").strip()

    if fact_choice == truth[sub_choice + random_value]:
        print("You are right!")
    else:
        print("You are wrong!")
        
    #below is just a placeholder
    print("category2 check")

def Food(sub_choice: int) -> None:
    """argument: sub_choice (int), which will be 1, 2, or 3
    
    the function should do the following:
    
    1. store the two groups of statements 
    (one fact & one fabrication + another fact & another fabrication) 
    and their corresponding explanations
    
    2. randomly print one group to user, which will be two statements
    
    3. prompt user to enter 1 or 2 to choose the fact
    
    4. use while loop and fact_choice_validation function below to prompt again 
    until the fact_choice is valid
    
    5. check whether the user's answer correct
    
    6. tell the user whether she/he is correct or not
    
    7. give a little bit explanation for both statements
    
    8. write >= 3 tests for this function in the test_code.py"""
    
    #below is just a placeholder
    print("category3 check")

def fact_choice_validation(fact_choice: str) -> bool:
    """the function the check whether the user enter a valid fact choice: 
    true if valid, false otherwise"""
    return (fact_choice in {"1","2"})
