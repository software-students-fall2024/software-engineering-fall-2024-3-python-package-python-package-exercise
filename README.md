# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

# Package Page on Pypi

https://pypi.org/simple/pyexcuses/

# Build Badge

[![CI / CD](https://github.com/software-students-fall2024/3-python-package-realoriginal/actions/workflows/build.yaml/badge.svg)](https://github.com/software-students-fall2024/3-python-package-realoriginal/actions/workflows/build.yaml)

## Installation

Install the `pyexcuses` module with pip:

```console
pip3 install pyexcuses
```

If you want to look at all the functions, make your way to the [example program](./showcase_usage.py), which shows you how to use each function in `pyexcuses`.

### Python

Access the **excuses** in your own project by importing `pyexcuses` and using the function
`generate_excuse`:

```pycon
>>> import pyexcuses
>>> print(pyexcuses.generate_excuse())
It works on my machine, but maybe the server environment is different.
```

We can use spoken languages for English and Spanish, and we have excuses for different programming languages:

```pycon
>>> import pyexcuses
>>> print(pyexcuses.generate_excuse("es"))  # spanish excuse
Funciona en mi máquina, pero quizás el entorno del servidor sea diferente
>>> print(pyexcuses.generate_excuse("es", "javascript"))  # spanish excuse for javascript programming language
El CSS está luchando con JavaScript de nuevo.
```

Access the **solutions** in your own project by importing `pyexcuses` and using the function
`suggest_solution`:

```pycon
>>> import pyexcuses
>>> print(pyexcuses.suggest_solution())
Try running it on a Friday—bugs don't like weekends.
```

We also have solutions for different spoken languages and programming languages:

```pycon
>>> import pyexcuses
>>> print(pyexcuses.suggest_solution("es"))  # spanish solution
"¿Has probado a añadir más comentarios a tu código?
>>> print(pyexcuses.suggest_solution("es", "javascript"))  # spanish solution for javascript programming language
¿Has probado a añadir más puntos y comas? A JavaScript le encantan.
```

We have a `list_available_options` function that lets you check which languages (spoken or programming) are supported by the package.

```pycon
>>> import pyexcuses
>>> print(pyexcuses.list_available_options("spoken_language")) # print all spoken langs
['en', 'es']
>>> print(pyexcuses.list_available_options("programming_language")) # print all programming langs
['python', 'javascript', 'neutral']
```

Finally, the get_multilingual_excuse_or_solution function provides an excuse or solution in both English and Spanish for any given programming language. 

```pycon
>>> import pyexcuses
>>> print(pyexcuses.get_multilingual_excuse_or_solution("excuse", "python")) # get both spanish and english
'en': 'It works on my machine.',
'es': 'Funciona en mi máquina.'


# Get a multilingual solution in English and Spanish for JavaScript
solution = pyexcuses.get_multilingual_excuse_or_solution("solution", "javascript")
print(solution)
# Output:
# {
#    'en': 'Have you tried clearing the cache?',
#    'es': '¿Has probado a limpiar la caché?'
# }
```


## Contributing to pyexcuses

Since we love contributions, if you’d like,  please follow these steps to help us out.

1. **Clone the repository**:
   ```console
   git clone https://github.com/<your-username>/pyexcuses.git
   cd pyexcuses
   ```

2. **Create a Branch**
    ```console
    git checkout -b feat/name
    ```


3. **Install dependencies and SetUp Virtual Environment**"
    ```console
    python -m pip install --upgrade pip
    pip install pipenv
    pipenv install --dev
    ```

4. **Make Your Changes**

5. **Run tests**"
    ```console
    pipenv run pytest
    ```

6. **Commit/Push Edits**"
    ```console
    git add .
    git commit -m "Your Changes"
    git push origin feat/name
    ```

7. **Make Pull Requests**

## Team members

- [Darren Zou](https://github.com/darrenzou)
- [Peter D'Angelo](https://github.com/dangelo729)
- [Gene Park](https://github.com/geneparkmcs)
- [Joseph Chege](https://github.com/JosephChege4)