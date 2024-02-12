#!/usr/bin/python3
"""
this module is responsible for
stroring objects to json files
and retrieving them from
the json files
"""

from models.base_model import BaseModel
import json


class FileStorage():
    """
    this class is responsible for
    stroring objects to json files
    and retrieving them from
    the json files
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """Return all instances stored"""
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        Attributes:
        obj -> the object to be stored in __obects
        """

        key_format = '<{}>.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key_format] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}
        obj_dict = FileStorage.__objects
        file = FileStorage.__file_path
        for key, value in obj_dict.items():
            print(type(value))
            new_dict[key] = value.to_dict()
        with open(file, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        file = FileStorage.__file_path
        objects = FileStorage.__objects
        try :
            with open(file, 'r') as f:
                object = json.load(f)
            for key, value in object.items():
                obj = BaseModel(**value)
                objects[key] = obj
        except :
            pass
