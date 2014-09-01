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
        """
        Calculations should contain correct keys
        """
        results = calc.calculate(8, 4)

        # Assert results is a dictionary
        self.assertEqual(type(results), dict)
        self.assertEqual(len(results), 4)

        # Assert calculations are keys
        self.assertTrue(results.has_key(12))
        self.assertTrue(results.has_key(4))
        self.assertTrue(results.has_key(-4))
        self.assertTrue(results.has_key(32))

        # Assert results of calculations
        self.assertEqual(results[12][0], (8, '+', 4))
        self.assertEqual(results[4][0],  (8, '-', 4))
        self.assertEqual(results[-4][0], (4, '-', 8))
        self.assertEqual(results[32][0], (8, '*', 4))

    def test_empty_create_result(self):
        """
        Create results of empty should create a new list
        """
        # Test empty results
        value = 2
        results = {}
        calc.create_result(results, value)
        results_list = results[value]
        self.assertTrue(results.has_key(value))
        self.assertEqual(type(results_list), list)
        self.assertEqual(len(results_list), 0)

    def test_non_empty_create_result(self):
        """
        Create results of non empty should not create a new list
        """
        # Test empty results
        value = 24
        results = {24: [(8, '*', 3)]}
        calc.create_result(results, value)
        results_list = results[value]
        self.assertTrue(results.has_key(value))
        self.assertEqual(type(results_list), list)
        self.assertEqual(len(results_list), 1)


if __name__ == '__main__':
    unittest.main()
