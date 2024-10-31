from src.guessFact.code import main_function, category_choice_validation, fact_choice_validation

#Test for fact_choice_validation function
def test_fact_choice_validation_case1() -> None:
    assert fact_choice_validation("1") == True

def test_fact_choice_validation_case2() -> None:
    assert fact_choice_validation("2") == True
    
def test_fact_choice_validation_case3() -> None:
    assert fact_choice_validation(" 2") == False
    
def test_fact_choice_validation_case4() -> None:
    assert fact_choice_validation(" ") == False

def test_fact_choice_validation_case5() -> None:
    assert fact_choice_validation("3") == False

#Test for category_choice_validation function
def test_category_choice_validation_case1() -> None:
    assert category_choice_validation("1") == True

def test_category_choice_validation_case2() -> None:
    assert category_choice_validation("2") == True
    
def test_category_choice_validation_case3() -> None:
    assert category_choice_validation("3") == True

def test_category_choice_validation_case4() -> None:
    assert category_choice_validation("") == False
    
def test_category_choice_validation_case5() -> None:
    assert category_choice_validation("1") == True
    
def test_category_choice_validation_case6() -> None:
    assert category_choice_validation("4") == False