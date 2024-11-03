import pytest
from src.virtualpet.pet import VirtualPet

def test_feed_pet():
    """Test feed_pet() functionality comprehensively"""
    pet = VirtualPet("TestPet")
    
    # Test initial state
    assert pet.happiness == 10, "Initial happiness should be 10"
    assert pet.cleanness == 10, "Initial cleanness should be 10"
    
    # Test feeding multiple times and check values
    pet.feed_pet()
    assert pet.happiness == 10, "Happiness should stay at 10 (max)"
    assert pet.cleanness == 8, "Cleanness should decrease by 2"
    
    # Test feeding until pet gets dirty
    for _ in range(3):  # Feed 3 more times
        pet.feed_pet()
    
    assert pet.cleanness == 2, "Cleanness should be 2 after 4 feedings"
    assert pet.dirty_command_count == 1, "Should have 1 dirty command"
    
    # Test feeding with minimum cleanness
    pet.feed_pet()
    assert pet.cleanness == 1, "Cleanness shouldn't go below 1"
    assert pet.dirty_command_count == 2, "Should have 2 dirty commands"


def test_feed_sleeping_pet():
    """Test feeding a sleeping pet"""
    pet = VirtualPet("TestPet")
    pet.is_sleeping = True
    
    initial_happiness = pet.happiness
    initial_cleanness = pet.cleanness
    
    pet.feed_pet()
    
    assert pet.happiness == initial_happiness, "Sleeping pet's happiness shouldn't change"
    assert pet.cleanness == initial_cleanness, "Sleeping pet's cleanness shouldn't change"

def test_exit():
    """Test basic exit functionality"""
    pet = VirtualPet("TestPet")
    pet.exit()
    assert pet.active == False, "Pet should not be active after exit"

def test_take_shower():
    """Test the take_shower() functionality"""
    pet = VirtualPet("TestPet")
    pet.cleanness = 2

    # Take a shower to reset cleanness
    pet.take_shower()
    assert pet.cleanness == 10, "Cleanness should be reset to 10 after a shower"
    assert pet.dirty_command_count == 0, "Dirty command count should be reset to 0 after a shower"

def test_play_with_pet():
    """Test play_with_pet() functionality for different actions comprehensively"""
    pet = VirtualPet("TestPet")

    # Test initial state
    assert pet.happiness == 10, "Initial happiness should be 10"
    assert pet.cleanness == 10, "Initial cleanness should be 10"
    
    # Play with pet using 'hug' action
    pet.happiness = 8  # Reduce happiness to allow an increase
    pet.play_with_pet('hug')
    assert pet.happiness == 10, "Happiness should increase by 2 but not exceed max limit"
    assert pet.cleanness == 9, "Cleanness should decrease by 1 after hug"

    # Play with pet using 'pet' action when happiness is below max
    pet.happiness = 8
    pet.play_with_pet('pet')
    assert pet.happiness == 9, "Happiness should increase by 1 after pet action"
    assert pet.cleanness == 8, "Cleanness should decrease by 1 after pet action"

    # Play with pet using 'kiss' action when happiness is below max
    pet.happiness = 7
    pet.play_with_pet('kiss')
    assert pet.happiness == 10, "Happiness should increase by 3 but not exceed max limit"
    assert pet.cleanness == 7, "Cleanness should decrease by 1 after kiss action"

    # Test playing with pet when happiness is already at max
    pet.happiness = 10
    pet.play_with_pet('hug')
    assert pet.happiness == 10, "Happiness should stay at 10 when at max"
    assert pet.cleanness == 6, "Cleanness should decrease by 1 after hug"

    # Test playing when pet is sleeping
    pet.is_sleeping = True
    initial_happiness = pet.happiness
    initial_cleanness = pet.cleanness
    pet.play_with_pet('hug')
    assert pet.happiness == initial_happiness, "Sleeping pet's happiness shouldn't change"
    assert pet.cleanness == initial_cleanness, "Sleeping pet's cleanness shouldn't change"

    # Test invalid action
    pet.is_sleeping = False
    pet.play_with_pet('invalid')
    assert pet.happiness == initial_happiness, "Invalid action should not affect happiness"
    assert pet.cleanness == initial_cleanness, "Invalid action should not affect cleanness"

def test_restart():
    """Test the restart() functionality"""
    pet = VirtualPet("TestPet")

    # Assign non-default values
    pet.happiness = 1
    pet.cleanness = 6
    pet.is_sleeping = True
    pet.dirty_command_count = 3

    # Reset everything
    pet.restart()

    assert pet.happiness == 10, "Happiness should be reset to 10 after restart"
    assert pet.cleanness == 10, "Cleanness should be reset to 10 after restart"
    assert not pet.is_sleeping, "Pet should not be sleeping after restart"
    assert pet.dirty_command_count == 0, "Dirty command count should be reset to 0 after restart"
    assert pet.active == True, "Pet should be active after restart"