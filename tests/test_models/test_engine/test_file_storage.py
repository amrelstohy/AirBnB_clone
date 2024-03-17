#!/usr/bin/python3
"""this module tests file_storage"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """this class tests FileStorage class"""

    def test_var(self):
        x = BaseModel()
        FileStorage.save(self)
        y = FileStorage.all(self)
        print(type(FileStorage.all(self)))
        self.assertEqual(type(y), dict)

    