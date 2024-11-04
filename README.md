# Python Package Exercise

Built Oracle, a prophet that can do multiple things, including spit fortunes (fortune cookie),
output a random decision (8ball), give a quick, random mood (vibe check), and output a random 
pet (petting zoo). 

## Badge
[INSERT BADGE HERE]

## Link to Package Page
[INSERT LINK HERE]




## Team Members
[Christopher Li](https://github.com/christopherlii), [Julie Chen](https://github.com/Julie-Chen), [Maddy Li](https://github.com/maddy-li), [Aneri Shah](https://github.com/anerivs)


## Steps necessary to run the software

1. Clone the respository to your local machine.

2. Create a virtual environment by running the following command:
```
pip3 install pipenv
```

3. Activate the environment by running the below command:
```
pipenv shell
```

4. Navigate to Oracle directory and run software with 
```
pipenv run python -m cli.py
```

## Steps necessary to run tests

1. Install PyTest
```
pipenv install --dev pytest build twine
```

2. Run the tests with `pytest`