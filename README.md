# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

[![.github/workflows/ci.yml](https://github.com/software-students-fall2024/3-python-package-the-fixers/actions/workflows/ci.yml/badge.svg)](https://github.com/software-students-fall2024/3-python-package-the-fixers/actions/workflows/ci.yml)

## Project Description

Our python package returns different recommendations for stretches and exercises for coders who want to take a break after coding for a period of time. The function mental_exercises takes ‘focus’, ‘creativity’, or ‘mindfulness’ as an argument and outputs a corresponding quote. The function stretches takes integer values ranging from 1 to 15 as an argument and outputs a stretch that takes the given number of minutes to complete. The eye_exercises function takes an integer value that equals 10, 20 or 60 and outputs an eye exercise that takes 10, 20, or 60 seconds to complete. The physical_exercises function takes in user input of their preferred physical exercise (ex. Running or strength), asks them for their preferred degree of intensity for the exercise, and then finally asks the user for the preferred time interval between each exercise. From then on the user will get a reminder to do their preferred physical exercise once their preferred time interval is up.  The purpose of our functions is to promote regular wellness breaks that help reduce physical and mental strain. Each function offers tailored suggestions for brief activities—such as stretching, eye exercises, movement, and mental exercises—that encourage a balanced, healthy routine throughout the day, especially for individuals with sedentary or screen-heavy tasks.

## PyPI Website 
https://pypi.org/project/codebreak/0.1/

## Developer Instructions 
how a developer who wants to import your project into their own code can do so - include documentation and code examples for all functions in your package and a link to an example Python program that uses each of them.

Step 1: Install the Package
To use codebreak in your project, first install it from PyPI. In your terminal or command prompt, type:
```
pip install codebreak
```

Step 2: Import and Use the Package
After installation, you can import CodeBreak modules and functions directly into your Python code. Below is a description of each function and class in the package, along with usage examples.

Function Documentation and Examples
1. Eye Exercise (eye_exercise function)
Provides a quick eye exercise suggestion based on the specified duration in seconds.

Function: eye_exercise(duration: int) -> str
Parameters:
duration (int): The duration for the exercise (options: 10, 20, or 60 seconds)
Returns: A string describing an eye exercise suggestion for the specified duration.
Example Usage:

```
from codebreak.eye_exercises import eye_exercise

# Get a 10-second eye exercise suggestion
print(eye_exercise(10))
```

2. Mental Exercise (mental_exercise function)
Provides a mental exercise suggestion based on the type of break desired.

Function: mental_exercise(break_type: str) -> str
Parameters:
break_type (str): The type of mental break (options: 'focus', 'creativity', 'mindfulness')
Returns: A string describing a mental exercise suggestion for the specified type.
Example Usage:
```
from codebreak.mental_exercises import mental_exercise

# Get a mental exercise suggestion for creativity
print(mental_exercise("creativity"))
```
3. Physical Exercise (Exercise class)
The Exercise class provides instructions for a physical exercise, allowing different intensity levels.

Class: Exercise
Methods:
get_name(): Returns the exercise name as a string.
output(intensity: str): Prints instructions for the exercise based on the specified intensity ('low', 'medium', or 'high').
Example Usage:

```
from codebreak.physical_exercise import Exercise

# Create an instance of the Exercise class for jogging
jogging = Exercise("Jogging", "5 minutes", "10 minutes", "15 minutes", "Cardio")

# Print a high-intensity exercise suggestion
jogging.output("high")
```

4. Stretch Exercise (stretch_exercise function)
Suggests a stretch exercise based on the available time in minutes.

Function: stretch_exercise(minutes: int) -> str
Parameters:
minutes (int): Available time for stretching (between 1 and 15 minutes)
Returns: A string describing a stretching exercise suggestion for the specified duration.
Example Usage:
```
from codebreak.stretches import stretch_exercise

# Get a 5-minute stretching exercise suggestion
print(stretch_exercise(5))
```
Step 3: Example Program
To see all functions in action, try running the example program on GitHub. This example demonstrates each function in the package and shows how to use them in a Python script.

Here’s an overview of the example_program.py file:

```
from codebreak.eye_exercises import eye_exercise
from codebreak.mental_exercises import mental_exercise
from codebreak.physical_exercise import Exercise
from codebreak.stretches import stretch_exercise

# Example usage of eye exercise function
print("Eye Exercise:", eye_exercise(10))

# Example usage of mental exercise function
print("Mental Exercise:", mental_exercise("creativity"))

# Example usage of Exercise class
jogging = Exercise("Jogging", "5 minutes", "10 minutes", "15 minutes", "Cardio")
jogging.output("medium")

# Example usage of stretch exercise function
print("Stretch Exercise:", stretch_exercise(8))
```

## Developer Contributions
how a developer who wants to contribute to your project can set up the virtual environment, install dependencies, and build and test your package for themselves.
###Fork and Clone the Repository

Fork the repository on github. The repository can be cloned with the command 
git clone https://github.com/software-students-fall2024/3-python-package-the-fixers.git

### Setting up a virtual environment 
The virtual environment pipenv can be installed with the command
``` 
pip install pipenv
``` 

To activate the environment, run
``` 
pipenv shell
``` 

### Installing dependencies

To install pytest, run the commands
``` 
pipenv install pytest
``` 
``` 
pipenv install random
``` 

In the pipenv environment, run to install all dependencies. The Pipfile can alternatively used.
``` 
pipenv install -r requirements.txt
``` 

### Build the package 
If you haven’t already installed build then run the command
``` 
pip install build 
``` 
To build the package run the command 
``` 
python -m build
``` 
Make changes on the local repository on a new branch using the command
``` 
git checkout -b feature/your-feature-name
``` 
Stage changes, commit the changes, and push the changes to the forked repository on Github. It is important to note that to prevent merge conflicts, git pull is always recommended before pushing any changes. 
``` 
git add .
git commit -m "Add description of your changes"
git push origin branch-name
``` 
Go to the forked repository on GitHub and create a pull request for the branch that was just pushed. Select ‘Compare & pull request.’ and submit the pull request to the original repository. 

## Teammates 
[Nick Burwell](https://github.com/nickburwell)
[Finn Eskeland](https://github.com/finn1003)
[Jessie Kim](https://github.com/jessiekim0)
[Dasha Miroshnichenko](https://github.com/dm5198)

## Configuration 
instructions for how to configure and run all parts of your project for any developer on any platform - these instructions must work!
Mac
Windows
Linux 

## Other
instructions for how to set up any environment variables and import any starter data into the database, as necessary, for the system to operate correctly when run.
if there are any "secret" configuration files, such as .env or similar files, that are not included in the version control repository, exact instructions for how to create them and what their contents should be must be supplied to the course admins by the due date.
