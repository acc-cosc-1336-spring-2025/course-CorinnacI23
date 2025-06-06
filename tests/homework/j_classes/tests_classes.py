import unittest
from src.homework.j_classes.class_a import Die

class TestDie(unittest.TestCase):

    def test_roll_range(self):
        die = Die()
        for _ in range(3):  # Test 3 rolls
            die.roll()
            value = die.get_rolled_value()
            self.assertIn(value, range(1, 7), f"Value {value} not in 1-6 range")

if __name__ == '__main__':
    unittest.main()
