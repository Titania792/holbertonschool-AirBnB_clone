#!/usr/bin/python3
"""Write a class Place"""

from models.base_model import BaseModel
import json


class Place(BaseModel):
    """ Inherits from BaseModel """

    def __init__(self, *args, **kwargs):
        """ Public class attributes """
        super().__init__(*args, **kwargs)
        self.city_id = str("")
        self.user_id = str("")
        self.name = str("")
        self.description = str("")
        self.number_rooms = int(0)
        self.number_bathrooms = int(0)
        self.max_guest = int(0)
        self.price_by_night = int(0)
        self.latitude = float(0.0)
        self.longitude = float(0.0)
        self.amenity_ids = {}
