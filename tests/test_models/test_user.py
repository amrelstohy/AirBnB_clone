#!/usr/bin/python3
"""
this module tests user.py
"""

from models.user import User
import unittest

class TestUser(unittest.TestCase):
    """this class test User class"""

    def test_vars(self):
        x = User()
        self.assertEqual(type(x.password), str)
        self.assertEqual(type(x.email), str)
        self.assertEqual(type(x.first_name), str)
        self.assertEqual(type(x.last_name), str)


if __name__ == '__main__':
    unittest.main()