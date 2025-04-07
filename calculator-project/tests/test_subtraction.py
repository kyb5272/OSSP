import unittest
from src.subtraction import subtract_two_numbers

class TestSubtraction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(subtract_two_numbers(10, 5), 5)

    def test_negative_numbers(self):
        self.assertEqual(subtract_two_numbers(-1, -1), 0)

    def test_zero(self):
        self.assertEqual(subtract_two_numbers(0, 5), -5)

    def test_subtracting_zero(self):
        self.assertEqual(subtract_two_numbers(5, 0), 5)

    def test_large_numbers(self):
        self.assertEqual(subtract_two_numbers(1000000, 999999), 1)

if __name__ == '__main__':
    unittest.main()