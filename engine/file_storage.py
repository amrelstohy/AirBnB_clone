#!/usr/bin/python3
import pathlib
import json


class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        pass

    def save(self):
        with open(self.__file_path, "a") as jsonfile:
           jsonfile.write(json.dump(self.__objects))

    def reload(self):
        if self.__file_path == None:
            pass
        else:
            pass











