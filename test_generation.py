import pytest
from generate_riddle import generate_riddle
import json

@pytest.fixture
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
