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
import shlex
import sys
import json


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

    def do_EOF(self, arg):
        """EOF exit the program"""
        return True

    def do_create(self, args):
        """Creates a new instance of an object"""
        if args is not None and args != "":
            listt = args.split()
            if listt[0] not in self.classes:
                print("** class doesn't exist **")
                return
            else:
                gett = getattr(sys.modules[__name__], listt[0])
                newinst = gett()
                newinst.save()
                print(newinst.id)
        else:
            print("** class name missing **")
            return

    def do_show(self, args):
        """Prints the string representation of an instance based on
        the class name and id"""
        if args is not None and args != "":
            listt = args.split()
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
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        """if args is not None and args != "":
            listt = args.split()
            if listt[0] not in self.classes:
                print("** class doesn't exist **")
                return
            if len(listt) == 1:
                print("** instance id missing **")
                return
            key = f"{listt[0]}.{listt[1]}"
            if key in storage.all():
                del storage.all()[key]
            else:
                print("** no instance found **")
                return
        else:
            print("** class name missing **")
            return"""
        if len(args) < 1:
            print("** class name missing **")
        else:
            a_list = args.split()
            if len(a_list) == 1:
                if a_list[0] in self.classes:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            else:
                if a_list[0] in self.classes:
                    aux_dict = storage.all()
                    key = f"{a_list[0]}.{a_list[1]}"
                    if key in aux_dict:
                        del aux_dict[key]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

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
        listt = shlex.split(args)
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

    def do_count(self, args):
        """ Retrieve number of instances """
        count = 0
        listt = args.split()
        for key in storage.all():
            if listt[0] in key:
                count += 1
        print(count)

    def default(self, args):
        """ Advanced commands """
        listt = args.split('.')
        if len(listt) == 2:
            if listt[1] == "all()":
                self.do_all(listt[0])
            elif listt[1] == "count()":
                self.do_count(listt[0])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
