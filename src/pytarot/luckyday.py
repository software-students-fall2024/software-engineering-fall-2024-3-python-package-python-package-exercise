import random

def get_lucky_day():
    month = random.randint(1, 12)

    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:  
        day = random.randint(1, 28)

    output = f"Your lucky day is: {month}/{day}"
    return output
