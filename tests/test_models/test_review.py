#!/usr/bin/python3
"""
this module tests review.py
"""

from models.review import Review
import unittest

class TestReview(unittest.TestCase):
    """this class test Review class"""

    def test_vars(self):
        x = Review()
        self.assertEqual(type(x.place_id), str)
        self.assertEqual(type(x.user_id), str)
        self.assertEqual(type(x.text), str)


if __name__ == '__main__':
    unittest.main()