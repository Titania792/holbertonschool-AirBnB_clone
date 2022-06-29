#!/usr/bin/python3
""" Write a class State """


from models.base_model import BaseModel


class State(BaseModel):
    """ Inherits from BaseModel """

    def __init__(self, *args, **kwargs):
        """ Public class attributes """
        super().__init__(*args, **kwargs)
        self.name = str("")
