#!/usr/bin/python3
"""
this module tests amenity.py
"""

from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """this class test Amenity class"""

    def test_vars(self):
        x = Amenity()
        self.assertEqual(type(x.name), str)


if __name__ == '__main__':
    unittest.main()
