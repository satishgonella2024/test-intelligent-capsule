import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_positive_numbers(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(10, 20), 30)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calculator.add(-2, -3), -5)
        self.assertEqual(self.calculator.add(-10, -20), -30)

    def test_add_zero(self):
        self.assertEqual(self.calculator.add(0, 0), 0)
        self.assertEqual(self.calculator.add(10, 0), 10)
        self.assertEqual(self.calculator.add(0, -10), -10)

    def test_add_float_numbers(self):
        self.assertEqual(self.calculator.add(2.5, 3.2), 5.7)
        self.assertEqual(self.calculator.add(-2.1, -3.4), -5.5)

    def test_add_string_inputs(self):
        with self.assertRaises(TypeError):
            self.calculator.add("2", "3")

    def test_add_none_inputs(self):
        with self.assertRaises(TypeError):
            self.calculator.add(None, 3)
        with self.assertRaises(TypeError):
            self.calculator.add(2, None)

if __name__ == '__main__':
    unittest.main()