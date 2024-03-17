#!/usr/bin/python3
"""
this module tests Base_model.py
"""

from models.base_model import BaseModel
import unittest

class TestBaseModel(unittest.TestCase):
    """this class tests BaseModel class"""

    def test_id(self):
        x = BaseModel()
        x.id = "123"
        self.assertEqual(x.id, "123")

    def test_name(self):
        x = BaseModel()
        x.name = "amr"
        self.assertEqual(x.name, "amr")


if __name__ == '__main__':
    unittest.main()