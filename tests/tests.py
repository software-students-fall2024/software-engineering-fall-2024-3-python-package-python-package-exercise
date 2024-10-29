import pytest
import freezegun
from pymagotchi.pet import Pet, new_pet
from pymagotchi.constants import DEFAULT_TIMEFRAME, MAX_STAT_VALUE
from pymagotchi.names import generate_name
from time import sleep


# Write unit tests here to test all types of valid and valid function inputs
# Marking scheme says at least 3 tests
# Order of functions to test (Some rely on others working):
# 1) pet.time_elapsed
# 2) names.generate_name
# 3) pet.__init__
# 4) pet.new_pet
# 5) pet.update_stats
# 6) pet.status

# 1) Test Pet.time_elapsed()
@freezegun.freeze_time("2024-10-28")
def test_time_elapsed():
    pet = Pet(timeframe=DEFAULT_TIMEFRAME)
    with freezegun.freeze_time("2024-10-28 00:02:00"):
            assert pet.time_elapsed() == 120
    with freezegun.freeze_time("2024-10-28 00:02:30"):
            assert pet.time_elapsed() == 30
    with freezegun.freeze_time("2024-10-28 00:03:00"):
            assert pet.time_elapsed() == 30



# 2) Test names.generate_name()
def test_generate_name():
    name = generate_name()
    assert isinstance(name, str) 
    assert len(name) > 0 


# 3) Test Pet.__init__()
def test_pet_initialization():
    pet = Pet(name="Benny", timeframe=5, immortal=True)
    assert pet.name == "Benny"  
    assert pet.immortal is True 
    assert pet.timeframe == 5  
    assert pet.stats["health"] == MAX_STAT_VALUE
    assert pet.stats["food"] == MAX_STAT_VALUE
    assert pet.stats["sleep"] == MAX_STAT_VALUE 
    assert pet.stats["happiness"] == MAX_STAT_VALUE
    assert pet.rates["food"] == 3
    assert pet.rates["sleep"] == 3
    assert pet.rates["happiness"] == 3


# 4) Test new_pet() function
def test_new_pet():
    pet = new_pet(name="Shadow", timeframe=3, immortal=False)
    assert pet.name == "Shadow" 
    assert pet.timeframe == 3 
    assert pet.immortal is False  
    assert pet.stats["health"] == MAX_STAT_VALUE
    assert pet.stats["food"] == MAX_STAT_VALUE
    assert pet.stats["sleep"] == MAX_STAT_VALUE
    assert pet.stats["happiness"] == MAX_STAT_VALUE
    assert pet.rates["food"] == 1
    assert pet.rates["sleep"] == 1
    assert pet.rates["happiness"] == 1


# 5) Test Pet.update_stats()
def test_update_stats():
    pet = Pet(timeframe=DEFAULT_TIMEFRAME)
    pet.stats["food"] = 50
    pet.stats["sleep"] = 50
    pet.stats["happiness"] = 50
    pet.stats["health"] = 50
    sleep(1)
    pet.update_stats()  
    assert pet.stats["health"] <= 50 
    assert pet.stats["food"] < 50
    assert pet.stats["sleep"] < 50
    assert pet.stats["happiness"] < 50
   


# 6) Test Pet.status() output
def test_pet_status_initial(capsys):
    pet = Pet(name="Bella", timeframe=DEFAULT_TIMEFRAME)
    pet.status() 

    captured = capsys.readouterr()
    assert "Health: 100" in captured.out 
    assert "Food: 100" in captured.out
    assert "Sleep: 100" in captured.out
    assert "Happiness: 100" in captured.out
