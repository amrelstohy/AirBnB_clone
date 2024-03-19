#!/usr/bin/python3
"""this module tests file_storage"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import datetime
import time


class TestFileStorage(unittest.TestCase):
    """this class tests FileStorage class"""

    def test_var(self):
        x = BaseModel()
        FileStorage.save(self)
        y = FileStorage.all(self)
        print(type(FileStorage.all(self)))
        self.assertEqual(type(y), dict)

    def test_file(self):
        """self.assertEqual(FileStorage.__file_path, None)"""

        key = "_FileStorage__file_path"

        self.assertEqual(type(FileStorage.__dict__[key]), str)
        self.assertEqual(FileStorage.__dict__[key], "file.json")

    def test_save(self):
        x = BaseModel()
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)
