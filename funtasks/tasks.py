import random

tasks={}

#add task
def add_task(task_name:str,task_urgency:int):
    if task_name in tasks:
        raise ValueError(f"Task '{task_name}' already exists.")
    else:
        tasks[task_name]={"urgency": task_urgency, "completed": False}
        return f"Task '{task_name}' added with urgency {task_urgency}."

#complete task
def complete_task(task_name:str):
    if task_name not in tasks:
        return f"Task '{task_name}' not found."
    elif task_name in tasks and not tasks[task_name]["completed"]:
        tasks[task_name]["completed"]=True
        return f"Task '{task_name}' completed!"
    else:
        return f"Task '{task_name}' already completed."

#random task
def random_task():
    if not tasks:
        return "No tasks available."
    else:
        task=random.choice(list(tasks.keys()))
        return f"Random task: {task} with urgency {tasks[task]['urgency']}"
