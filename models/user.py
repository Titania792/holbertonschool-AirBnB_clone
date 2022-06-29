#!/usr/bin/python3
"""Write a class User"""


from models.base_model import BaseModel


class User(BaseModel):
    """inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Public class attributes"""
        super().__init__(*args, **kwargs)
        self.email = str("")
        self.password = str("")
        self.first_name = str("")
        self.last_name = str("")
