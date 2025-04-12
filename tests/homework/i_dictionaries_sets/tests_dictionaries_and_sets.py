# tests/homework/i_dictionaries_and_sets/test_dictionaries_and_sets.py

import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):
    
    def setUp(self):
        """Setup an initial inventory dictionary for testing."""
        self.inventory = {}

    def test_add_inventory(self):
        """Test the add_inventory function."""
        add_inventory(self.inventory, 'Widget1', 10)
        self.assertEqual(self.inventory['Widget1'], 10)  # Assert Widget1 is added with quantity 10

        add_inventory(self.inventory, 'Widget1', 25)
        self.assertEqual(self.inventory['Widget1'], 35)  # Assert quantity updated to 35

        add_inventory(self.inventory, 'Widget1', -10)
        self.assertEqual(self.inventory['Widget1'], 25)  # Assert quantity updated to 25

    def test_remove_inventory_widget(self):
        """Test the remove_inventory_widget function."""
        add_inventory(self.inventory, 'Widget1', 10)
        add_inventory(self.inventory, 'Widget2', 20)

        result = remove_inventory_widget(self.inventory, 'Widget1')
        self.assertEqual(result, 'Record deleted')  # Assert widget1 is deleted

        self.assertEqual(len(self.inventory), 1)  # Assert only 1 widget remains
        self.assertIn('Widget2', self.inventory)  # Assert Widget2 still exists

        result = remove_inventory_widget(self.inventory, 'Widget1')
        self.assertEqual(result, 'Item not found')  # Assert trying to delete again returns 'Item not found'

