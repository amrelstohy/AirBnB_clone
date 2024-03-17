#!/usr/bin/python3
"""
this module tests place.py
"""

from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """this class test Place class"""

    def test_vars(self):
        x = Place()
        self.assertEqual(type(x.name), str)
        self.assertEqual(type(x.city_id), str)
        self.assertEqual(type(x.user_id), str)
        self.assertEqual(type(x.description), str)
        self.assertEqual(type(x.number_rooms), int)
        self.assertEqual(type(x.number_bathrooms), int)
        self.assertEqual(type(x.max_guest), int)
        self.assertEqual(type(x.price_by_night), int)
        self.assertEqual(type(x.latitude), float)
        self.assertEqual(type(x.longitude), float)
        self.assertEqual(type(x.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
