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
    steps = {}
    # Calculate addition
    result = a + b
    steps[result] = []
    steps[result].append((a, '+', b))

    # Calculate subtraction 1
    result = a - b
    steps[result] = []
    steps[result].append((a, '+', b))

    # Calculate subtraction 2

    # Calculate multiplication

    return steps

def find_combinations(target, numbers):
    combinations = []
    while numbers:
        current = numbers.pop(0)
    return combinations

def push_results(results, a, b, op):
