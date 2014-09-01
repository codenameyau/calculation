"""
calc.py
MIT License (c) 2014
codenameyau.github.io
"""

def calculate(a, b, repeat=False):
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


def find_combinations(target, numbers):
    combinations = []
    while numbers:
        current = numbers.pop(0)
    return combinations


def create_result(results, value):
    """
    Internal: (Dictionary, Integer) -> List
    """
    if value not in results:
        results[value] = []
