#!/usr/bin/python3
"""
this module tests state.py
"""

from models.state import State
import unittest

class TestState(unittest.TestCase):
    """this class test State class"""

    def test_vars(self):
        x = State()
        self.assertEqual(type(x.name), str)
 


if __name__ == '__main__':
    unittest.main()