"""
calc.py
MIT License (c) 2014
codenameyau.github.io

Run in 'calculation/' directory:
nosetests
"""
from calc import calc
import unittest

class TestCalculation(unittest.TestCase):

    def setUp(self):
        pass

    def test_calculate(self):
        steps = calc.calculate(8, 4)
        self.assertEqual(steps, {})


if __name__ == '__main__':
    unittest.main()