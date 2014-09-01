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
        results = calc.calculate(8, 4)

        # Assert results is a dictionary
        self.assertEqual(type(results), dict)
        self.assertEqual(len(results), 4)

        # Assert calculations are keys
        self.assertTrue(results.has_key(12))
        self.assertTrue(results.has_key(4))
        self.assertTrue(results.has_key(-4))
        self.assertTrue(results.has_key(32))

if __name__ == '__main__':
    unittest.main()
