#!/usr/bin/python3
""" tests for the console """


from console import HBNBCommand
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
import os
from os.path import exists


class Test_console(unittest.TestCase):
    """ tests for the console """

    def test_prompt(self):
        """ checking prompt """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_do_EOF(self):
        """ checking do_EOF """
        self.assertEqual(True, HBNBCommand().do_EOF(None))

    def test_do_quit(self):
        """ checking do_quit """
        with self.assertRaises(SystemExit):
            HBNBCommand().do_quit(None)

    def test_do_create(self):
        """ checking do_create """
        HBNBCommand().do_create("BaseModel")
        self.assertTrue(exists("BaseModel.json"))
        HBNBCommand().do_create("BaseModel")
        self.assertTrue(exists("BaseModel2.json"))
        HBNBCommand().do_create("BaseModel")
        self.assertTrue(exists("BaseModel3.json"))

    def test_do_all(self):
        """ checking do_all """
        HBNBCommand().do_create("BaseModel")
        HBNBCommand().do_create("BaseModel")
        HBNBCommand().do_all("BaseModel")
        self.assertTrue(exists("BaseModel.json"))
        self.assertTrue(exists("BaseModel2.json"))
