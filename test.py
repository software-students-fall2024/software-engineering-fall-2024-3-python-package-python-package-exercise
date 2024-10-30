from provide_hint import provide_hint
import pytest
from generate_riddle import generate_riddle
from check_answer import check_answer
from read_file import read_file
from submit_riddle import submit_riddle
import json

#generate hint tests
def test_valid_id():
    print("Test valid ID:")
    result = provide_hint(90,"riddleLibrary.json") 
    print(result)
    assert "Hint:" in result, "Failed: Valid ID should return a hint."

def test_invalid_input():
    print("Test invalid input:")
    result = provide_hint("abc","riddleLibrary.json") 
    print(result)
    assert "Error: Invalid input" in result, "Failed: Non-integer input should return an error."

def test_nonexistent_id():
    print("Test nonexistent ID:")
    result = provide_hint(999,"riddleLibrary.json")  
    print(result)
    assert "Error: Riddle ID not found" in result, "Failed: Nonexistent ID should return an error."

#generate riddle tests
def test_generate_input_type():
    print("Start test generate input")
    with pytest.raises(TypeError):
        generate_riddle("string")
    with pytest.raises(ValueError):
        generate_riddle(-1)
    with pytest.raises(ValueError):
        generate_riddle(5)

def test_generate_correctness():
    # Mock??? 
    print("Start test generate correctness")
    def find_question_diff(question: str):
        with open("riddleLibrary.json", 'r') as file:
            riddles = json.load(file)
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
def test_correct_answer_for_id_range_26_50():
    print("test correct answer")
    for riddle in riddles:
        if 26 <= riddle["id"] <= 100:
            result = check_answer(riddle["id"], riddle["answer"][0], FILE_PATH)
            assert "Correct answer!" in result, f"Test fails for {riddle['id']}"

def test_incorrect_answer(riddles):
    for riddle in riddles:
        if 26 <= riddle["id"] <= 100:
            result = check_answer(riddle["id"], "incorrect answer", FILE_PATH)
            assert "Incorrect answer. Try again!" in result, f"Test fails for {riddle['id']}."

def test_case_insensitive_answer(riddles):
    for riddle in riddles:
        if 26 <= riddle["id"] <= 50:
            result = check_answer(riddle["id"], riddle["answer"][0].upper(), "riddleLibrary.json")
            print(result)
            assert "Correct answer!" in result, f"test fails for {riddle['id']}"

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

if __name__ == "__main__":
    riddles = read_file("riddleLibrary.json")

    #generate riddle tests
    test_generate_input_type() # 拆成 3 个 # return string #在test里面核对 # 使用统一接口
    test_generate_output_type()
    test_generate_correctness()

    #check answer tests
    test_correct_answer_for_id_range_26_50() # riddles 应该passed as argument
    test_incorrect_answer_for_id_range_26_50() # 应该test全部
    test_case_insensitive_answer_for_id_range_26_50()

    #submit riddle test
    test_valid_riddle(riddles) # riddles 应该passed as argument
    test_duplicate_riddle(riddles) 
    test_invalid_input(riddles) # 针对重复riddles进行识别
    test_invalid_riddle_format(riddles)

    #generate hint tests
    test_valid_id() # riddles 应该passed as argument
    test_invalid_input() # 生成readfile的test， 使用pytest
    test_nonexistent_id()

#把test都变成pytest
    print("All tests completed.")