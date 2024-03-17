#!/usr/bin/python3
"""
This module is for users

"""
from models.base_model import BaseModel



class User(BaseModel):
    """
    This class is for users

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        initiate the user and
        creates a basemodel object
        """
        super().__init__(**kwargs)
