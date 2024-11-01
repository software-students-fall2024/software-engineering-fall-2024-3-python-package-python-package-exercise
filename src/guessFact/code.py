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
    
    #below is just a placeholder
    print("category1 check")

def Coffee(sub_choice: int) -> None:

    #subcategories: 1.historical tales; 2.coffee culture; 3.scientific facts

    facts = ["truth\nlie", "lie\ntruth", "truth\nlie", "truth\nlie", "lie\ntruth", "truth\nlie"]
    explanation = ["11", "12", "21", "22", "31", "32"]
    truth = [1, 2, 1, 1, 2, 1]
    
    #randomly generate 0 or 1
    random_value = int(__import__('time').time() * 1000) % 2

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
