#!/usr/bin/python3
"""Write a class Amenity"""

from models.base_model import BaseModel
import json


class Amenity(BaseModel):
    """inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Public class attributes"""
        super().__init__(*args, **kwargs)
        self.name = str("")

    def __str__(self):
        """returns the string representation of a Amenity object"""
        return "[Amenity] ({}) {}".format(self.id, self.name)

    def save(self):
        """updates the file_path attribute"""
        self.updated_at = self._updated_at()
        self.to_dict()
        filename = "{}.json".format(self.__class__.__name__)
        with open(filename, 'w') as f:
            f.write(self.to_json_string())
        return self.to_dict()

    def to_dict(self):
        """returns a dictionary of the Amenity object"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    @staticmethod
    def load_from_file(file_name):
        """returns a list of Amenity objects"""
        with open(file_name, 'r') as f:
            return [Amenity.from_json_string(line) for line in f]

    @classmethod
    def from_json_string(cls, json_string):
        """returns a Amenity object from a json string"""
        return cls.from_dict(json.loads(json_string))

    @classmethod
    def from_dict(cls, dict):
        """returns a Amenity object from a dictionary"""
        return cls(**dict)

    @classmethod
    def create(cls, **kwargs):
        """returns a Amenity object"""
        return cls(**kwargs)

    @classmethod
    def load_from_file(cls, file_name):
        """returns a list of Amenity objects"""
        with open(file_name, 'r') as f:
            return [cls.from_json_string(line) for line in f]
