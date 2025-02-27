# tests/homework/e_functions/test_functions.py
import unittest
from src.homework.e_functions.value_return import get_hour
from src.homework.e_functions.value_return import get_minutes
from src.homework.e_functions.value_return import get_seconds

class Test_Config(unittest.TestCase):

    def test_get_hour(self):
        self.assertEqual(get_hour(3800), 1)   # 3800 seconds -> 1 hour
        self.assertEqual(get_hour(3600), 1)   # 3600 seconds -> 1 hour
        self.assertEqual(get_hour(3601), 1)   # 3601 seconds -> 1 hour
        self.assertEqual(get_hour(7200), 2)   # 7200 seconds -> 2 hours

    def test_get_minutes(self):
        self.assertEqual(get_minutes(3800), 3)  # 3800 seconds -> 3 minutes
        self.assertEqual(get_minutes(3600), 0)  # 3600 seconds -> 0 minutes
        self.assertEqual(get_minutes(3661), 1)  # 3661 seconds -> 1 minute
        self.assertEqual(get_minutes(4500), 25) # 4500 seconds -> 25 minutes

    def test_get_seconds(self):
        self.assertEqual(get_seconds(3800), 20)  # 3800 seconds -> 20 seconds
        self.assertEqual(get_seconds(3600), 0)   # 3600 seconds -> 0 seconds
        self.assertEqual(get_seconds(3661), 1)   # 3661 seconds -> 1 second
        self.assertEqual(get_seconds(4500), 0)   # 4500 seconds -> 0 seconds
