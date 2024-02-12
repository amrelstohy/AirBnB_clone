#!/usr/bin/python3
"""
This module defines a class Basemodel.
All the attriutes/methods
needed for other classes are found here.
"""

from uuid import uuid4
import datetime
import models


class BaseModel():
    """
    This class defines all attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        initialization function for creating new
        instances of the basemodel class
        attributes and their functions
        id -> makes a uuid code for the instance
        created_at -> represents time of creation of an obj
        updated_at -> represents the updated time for obj
        """
        if (len(kwargs) != 0):
            kwargs.pop("__class__")
            format = "%Y-%m-%dT%H:%M:%S.%f"
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.datetime.strptime(v, format)
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        this string magic functions writes out the
        string to be printed when printing the object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id, self.__dict__)

    def save(self):
        """
        function responsible for updates the public instance
        attribute updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing
        all keys/values of __dict__ of the instance:
        """
        new_dict = {}
        new_dict['__class__'] = self.__class__.__name__
        new_dict.update(dict(self.__dict__))
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict
