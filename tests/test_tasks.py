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
    
#TEST 1


#TEST 2
    

#TEST 3
    
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