#!/usr/bin/python3
"""contains the entry point of the command interpreter"""


from models.base_model import BaseModel
from models.review import Review
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.user import User
from models import storage
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""

    prompt = '(hbnb) '

    classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
               "City": City, "Place": Place, "State": State, "Review": Review}

    def emptyline(self):
        """ Don't execute anything if an empty line + enter are typed """
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
        """Creates a new instance of an object"""
        listt = args.split()
        if len(listt) == 0:
            print("** class name missing **")
            return
        if listt[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            new_obj = self.classes[listt[0]]()
            storage.new(new_obj)
            print(eval(new_obj.__class__.__name__ + "()").id)

    def do_show(self, args):
        """Prints the string representation of an instance based on
        the class name and id"""
        listt = args.split()
        if len(listt) == 0:
            print("** class name missing **")
            return
        if listt[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(listt) == 1:
            print("** instance id missing **")
            return
        key = listt[0] + "." + listt[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        listt = args.split()
        if len(listt) == 0:
            print("** class name missing **")
            return
        if listt[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(listt) == 1:
            print("** instance id missing **")
            return
        key = listt[0] + "." + listt[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]

    def do_all(self, args):
        """Prints all string representation of all instances based
        or not on the class name"""
        listt = args.split()
        if len(listt) == 1 and listt[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(listt) == 1 and listt[0] in self.classes:
            print([str(i) for i in storage.all().values() if
                   i.__class__.__name__ == listt[0]])
        else:
            print([str(i) for i in storage.all().values()])

    def do_update(self, args):
        """Updates an instance based on the class name and id by
        adding or updating attribute"""
        listt = args.split()
        if len(listt) == 0:
            print("** class name missing **")
            return
        if listt[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(listt) == 1:
            print("** instance id missing **")
            return
        key = listt[0] + "." + listt[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(listt) == 2:
            print("** attribute name missing **")
            return
        if len(listt) == 3:
            print("** value missing **")
            return
        storage.all()[key].__dict__[listt[2]] = listt[3]
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
