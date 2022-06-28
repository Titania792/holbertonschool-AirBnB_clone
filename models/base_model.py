#!/usr/bin/python3
"""class BaseModel that defines all common
attributes/methods for other classes"""


from datetime import datetime
import uuid
import json


class BaseModel:
    """"""

    def __init__(self, *args, **kwargs):
        """Public instance attributes"""
        if kwargs is not None and len(kwargs) != 0:
            """ If kwargs is not None and is not empty """
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "updated_at":
                    self.created_at = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Public instance attributes"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute
            updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__
