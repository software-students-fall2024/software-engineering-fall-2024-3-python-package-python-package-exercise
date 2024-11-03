# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

[![.github/workflows/ci.yml](https://github.com/software-students-fall2024/3-python-package-the-fixers/actions/workflows/ci.yml/badge.svg)](https://github.com/software-students-fall2024/3-python-package-the-fixers/actions/workflows/ci.yml)

## Project Description

Our python package returns different recommendations for stretches and exercises for coders who want to take a break after coding for a period of time. The function mental_exercises takes ‘focus’, ‘creativity’, or ‘mindfulness’ as an argument and outputs a corresponding quote. The function stretches takes integer values ranging from 1 to 15 as an argument and outputs a stretch that takes the given number of minutes to complete. The eye_exercises function takes an integer value that equals 10, 20 or 60 and outputs an eye exercise that takes 10, 20, or 60 seconds to complete. The physical_exercises function takes in user input of their preferred physical exercise (ex. Running or strength), asks them for their preferred degree of intensity for the exercise, and then finally asks the user for the preferred time interval between each exercise. From then on the user will get a reminder to do their preferred physical exercise once their preferred time interval is up.  The purpose of our functions is to promote regular wellness breaks that help reduce physical and mental strain. Each function offers tailored suggestions for brief activities—such as stretching, eye exercises, movement, and mental exercises—that encourage a balanced, healthy routine throughout the day, especially for individuals with sedentary or screen-heavy tasks.

## PyPI Website 

## Developer Instructions 
how a developer who wants to import your project into their own code can do so - include documentation and code examples for all functions in your package and a link to an example Python program that uses each of them.

## Developer Contributions
how a developer who wants to contribute to your project can set up the virtual environment, install dependencies, and build and test your package for themselves.
###Fork and Clone the Repository

Fork the repository on github. The repository can be cloned with the command 
git clone https://github.com/software-students-fall2024/3-python-package-the-fixers.git

### Setting up a virtual environment 
The virtual environment pipenv can be installed with the command
