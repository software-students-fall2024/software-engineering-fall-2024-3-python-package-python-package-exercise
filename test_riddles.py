import pytest
from generate_riddle import generate_riddle


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

