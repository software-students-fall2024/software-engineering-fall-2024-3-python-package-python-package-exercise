from provide_hint import provide_hint
import pytest
from generate_riddle import generate_riddle
from check_answer import check_answer
from read_file import read_file
from submit_riddle import submit_riddle
import json

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
def test_hint_valid_id(riddles):
    print("Hint Test valid ID:")
    result = provide_hint(90, riddles) 
    print(result)
    assert "Hint:" in result, "Failed: Valid ID should return a hint."

def test_hint_invalid_input(riddles):
    print("Hint Test invalid input:")
    result = provide_hint("abc", riddles) 
    print(result)
    assert "Error: Invalid input" in result, "Failed: Non-integer input should return an error."

def test_hint_nonexistent_id(riddles):
    print("Hint Test nonexistent ID:")
    result = provide_hint(999, riddles)  
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
def test_correct_answer(riddles):
    print("test correct answer")
    for riddle in riddles:
        if 1 <= riddle["id"] <= 100:
            result = check_answer(riddle["id"], riddle["answer"][0], riddles)
            assert "Correct answer!" in result, f"Test fails for {riddle['id']}"

def test_incorrect_answer(riddles):
    for riddle in riddles:
        if 1 <= riddle["id"] <= 100:
            result = check_answer(riddle["id"], "incorrect answer", riddles)
            assert "Incorrect answer. Try again!" in result, f"Test fails for {riddle['id']}."

def test_case_insensitive_answer(riddles):
    for riddle in riddles:
        if 1 <= riddle["id"] <= 100:
            result = check_answer(riddle["id"], riddle["answer"][0].upper(), riddles)
            print(result)
            assert "Correct answer!" in result, f"test fails for {riddle['id']}"
'''


# Check answer tests
def test_correct_answer_for_id_range_26_50(riddles):
    print("Test correct answer")
    for riddle in riddles:
        if 26 <= riddle["id"] <= 50:
            result = check_answer(riddle["id"], riddle["answer"][0], "riddleLibrary.json")
            print(result)
            assert "Correct answer!" in result, f"Test fails for {riddle['id']}"

def test_incorrect_answer_for_id_range_26_50(riddles):
    print("Test incorrect answer for id range 26-50")
    for riddle in riddles:
        if 26 <= riddle["id"] <= 50:
            result = check_answer(riddle["id"], "incorrect answer", "riddleLibrary.json")
            print(result)
            assert "Incorrect answer. Try again!" in result, f"Test fails for {riddle['id']}。"

def test_case_insensitive_answer_for_id_range_26_50(riddles):
    print("Test case insensitive")
    for riddle in riddles:
        if 26 <= riddle["id"] <= 50:
            result = check_answer(riddle["id"], riddle["answer"][0].upper(), "riddleLibrary.json")
            print(result)
            assert "Correct answer!" in result, f"Test fails for {riddle['id']}"


# submit riddle tests
def test_valid_riddle(riddles):
    print("Test valid riddle:")
    riddle = {"question": "What has keys but can't open locks?", "answer": ["keyboard"], "hint": "Used to type on a computer.", "difficulty": 1, "topic": "Riddles"}
    result = submit_riddle(riddle, riddles)
    assert "Riddle submitted successfully!" in result, "Failed: Valid riddle should be submitted successfully."

def test_duplicate_riddle(riddles):
    print("Test duplicate riddle:")
    result = submit_riddle(riddles[0], riddles)
    assert "Error: This riddle already exists in the library" in result, "Failed: Duplicate riddle should return an error."

def test_invalid_input(riddles):
    print("Test invalid input:")
    riddle = "abc"
    with pytest.raises(ValueError, match="Invalid input"):
        submit_riddle(riddle, riddles)

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
        with pytest.raises(ValueError, match="Riddle format is incorrect"):
            submit_riddle(riddle, riddles)

def test_invalid_riddle_format(tmp_path):
    print("Test invalid riddle format:")
    temp_file = tmp_path / "temp_riddleLibrary.json"
    test_riddles = [
        {"question": "What has keys but can't open locks?", "hint": "Used to type on a computer.", "difficulty": 1, "topic": "Riddles"},
        {"question": "What has keys but can't open locks?", "answer": "keyboard", "hint": "Used to type on a computer.", "difficulty": 1, "topic": "Riddles"},
        {"question": "What has keys but can't open locks?", "answer": ["keyboard"], "hint": "Used to type on a computer.", "difficulty": "easy", "topic": "Riddles"},
        {"question": "What has keys but can't open locks?", "answer": ["keyboard"], "hint": "Used to type on a computer.", "difficulty": 1},
        {"answer": ["keyboard"], "hint": "Used to type on a computer.", "difficulty": 1, "topic": "Riddles"}
    ]

    for riddle in test_riddles:
        result = submit_riddle(riddle, file_path=str(temp_file))
        print(result)
        assert "Riddle format is incorrect" in result, "Failed: Riddle format should be incorrect."
'''