import unittest
from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

class Test_Config(unittest.TestCase):

    def test_get_factorial(self):
        self.assertEqual(get_factorial(4), 24)
        self.assertEqual(get_factorial(5), 120)
        self.assertEqual(get_factorial(6), 720)

    def test_sum_odd_numbers(self):
        self.assertEqual(sum_odd_numbers(7), 16)  # 1 + 3 + 5 + 7
        self.assertEqual(sum_odd_numbers(9), 25)  # 1 + 3 + 5 + 7 + 9
        self.assertEqual(sum_odd_numbers(10), 25)  # 1 + 3 + 5 + 7 + 9



