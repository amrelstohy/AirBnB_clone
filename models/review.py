#!/usr/bin/python3
"""
This module is for users

"""
from models.base_model import BaseModel



class Review(BaseModel):
    """
    This class is for users

    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        initiate the user and
        creates a basemodel object
        """
        super().__init__(**kwargs)