#!/usr/bin/python3
"""
this module tests Base_model.py
"""

from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """this class tests BaseModel class"""

    def test_init(self):
        x = BaseModel()
        self.assertEqual(type(x.id), str)
        self.assertEqual(len(x.id), 36)
        self.assertEqual(type(x.created_at), datetime)
        self.assertEqual(type(x.updated_at), datetime)

    def test_name(self):
        x = BaseModel()
        x.name = "amr"
        self.assertEqual(x.name, "amr")


if __name__ == '__main__':
    unittest.main()
