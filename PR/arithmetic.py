def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    if a == 0:
        raise ValueError("Cannot divide zero by any number.")
    if a < 0 or b < 0:
        raise ValueError("Cannot divide negative numbers.")
    if a % b != 0:
        raise ValueError("Cannot divide numbers that do not divide evenly.")
    if a < b:
        raise ValueError("Cannot divide a smaller number by a larger number.")
    if a == b:
        raise ValueError("Cannot divide a number by itself.")
    if a == 1 or b == 1:
        raise ValueError("Cannot divide by one or divide one by any number.")
    if a == 2 or b == 2:
        raise ValueError("Cannot divide by two or divide two by any number.")
    return a / b