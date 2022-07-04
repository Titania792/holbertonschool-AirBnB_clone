#!/usr/bin/python3
""" Tests for User class """


import unittest
import models
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):
    """ Tests for the class methods """

    def test_subclass(self):
        """ checks is User is a subclass of BaseModel """
        self.assertTrue(issubclass(User, BaseModel))

    def test_instance(self):
        """ checks if an instance of User is created """
        ur = User()
        ur1 = User()
        self.assertNotEqual(ur.id, ur1.id)
        self.assertNotEqual(ur.created_at, ur1.created_at)
        self.assertNotEqual(ur.updated_at, ur1.updated_at)
        self.assertIn(ur, storage.all().values())
        self.assertIn(ur1, storage.all().values())
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

    def test_attr(self):
        """ checks if the attributes are correct """
        my_User = User()
        self.assertEqual(my_User.email, "")
        self.assertEqual(my_User.password, "")
        self.assertEqual(my_User.first_name, "")
        self.assertEqual(my_User.last_name, "")


if __name__ == '__main__':
    unittest.main()
