"""
calc.py
MIT License (c) 2014
codenameyau.github.io

Description:
Searches for ways to calculate a number from a given set of
numbers with the following operations: '+', '-', '*'.

Examples:
- List all ways to calculate the number 42 from the given set
python calc.py 3 9 8 4 5 -n 42
"""
import argparse


def calculate(a, b):
    """
    Public: (Integer, Integer) -> Dictionary
    Performs calculation on 'a' and 'b'
    """
    steps = {}
    return steps

def find_combinations(target, numbers):
    combinations = []
    while numbers:
        current = numbers.pop(0)
    return combinations

def main():
    """
    Command-line script argument parser
    """
    # Parse argument
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int)
    parser.add_argument('numbers', type=int, nargs='+')
    args = parser.parse_args()

    # Search for combinations
    if args.n:
        print find_combinations(args.n, args.numbers)


if __name__ == '__main__':
    main()
