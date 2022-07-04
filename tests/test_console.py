#!/usr/bin/python3
""" tests for the console """


from console import HBNBCommand
import unittest


class Test_console(unittest.TestCase):
    """ tests for the console """

    def test_prompt(self):
        """ checking prompt """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_do_EOF(self):
        """ checking do_EOF """
        self.assertEqual(True, HBNBCommand().do_EOF(None))
