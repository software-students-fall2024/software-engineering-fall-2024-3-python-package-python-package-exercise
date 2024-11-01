import pytest
from src.guessFact.code import main_function, category_choice_validation, fact_choice_validation

#Test for main_function
def test_main_function_case1(monkeypatch: pytest.MonkeyPatch, capfd: pytest.CaptureFixture) -> None:
    inputs = iter(["1","1"])
    monkeypatch.setattr("builtins.input",lambda _: next(inputs))
    main_function()
    captured = capfd.readouterr()
    expected_output_segments = [
        "Welcome to the Guess the Fact Game!",
        "In this game, you'll be presented with two statements about a chosen topic.",
        "Your task is to guess which statement is true.",
        "Let's get started",
        "Please choose a category:",
        "1: Music",
        "2: category2",
        "3: category3",
        "Please choose a sub-category:",
        "1: Classical",
        "2: Jazz",
        "3: Pop"
    ]
    output = captured.out
    for segment in expected_output_segments:
        assert segment in output

def test_main_function_case2(monkeypatch: pytest.MonkeyPatch, capfd: pytest.CaptureFixture) -> None:
    inputs = iter(["4","1","a","1"])
    monkeypatch.setattr("builtins.input",lambda _: next(inputs))
    main_function()
    captured = capfd.readouterr()
    expected_output_segments = [
        "Welcome to the Guess the Fact Game!",
        "In this game, you'll be presented with two statements about a chosen topic.",
        "Your task is to guess which statement is true.",
        "Let's get started",
        "Please choose a category:",
        "1: Music",
        "2: category2",
        "3: category3",
        "Please choose a sub-category:",
        "1: Classical",
        "2: Jazz",
        "3: Pop"
    ]
    output = captured.out
    for segment in expected_output_segments:
        assert segment in output

def test_main_function_case3(monkeypatch: pytest.MonkeyPatch, capfd: pytest.CaptureFixture) -> None:
    inputs = iter(["1","3"])
    monkeypatch.setattr("builtins.input",lambda _: next(inputs))
    main_function()
    captured = capfd.readouterr()
    expected_output_segments = [
        "Welcome to the Guess the Fact Game!",
        "In this game, you'll be presented with two statements about a chosen topic.",
        "Your task is to guess which statement is true.",
        "Let's get started",
        "Please choose a category:",
        "1: Music",
        "2: category2",
        "3: category3",
        "Please choose a sub-category:",
        "1: Classical",
        "2: Jazz",
        "3: Pop"
    ]
    output = captured.out
    for segment in expected_output_segments:
        assert segment in output

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