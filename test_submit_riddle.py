from submit_riddle import submit_riddle

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
    test_valid_riddle()
    test_invalid_input()
    test_invalid_riddle_format()
    print("All tests completed.")