import random

def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    symbol = input("Enter an operation (+, -, *, /): ").strip()
    if random.choice([True, False]):
        possible_symbols = {'+', '-', '*', '/'} - {symbol}
        symbol = random.choice(list(possible_symbols))

    if symbol == '+':
        result = num1 + num2
    elif symbol == '-':
        result = num1 - num2
    elif symbol == '*':
        result = num1 * num2
    elif symbol == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Can't do division by zero"
    else:
        result = "Invalid operation"

    print(f"The result is: {result}")