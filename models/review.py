#!/usr/bin/python3
""" Write a class Review """

from models.base_model import BaseModel
import json


class Review(BaseModel):
    """ Inherits from BaseModel """

    place_id = ""
    user_id = ""
    text = ""
