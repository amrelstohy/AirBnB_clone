#!/usr/bin/python3
"""
this module tests city.py
"""

from models.city import City
import unittest

class TestCity(unittest.TestCase):
    """this class test City class"""

    def test_vars(self):
        x = City()
        self.assertEqual(type(x.state_id), str)
        self.assertEqual(type(x.name), str)


if __name__ == '__main__':
    unittest.main()