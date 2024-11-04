![Python build & test](https://github.com/software-students-fall2024/3-python-package-java_and_the_scripts_/actions/workflows/build.yaml/badge.svg)


# Python Package Exercise
**Funtasks: A Task Management Package** 

This package was created by generally following the [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/) guide, with the addition of `pipenv` for virtual environment management. 

## Overview
Funtasks is a simple and efficient task management package designed to help you add, complete, and randomly select tasks. It includes features for adding tasks with urgency levels, marking tasks as complete, and generating random tasks or daily goals based on your available time. 


## How to install and use this package
---
### Prerequisites
    1. Make sure you have `pipenv` installed. You can install it using `pip3`:
    ```bash
    pip3 install pipenv

    2. To install the package, use `pip3` because this package requires Python 3:
    ```bash
    pip3 install funtasks==0.1.11

    3. Activate the virtual environment: 
    ```bash
    pipenv shell

    4. Create a Python program file that imports the package and uses it, e.g. 
    ```bash
    from funtasks.tasks import add_task, complete_task, random_task, random_daily_goal, tasks
    This approach lets you directly use ```add_task```, ```complete_task```, ```random_task```, and ```random_daily_goal```


