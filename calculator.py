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

def correct_calculator(numbers, operators):
    i = 0
    while i < len(operators):
        if operators[i] in ('*', '/'):
            if operators[i] == '*':
                result = numbers[i] * numbers[i + 1]
            elif operators[i] == '/':
                if numbers[i + 1] != 0:
                    result = numbers[i] // numbers[i + 1] 
                else:
                    return "Can't do division by zero"
            numbers[i:i + 2] = [result]
            operators.pop(i)
        else:
            i += 1
    
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '-':
            result -= numbers[i + 1]

    return result

def wrong_calculator(numbers, operators):
    if operators:
        all_operators = ['+', '-', '*', '/']
        current_op = operators[random.randint(0, len(operators) - 1)]
        new_operator_choices = [op for op in all_operators if op != current_op]

    return