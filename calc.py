"""
calc.py
MIT License (c) 2014
codenameyau.github.io

Description:
Searches for ways to calculate a number from a given set of
numbers with the following operations: '+', '-', '*'.

Examples:
- List all ways to calculate the number 42 from the given set
python calc.py -n 42 -s 9 8 4 5
"""
import argparse


def main():
    """
    Command-line script argument parser
    """
    # Parse argument
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int)
    number = parser.parse_args().integer


if __name__ == '__main__':
    main()
