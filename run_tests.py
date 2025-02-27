# tests/run_tests.py
import unittest
from tests.homework.e_functions import test_functions

suite = unittest.TestLoader().loadTestsFromModule(test_functions)
unittest.TextTestRunner().run(suite)


