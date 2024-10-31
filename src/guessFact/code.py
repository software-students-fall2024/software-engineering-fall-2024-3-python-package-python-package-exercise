"""This file should contains the code that will be implemented"""

def main_function() -> None:
    """the main function to implement the interaction with the user"""
    print("Welcome to the Guess the Fact Game!")
    print("In this game, you'll be presented with two statements about a chosen topic.")
    print("Your task is to guess which statement is true.")
    print("Let's get started")
    print("Please choose a category:")
    categories = {"1": "category1","2": "category2","3": "category3"}
    for key, value in categories.items():
        print(f"{key}: {value}")
    category_choice = input("Enter the number of your chosen category: ")
    while True:
        if category_choice_validation(category_choice):
            break
        category_choice = input("Please enter the number 1, 2, or 3 to choose the category").strip()
    print("Please choose a sub-category:")
    if category_choice=="1":
        sub_categories = {"1": "sub-category1","2": "sub-category2","3": "sub-category3"}
        for key, value in sub_categories.items():
            print(f"{key}: {value}")
        sub_choice = input("Enter the number of your chosen sub-category: ")
        while True:
            if category_choice_validation(sub_choice):
                break
            sub_choice = input(
                "Please enter the number 1, 2, or 3 to choose the sub-category").strip()
        category1(sub_choice)
    elif category_choice=="2":
        sub_categories = {"1": "sub-category1","2": "sub-category2","3": "sub-category3"}
        for key, value in sub_categories.items():
            print(f"{key}: {value}")
        sub_choice = input("Enter the number of your chosen sub-category: ")
        while True:
            if category_choice_validation(sub_choice):
                break
            sub_choice = input(
                "Please enter the number 1, 2, or 3 to choose the sub-category").strip()
        category2(sub_choice)
    else:
        sub_categories = {"1": "sub-category1","2": "sub-category2","3": "sub-category3"}
        for key, value in sub_categories.items():
            print(f"{key}: {value}")
        sub_choice = input("Enter the number of your chosen sub-category: ")
        while True:
            if category_choice_validation(sub_choice):
                break
            sub_choice = input(
                "Please enter the number 1, 2, or 3 to choose the sub-category").strip()
        category3(sub_choice)

def category_choice_validation(category_choice: str) -> bool:
    """the function the check whether the user enter a valid category choice: 
    true if valid, false otherwise"""
    return (category_choice in {"1","2","3"})

def category1(sub_choice: int) -> None:
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
    
    7. give a little bit explanation for both statements"""
    
    #below is just a placeholder
    print("category1 check")

def category2(sub_choice: int) -> None:
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
    
    7. give a little bit explanation for both statements"""
    
    #below is just a placeholder
    print("category2 check")

def category3(sub_choice: int) -> None:
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
    
    7. give a little bit explanation for both statements"""
    
    #below is just a placeholder
    print("category3 check")

def fact_choice_validation(fact_choice: str) -> bool:
    """the function the check whether the user enter a valid fact choice: 
    true if valid, false otherwise"""
    return (fact_choice in {"1","2"})
