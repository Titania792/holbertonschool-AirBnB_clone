#!/usr/bin/python3
"""contains the entry point of the command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""

    prompt = '(hbnb)'

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
        if self.__class__.__name__ is False:
            print("** class doesn't exist **")

    def do_show(self, args):
        pass

    def do_destroy(self, args):
        pass

    def do_all(self, args):
        pass

    def do_update(self, args):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
