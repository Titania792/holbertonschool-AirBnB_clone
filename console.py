#!/usr/bin/python3
"""contains the entry point of the command interpreter"""


import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""

    prompt = '(hbnb)'

    classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
               "City": City, "Place": Place, "State": State, "Review": Review}

    def emptyline(self):
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        raise SystemExit

    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
        print(f"Hello, {name}")

    def do_EOF(self, arg):
        """EOF exit the program"""
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        if args == 0:
            print("** class name missing **")
        elif args == 1 in self.classes:
            pass
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based on
        the class name and id"""
        pass

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        pass

    def do_all(self, args):
        """Prints all string representation of all instances based
        or not on the class name"""
        pass

    def do_update(self, args):
        """Updates an instance based on the class name and id by
        adding or updating attribute"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
