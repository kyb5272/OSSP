import unittest
from src.division import divide_two_numbers

class TestDivision(unittest.TestCase):
    
    def test_divide_positive_numbers(self):
        self.assertEqual(divide_two_numbers(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide_two_numbers(-10, -2), 5)

    def test_divide_mixed_sign_numbers(self):
        self.assertEqual(divide_two_numbers(10, -2), -5)
        self.assertEqual(divide_two_numbers(-10, 2), -5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide_two_numbers(10, 0)

    def test_divide_zero_by_number(self):
        self.assertEqual(divide_two_numbers(0, 10), 0)

if __name__ == '__main__':
    unittest.main()