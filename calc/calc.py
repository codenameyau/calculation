"""
calc.py
MIT License (c) 2014
codenameyau.github.io
"""

def calculate(a, b):
    """
    Public: (Integer, Integer) -> Dictionary
    Performs calculation on 'a' and 'b'
    """
    results = {}
    # Addition
    value = a + b
    create_result(results, value)
    results[value].append((a, '+', b))

    # Subtraction 1
    value = a - b
    create_result(results, value)
    results[value].append((a, '-', b))

    # Subtraction 2
    value = b - a
    create_result(results, value)
    results[value].append((b, '-', a))

    # Multiplication
    value = a * b
    create_result(results, value)
    results[value].append((a, '*', b))
    return results


def find_target(target, numbers):
    """
    Public: (Integer, List) -> List
    Returns combinations to calculate target number
    """
    # Assert minimum numbers
    if len(numbers) < 2:
        return [target]

    # Calculate first combination
    combinations = []
    current = numbers.pop(0)
    results = calculate(current, numbers[0])

    # Recursively calculate rest of combinations
    while numbers:
        current = numbers.pop(0)
        for num in results:
            combos = results[num]
            temp = calculate(current, num)
            print current, num
            print temp
            print

    return combinations


def create_result(results, value):
    """
    Internal: (Dictionary, Integer) -> List
    """
    if value not in results:
        results[value] = []
