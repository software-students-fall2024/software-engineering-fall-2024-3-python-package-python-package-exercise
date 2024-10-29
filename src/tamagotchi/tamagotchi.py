import os

# create your own tamagotchi

def getpet(number):
    """Returns the pet associated with the number input"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(base_dir, f'tama-{number}.txt')
    try:
        with open(filename, 'r') as f:
            pet = f.read()
            print(pet) 
            return pet
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
