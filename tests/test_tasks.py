import pytest
from funtasks.tasks import add_task, complete_task, random_task, random_daily_goal, tasks


def test_add_task():
    tasks.clear()
    result=add_task("Do laundry", 3)
    assert result=="Task 'Do laundry' added with urgency 3."
    assert tasks["Do laundry"]["urgency"]==3
    assert tasks["Do laundry"]["completed"]==False

