#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models 

class BaseModel():
    def __init__(self, *args, **kwargs):
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    print("1")
                elif key == 'created_at' or key == 'updated_at' :
                       setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')) 
                else:
                     setattr(self, key, value)
                     
    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
            return "["+__class__.__name__+"] ("+self.id+") "+str(self.__dict__)
    
    def to_dict(self):
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = __class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    












