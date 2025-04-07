import unittest
from src.multiplication import multiply_two_numbers

class TestMultiplication(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply_two_numbers(3, 4), 12)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply_two_numbers(-3, -4), 12)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(multiply_two_numbers(3, -4), -12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply_two_numbers(0, 5), 0)
        self.assertEqual(multiply_two_numbers(5, 0), 0)

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply_two_numbers(2.5, 4), 10.0)
        self.assertAlmostEqual(multiply_two_numbers(3.5, 2.0), 7.0)

if __name__ == '__main__':
    unittest.main()