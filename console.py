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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
