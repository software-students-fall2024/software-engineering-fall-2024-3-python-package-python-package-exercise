import pytest
import json
import random
from src.provide_hint import provide_hint
from src.generate_riddle import generate_riddle
from src.check_answer import check_answer
from src.read_file import read_file
from src.submit_riddle import submit_riddle

@pytest.fixture
def riddles():
    riddles = read_file("riddleLibrary.json")
    return riddles

# Read file tests
def test_read_file_success(tmp_path):
    file_path = tmp_path / "riddleLibrary.json"
    data = [{"id": 1, "question": "Sample Question", "answer": ["Sample Answer"], "hint": "Sample Hint", "difficulty": 1}]
    file_path.write_text(json.dumps(data))
    
    result = read_file(file_path)
    assert result == data, "Failed: Expected data to be correctly read."

def test_read_file_not_found():
    result = read_file("non_existent_file.json")
    assert result == [], "Failed: Expected an empty list for a non-existent file."

def test_read_file_json_decode_error(tmp_path):
    file_path = tmp_path / "invalid_riddleLibrary.json"
    file_path.write_text("{invalid json}")  

    result = read_file(file_path)
    assert result == [], "Failed: Expected an empty list for a JSON decode error."

# Hint tests
def test_hint_valid_id():
    print("Hint Test valid ID:")
    result = provide_hint(90) 
    print(result)
    assert "Hint:" in result, "Failed: Valid ID should return a hint."

def test_hint_invalid_input():
    print("Hint Test invalid input:")
    result = provide_hint("abc") 
    print(result)
    assert "Error: Invalid input" in result, "Failed: Non-integer input should return an error."

def test_hint_nonexistent_id():
    print("Hint Test nonexistent ID:")
    result = provide_hint(999)  
    print(result)
    assert "Error: Riddle ID not found" in result, "Failed: Nonexistent ID should return an error."

#Generate riddle tests
def test_generate_input_type():
    print("Start test generate input")
    with pytest.raises(TypeError):
        generate_riddle("string")
    with pytest.raises(ValueError):
        generate_riddle(-1)
    with pytest.raises(ValueError):
        generate_riddle(5)

def test_generate_correctness(riddles):
    print("Start test generate correctness")
    def find_question_diff(question: str):
        for riddle in riddles:
            if riddle['question'] == question:
                return riddle['difficulty']
        return -1
    
    assert find_question_diff(generate_riddle(1)) == 1
    assert find_question_diff(generate_riddle(2)) == 2
    assert find_question_diff(generate_riddle(3)) == 3
    assert find_question_diff(generate_riddle(4)) == 4


def test_generate_output_type():
    print("Start test generate output")
    assert type(generate_riddle(1)) is str
    assert type(generate_riddle(2)) is str
    assert type(generate_riddle(3)) is str
    assert type(generate_riddle(4)) is str

#check answer tests
def test_correct_answer():
    print("test correct answer")
    riddles = read_file("riddleLibrary.json")
    for riddle in riddles:
        if 1 <= riddle["id"] <= 100:
            result = check_answer(riddle["id"], riddle["answer"][0])
            assert "Correct answer!" in result, f"Test fails for {riddle['id']}"

def test_incorrect_answer():
    riddles = read_file("riddleLibrary.json")
    for riddle in riddles:
        if 1 <= riddle["id"] <= 100:
            result = check_answer(riddle["id"], "incorrect answer")
            assert "Incorrect answer. Try again!" in result, f"Test fails for {riddle['id']}."

def test_case_insensitive_answer():
    riddles = read_file("riddleLibrary.json")
    for riddle in riddles:
        if 1 <= riddle["id"] <= 100:
            result = check_answer(riddle["id"], riddle["answer"][0].upper())
            print(result)
            assert "Correct answer!" in result, f"test fails for {riddle['id']}"

# submit riddle tests
def test_valid_riddle(file_path="riddleLibrary.json"):
    print("Test valid riddle:")
    riddle = {
        "question": "I swing through trees and chatter all day. I love bananas and in the jungle I play. What am I?",
        "answer": ["monkey"],
        "hint": "I am often seen hanging from branches and love to mimic sounds.",
        "difficulty": 1,
        "topic": "Animals"
    }
    
    result = submit_riddle(riddle)
    print(result)
    assert "Riddle submitted successfully" in result, "Failed: Valid riddle should be submitted successfully."
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    if riddle in data:
        data.remove(riddle)
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def test_duplicate_riddle():
    print("Test duplicate riddle:")
    riddles = read_file("riddleLibrary.json")
    # Select a random riddle from the library
    random_riddle = riddles[random.randint(0, len(riddles) - 1)]
    # submit duplicated riddle
    result = submit_riddle(random_riddle)
    print(result)
    assert "Error: This riddle already exists in the library" in result, "Failed: Duplicate riddle should return an error."

def test_invalid_input():
    print("Test invalid input:")
    riddle = "abc"
    result = submit_riddle(riddle)
    print(result)
    assert "Error: Invalid input" in result, "Failed: Non-dictionary input should return an error."

def test_invalid_riddle_format():
    print("Test invalid riddle format:")
    test_riddles = [
        {"question": "What has keys but can't open locks?", "hint": "Used to type on a computer.", "difficulty": 1, "topic": "Riddles"},
        {"question": "What has keys but can't open locks?", "answer": "keyboard", "hint": "Used to type on a computer.", "difficulty": 1, "topic": "Riddles"},
        {"question": "What has keys but can't open locks?", "answer": ["keyboard"], "hint": "Used to type on a computer.", "difficulty": "easy", "topic": "Riddles"},
        {"question": "What has keys but can't open locks?", "answer": ["keyboard"], "hint": "Used to type on a computer.", "difficulty": 1},
        {"answer": ["keyboard"], "hint": "Used to type on a computer.", "difficulty": 1, "topic": "Riddles"}
    ]

    for riddle in test_riddles:
        result = submit_riddle(riddle)
        print(result)
        assert "Error: Riddle format is incorrect" in result, "Failed: Riddle format should be incorrect."

def test_invalid_riddle_format(riddles):
    print("Test invalid riddle format:")
    test_riddles = [
        {"question": "What has keys but can't open locks?", "hint": "Used to type on a computer.", "difficulty": 1, "topic": "Riddles"},
        {"question": "What has keys but can't open locks?", "answer": "keyboard", "hint": "Used to type on a computer.", "difficulty": 1, "topic": "Riddles"},
        {"question": "What has keys but can't open locks?", "answer": ["keyboard"], "hint": "Used to type on a computer.", "difficulty": "easy", "topic": "Riddles"},
        {"question": "What has keys but can't open locks?", "answer": ["keyboard"], "hint": "Used to type on a computer.", "difficulty": 1},
        {"answer": ["keyboard"], "hint": "Used to type on a computer.", "difficulty": 1, "topic": "Riddles"}
    ]

    for riddle in test_riddles:
        result = submit_riddle(riddle)
        print(result)
        assert "Error: Riddle format is incorrect" in result, "Failed: Riddle format should be incorrect."