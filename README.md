# Riddle Generator

[![PyPI Version](https://img.shields.io/pypi/v/riddle-generator)](https://pypi.org/project/riddle-generator/)

## Overview

**Riddle Generator** is a lighthearted Python package designed to bring a bit of joy and levity to developers' lives. It provides an interactive experience where users can generate riddles of varying difficulties and topics, check answers, submit new riddles, and receive hints. The package is built following rigorous software engineering practices, ensuring quality and reliability.

## Installation

Install the package via pip:

```bash
pip install riddle-generator
```

## Usage

### Importing the Package

```python
import riddle_generator
```

### Functions and Examples

#### Function 1: `generate_riddle(difficulty: int) -> str`

Generates a random riddle based on the specified difficulty level.

- **Parameters:**
  - `difficulty` (int): The difficulty level of the riddle (1 to 4).

- **Returns:**
  - A string containing the riddle's question.

- **Example:**

  ```
  import riddle_generator

  # Generate a riddle of difficulty level 2
  riddle = riddle_generator.generate_riddle(2)
  print(f"Here's your riddle: {riddle}")
  ```

#### Function 2: `check_answer(riddle_id: int, answer: str) -> str`

Checks if the provided answer to the riddle is correct.

- **Parameters:**
  - `riddle_id` (int): The ID of the riddle.
  - `answer` (str): The user's answer to the riddle.

- **Returns:**
  - A string indicating whether the answer is correct or incorrect.

- **Example:**

  ```
  import riddle_generator

  # Check the answer to a riddle with ID 5
  result = riddle_generator.check_answer(5, 'shadow')
  print(result)  # Outputs: "Correct answer!" or "Incorrect answer. Try again!"
  ```

#### Function 3: `submit_riddle(custom_riddle: dict) -> str`

Allows users to submit their own riddles to the library.

- **Parameters:**
  - `custom_riddle` (dict): A dictionary containing the riddle's details.

    - `question` (str): The riddle's question.
    - `answer` (list): A list of acceptable answers.
    - `hint` (str): A hint for the riddle.
    - `difficulty` (int): Difficulty level (1 to 4).
    - `topic` (str): The topic of the riddle.

- **Returns:**
  - A string indicating success or an error message.

- **Example:**

  ```python
  import riddle_generator

  # Define your custom riddle
  my_riddle = {
      "question": "I speak without a mouth and hear without ears. What am I?",
      "answer": ["echo"],
      "hint": "You can hear me but cannot see me.",
      "difficulty": 2,
      "topic": "Mystery"
  }

  # Submit the riddle
  response = riddle_generator.submit_riddle(my_riddle)
  print(response)  # Outputs: "Riddle submitted successfully"
  ```

#### Function 4: `provide_hint(riddle_id: int) -> str`

Provides a hint for the specified riddle.

- **Parameters:**
  - `riddle_id` (int): The ID of the riddle.

- **Returns:**
  - A string containing the hint or an error message.

- **Example:**

  ```python
  import riddle_generator

  # Get a hint for a riddle
  hint = riddle_generator.provide_hint(5)
  print(hint)  # Outputs the hint for the riddle
  ```

#### Function 5: `read_file(file_path: str) -> list`

Reads the riddle library from a JSON file.

- **Parameters:**
  - `file_path` (str): Path to the JSON file containing riddles.

- **Returns:**
  - A list of riddle dictionaries.

- **Example:**

  ```python
  import riddle_generator

  # Read riddles from a file
  riddles = riddle_generator.read_file('riddleLibrary.json')
  print(riddles)
  ```

_**For more examples, check out** [this example program](https://github.com/yourusername/riddle-generator/blob/main/example_program.py)._

## Contributing

### Setting Up the Development Environment

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/riddle-generator.git
   ```


2. **Install pipenv if you haven't already:**

   ```bash
   pip install pipenv
   ```

3. **Create a virtual environment and install dependencies:**

   ```bash
   pipenv install --dev
   ```

4. **Activate the virtual environment:**

   ```bash
   pipenv shell
   ```

### Building and Testing

- **Run Tests:**

  We use `pytest` for testing. In test.py file, running this file by using pytest.

  ```bash
  pytest
  ```

- **Build Package:**

  Use `build` to create the package artifacts.

  ```bash
  python -m build
  ```

- **Upload to PyPI (For maintainers):**

  Use `twine` to upload the package.

  ```bash
  twine upload dist/*
  ```

### Git Workflow

All code changes must be done in feature branches and not directly in the `main` branch.

To merge code from a feature branch into `main`:

1. **Create a pull request** from the feature branch to `main`.
2. **Request a code review** from a team member.
3. **Review and approve** the code after ensuring all tests pass.
4. **Merge the pull request** into `main`.
5. **Delete the feature branch**.

**Note:** Regularly merge feature branches to avoid merge conflicts.

## Contributors

- [Teammate 1](https://github.com/teammate1)
- [Teammate 2](https://github.com/teammate2)
- [Teammate 3](https://github.com/teammate3)
- [Teammate 4](https://github.com/teammate4)

## Instructions for Running the Project

### For Developers

1. **Ensure Python 3.9 or higher is installed** on your system.

2. **Clone the repository and set up the environment** as described in the [Contributing](#contributing) section.

3. **Run the example program:**

   ```bash
   python example_program.py
   ```

### For Users

1. **Install the package via pip:**

   ```bash
   pip install riddle-generator
   ```

2. **Use the package in your Python scripts** as shown in the [Usage](#usage) examples.

## Configuration and Setup

### Environment Variables

No environment variables are required for basic usage.

### Importing Starter Data

The package uses a `riddleLibrary.json` file to store riddles. Ensure that this file is in the root directory of your project.

