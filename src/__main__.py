import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calculator.subtract(10, 4), 6)
        self.assertEqual(self.calculator.subtract(100, 50), 50)
        self.assertEqual(self.calculator.subtract(20, 15), 5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calculator.subtract(-10, -4), -6)
        self.assertEqual(self.calculator.subtract(-100, -50), -50)
        self.assertEqual(self.calculator.subtract(-20, -15), -5)

    def test_subtract_zero(self):
        self.assertEqual(self.calculator.subtract(10, 0), 10)
        self.assertEqual(self.calculator.subtract(0, 0), 0)
        self.assertEqual(self.calculator.subtract(-10, 0), -10)

    def test_subtract_equal_numbers(self):
        self.assertEqual(self.calculator.subtract(10, 10), 0)
        self.assertEqual(self.calculator.subtract(-10, -10), 0)

    def test_subtract_overflow(self):
        with self.assertRaises(OverflowError):
            self.calculator.subtract(float('inf'), float('inf'))

    def test_subtract_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            self.calculator.subtract('a', 'b')
        with self.assertRaises(TypeError):
            self.calculator.subtract(10, 'b')
        with self.assertRaises(TypeError):
            self.calculator.subtract('a', 10)

if __name__ == '__main__':
    unittest.main()