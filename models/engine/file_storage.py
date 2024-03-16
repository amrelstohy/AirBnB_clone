#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel


class FileStorage(BaseModel):

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass
        
    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects[obj.__class__.__name__+"."+obj.id] = obj

    def save(self):
        with open(self.__file_path, "w") as jsonfile1:
            f = dict(self.__objects)
            for key, value in f.items():
                f[key] = value.to_dict()
            jsonfile1.write(json.dumps(f))

    def reload(self):
        if os.path.exists(self.__file_path) and os.path.getsize(self.__file_path) != 0:
            with open(self.__file_path, "r") as jsonfile2:
                data = json.load(jsonfile2)
                if isinstance(data, di):
                    for key, value in data.items():
                        obj = BaseModel(**value)
                        self.__objects[key] = obj
                else:
                    pass
        else:
            pass
    











