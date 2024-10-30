from check_answer import check_answer
from read_file import read_file


def test_correct_answer_for_id_range_26_50():
    print("test correct answer")
    riddles = read_file("riddleLibrary.json")
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

if __name__ == "__main__":
    test_correct_answer_for_id_range_26_50()
    test_incorrect_answer_for_id_range_26_50()
    test_case_insensitive_answer_for_id_range_26_50()
    print("Completed all test")
