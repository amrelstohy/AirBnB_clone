#!/usr/bin/python3
"""
This module is for users

"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class User(BaseModel):
    """
    This class is for users

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        """
        initiate the user and
        creates a basemodel object
        """
        super().__init__()