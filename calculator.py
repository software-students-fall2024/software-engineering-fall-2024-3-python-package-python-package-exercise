import random

def parse_eq(equation):
    if '.' in equation:
        return "Invalid equation: Decimals are not allowed."
    if equation.strip()[0] in '+-*/' or equation.strip()[-1] in '+-*/ ':
        return "Invalid equation: Cannot start or end with an operator or space."
    
    parse_e = equation.split()

    if len(parse_e) % 2 == 0:
        return "Invalid equation: Equation must have even spaces between numbers and operations."
    
    numbers = []
    operators = []
    for i, t in enumerate(parse_e):
        if i % 2 == 0:
            if parse_e.isdigit():
                numbers.append(int(t))
            else:
                return "Invalid equation: Expected a number."
        else:
            if t in '+-*/':
                operators.append(t)
            else:
                return "Invalid equation: Expected an operator."
    
    return numbers, operators

def calculator(numbers, operators):
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