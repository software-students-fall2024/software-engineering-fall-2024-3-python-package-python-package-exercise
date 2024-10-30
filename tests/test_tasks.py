import pytest
from funtasks.tasks import add_task, tasks

def test_add_task():
    # Clear the tasks dictionary before running the test
    tasks.clear()

    # Test adding a new task
    result = add_task("Do laundry", 3)
    assert result == "Task 'Do laundry' added with urgency 3."
    assert tasks["Do laundry"] == 3

    # Test adding another task
    result = add_task("Write report", 5)
    assert result == "Task 'Write report' added with urgency 5."
    assert tasks["Write report"] == 5

    # Test trying to add a duplicate task (should raise a ValueError)
    with pytest.raises(ValueError):
        add_task("Do laundry", 4)
