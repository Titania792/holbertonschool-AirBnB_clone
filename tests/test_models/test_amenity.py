#!/usr/bin/python3
""" tests for the class Amenity """


import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage


class TestAmenity(unittest.TestCase):
    """ tests for the class Amenity """

    def test_subclass(self):
        """ checks if the class is a subclass of BaseModel """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_instance(self):
        """ checks if an instance of Amenity is created """
        am = Amenity()
        am1 = Amenity()
        self.assertNotEqual(am.id, am1.id)
        self.assertNotEqual(am.created_at, am1.created_at)
        self.assertNotEqual(am.updated_at, am1.updated_at)
        self.assertIn(am, storage.all().values())
        self.assertIn(am1, storage.all().values())
        self.assertEqual(Amenity.name, "")

    def test_attributes(self):
        """ checks if the attributes are correct """
        a = Amenity()
        self.assertEqual(a.name, "")


if __name__ == '__main__':
    unittest.main()
