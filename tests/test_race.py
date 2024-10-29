import pytest
from pyanimals.main import _get_animal_emoji, _update_position, _get_race_result, race

# tests for package function race
class TestRaceFunctions:
    # race test #1: test that _get_animal_emoji() returns correct emoji
    def test_get_animal_emoji(self):
        expected_emojis = {
            "cat": "🐈",
            "bunny": "🐰",
            "elephant": "🐘",
            "rabbit": "🐇"
        }
        for animal, expected_emoji in expected_emojis.items():
            actual = _get_animal_emoji(animal)
            assert actual == expected_emoji, f"Expected emoji returned by _get_animal_emoji() to be {expected_emoji}. Instead, it returned '{actual}'"
    
    # race test #2: test that _update_position() returns valid position
    def test_update_position(self):
        # check that updated position is within +2 of initial position
        init_pos = 5
        track_length = 20

        actual = _update_position(init_pos, track_length)
        assert init_pos + 1 <= actual <= init_pos + 2, f"Expected position returned by _update_position() to be +1 or +2 from initial position {init_pos}. Instead, it returned '{actual}'"

        # check that updated position doesn't exceed track length
        init_pos = 20
        actual = _update_position(init_pos, track_length)
        assert actual <= 20, f"Expected position returned by _update_position() to be less than track_length {track_length}. Instead, it returned '{actual}'"
    
    # race test #3: test that _get_race_result() returns correct result
    def test_get_race_result(self):
        animal = "elephant"

        # animal won
        player_pos = 18
        animal_pos = 20

        actual = _get_race_result(player_pos, animal_pos, animal)
        assert actual == f"{animal.title()} is the winner. Better luck next time 😅", f"Expected winner to be {animal}. Instead, it returned '{actual}'"

        # player won
        player_pos = 20
        animal_pos = 18
        
        actual = _get_race_result(player_pos, animal_pos, animal)
        assert actual == "Congratulations! You are the winner 🏆", f"Expected winner to be player. Instead, it returned '{actual}'"

        # animal and player tied
        player_pos = 20
        animal_pos = 20

        actual = _get_race_result(player_pos, animal_pos, animal)
        assert actual == "It's a tie!", f"Expected result to be a tie. Instead, it returned '{actual}'"

    # race test #4: test that at least one racer reaches the end of track by
    # the end of race()
    def test_race(self):
        player_pos, animal_pos = race("elephant")
        assert player_pos == 20 or animal_pos == 20, f"Expected at least one racer to reach the end of track, position 20. However, by the end of race, the player was at '{player_pos}' and the animal was at '{animal_pos}'"
