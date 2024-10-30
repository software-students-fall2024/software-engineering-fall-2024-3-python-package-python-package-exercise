from provide_hint import provide_hint
import pytest
from generate_riddle import generate_riddle
from check_answer import check_answer
from read_file import read_file
from submit_riddle import submit_riddle

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

#geenrate riddle tests
def test_generate_riddle():
    assert generate_riddle(1)["difficulty"] == 1
    assert generate_riddle(2)["difficulty"] == 2
    assert generate_riddle(3)["difficulty"] == 3
    assert generate_riddle(4)["difficulty"] == 4
    assert type(generate_riddle(4)) is dict
    assert type(generate_riddle(4)['question']) is str
    with pytest.raises(TypeError):
        generate_riddle("string")
    with pytest.raises(ValueError):
        generate_riddle(-1)
    with pytest.raises(ValueError):
        generate_riddle(5)

#check answer tests
def test_correct_answer_for_id_range_26_50():
    print("test correct answer")
    for riddle in riddles:
        if 26 <= riddle["id"] <= 50:
            result = check_answer(riddle["id"], riddle["answer"][0], "riddleLibrary.json")
            print(result)
            assert "Correct answer!" in result, f"Test fails for {riddle['id']}"

def test_incorrect_answer_for_id_range_26_50():
    print("test incorrect answer for id range 26-50")
    riddles = read_file("riddleLibrary.json")
    for riddle in riddles:
        if 26 <= riddle["id"] <= 50:
            result = check_answer(riddle["id"], "incorrect answer", "riddleLibrary.json")
            print(result)
            assert "Incorrect answer. Try again!" in result, f"Test fails for {riddle['id']}。"

def test_case_insensitive_answer_for_id_range_26_50():
    print("test cases insentitive")
    riddles = read_file("riddleLibrary.json")
    for riddle in riddles:
        if 26 <= riddle["id"] <= 50:
            result = check_answer(riddle["id"], riddle["answer"][0].upper(), "riddleLibrary.json")
            print(result)
            assert "Correct answer!" in result, f"test fails for {riddle['id']}"

# submit riddle tests
def test_valid_riddle():
    print("Test valid riddle:")
    riddle = {"question": "What has keys but can't open locks?", "answer": ["keyboard"], "hint": "Used to type on a computer.", "difficulty": 1, "topic": "Riddles"}
    result = submit_riddle(riddle)
    print(result)
    assert "Riddle submitted successfully!" in result, "Failed: Valid riddle should be submitted successfully."

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

if __name__ == "__main__":
    riddles = read_file("riddleLibrary.json")

    #generate riddle tests
    test_generate_riddle() # 拆成 3 个 # return string #在test里面核对 # 使用统一接口

    #check answer tests
    test_correct_answer_for_id_range_26_50() # riddles 应该passed as argument
    test_incorrect_answer_for_id_range_26_50() # 应该test全部
    test_case_insensitive_answer_for_id_range_26_50()

    #submit riddle test
    test_valid_riddle() # riddles 应该passed as argument
    test_invalid_input() # 针对重复riddles进行识别
    test_invalid_riddle_format()

    #generate hint tests
    test_valid_id() # riddles 应该passed as argument
    test_invalid_input() # 生成readfile的test， 使用pytest
    test_nonexistent_id()


#把test都变成pytest
    print("All tests completed.")