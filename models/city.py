#!/usr/bin/python3
""" Write a class City """


from models.base_model import BaseModel


class City(BaseModel):
    """ Inherits from BaseModel """

    def __init__(self, *args, **kwargs):
        """ Public class attributes """
        super().__init__(*args, **kwargs)
        self.name = str("")
        self.state_id = str("")
