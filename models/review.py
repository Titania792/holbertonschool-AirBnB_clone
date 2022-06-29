#!/usr/bin/python3
""" Write a class Review """

from models.base_model import BaseModel
import json


class Amenity(BaseModel):
    """ Inherits from BaseModel """

    def __init__(self, *args, **kwargs):
        """ Public class attributes """
        super().__init__(*args, **kwargs)
        self.place_id = str("")
        self.user_id = str("")
        self.text = str("")
