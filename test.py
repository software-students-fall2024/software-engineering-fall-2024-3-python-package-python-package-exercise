from provide_hint import provide_hint

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

if __name__ == "__main__":
    test_valid_id()
    test_invalid_input()
    test_nonexistent_id()
    print("All tests completed.")