#!/usr/bin/python3
"""Write a class User"""


from models.base_model import BaseModel


class User(BaseModel):
    """inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
