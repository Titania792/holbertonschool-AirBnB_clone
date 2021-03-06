#!/usr/bin/python3
"""class BaseModel that defines all common
attributes/methods for other classes"""


from datetime import datetime
import uuid
import json
import models


class BaseModel:
    """class basemodel that define all common attributes"""

    def __init__(self, *args, **kwargs):
        """Public instance attributes"""
        is_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs is not None and len(kwargs) != 0:
            """ If kwargs is not None and is not empty """
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.strptime(value, is_format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, is_format)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Public instance attributes"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute
            updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        dict_cpy = self.__dict__.copy()
        dict_cpy["created_at"] = self.created_at.isoformat()
        dict_cpy["updated_at"] = self.updated_at.isoformat()
        dict_cpy['__class__'] = self.__class__.__name__
        return dict_cpy
