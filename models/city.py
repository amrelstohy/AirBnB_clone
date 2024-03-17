#!/usr/bin/python3
"""
This module is for users

"""
from models.base_model import BaseModel



class City(BaseModel):
    """
    This class is for users

    """

    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """
        initiate the user and
        creates a basemodel object
        """
        super().__init__(**kwargs)
