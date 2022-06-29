#!/usr/bin/python3
""" Serializes instances to a JSON file and deserializes JSON file
    to instances """


from models.base_model import BaseModel
import json


class FileStorage:
    """ Class that serializes instances to a JSON file and
    deserializes JSON file """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Return the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        all_dict = {}
        for key, value in self.__objects.items():
            str_to_dict = value.to_dict()
            all_dict[key] = str_to_dict
        with open(self.__file_path, 'w') as MyFile:
            json.dump(all_dict, MyFile)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, 'r') as MyFile:
                to_dict = json.load(MyFile)
                for key, value in to_dict.items():
                    to_obj = BaseModel(**value)
                    self.__objects[key] = to_obj
        except FileNotFoundError:
            return
