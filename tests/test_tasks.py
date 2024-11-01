import pytest
from funtasks.tasks import add_task, complete_task, random_task, random_daily_goal, tasks

##############################
#add task tests

#TEST 1
def test_add_task():
    tasks.clear()
    result=add_task("Do laundry", 3)
    assert result=="Task 'Do laundry' added with urgency 3."
    assert tasks["Do laundry"]["urgency"]==3
    assert tasks["Do laundry"]["completed"]==False

#TEST 2
    


#TEST 3
    

##############################
#complete task tests
    
def test_complete_incomplete():
    tasks["Incomplete Task"] = {"completed": False}
    result = complete_task("Incomplete Task")
    assert result == "Task successfully completed!"
    assert tasks["Incomplete Task"]["completed"]

def test_complete_completed():
    tasks["Completed Task"] = {"completed": True}
    result = complete_task("Completed Task")
    assert result == "Task already completed."

def test_complete_nonexist():
    result = complete_task("Nonexistent Task")
    assert result == "Task 'Nonexistent Task' not found."
    
##############################
#random task tests
    
#TEST 1


#TEST 2
    

#TEST 3
    
##############################
#daily goal task tests
    
#TEST 1


#TEST 2
    

#TEST 3
    
##############################