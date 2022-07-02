#!/usr/bin/python3
""" Serializes instances to a JSON file and deserializes JSON file
    to instances """


from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
import os
import json


class FileStorage:
    """ Class that serializes instances to a JSON file and deserializes
    JSON file """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        all_dict = {}
        for key in self.__objects:
            all_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as MyFile:
            json.dump(all_dict, MyFile)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:    
            with open(self.__file_path, 'r') as MyFile:
                self.__objects = json.load(MyFile)
        except FileNotFoundError:
            pass
