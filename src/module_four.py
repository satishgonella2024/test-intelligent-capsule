Here is the Python code for the 'Calculator' class and its unit tests:

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(1, 1), 0)
        self.assertEqual(self.calculator.subtract(0, 0), 0)

if __name__ == '__main__':
    unittest.main()