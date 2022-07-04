#!/usr/bin/python3
""" tests for the class City """


import unittest
import models
from models.city import City
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ tests for the class City """

    def test_subclass(self):
        """ checks if City is a subclass of BaseModel """
        self.assertTrue(issubclass(City, BaseModel))

    def test_inst(self):
        """ checks if an instance of City is created """
        cy = City()
        cy1 = City()
        self.assertNotEqual(cy.id, cy1.id)
        self.assertNotEqual(cy.created_at, cy1.created_at)
        self.assertNotEqual(cy.updated_at, cy1.updated_at)
        self.assertIn(cy, storage.all().values())
        self.assertIn(cy1, storage.all().values())
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")

    def test_attributes(self):
        """ checks if the attributes are correct """
        my_city = City()
        self.assertEqual(my_city.state_id, "")
        self.assertEqual(my_city.name, "")


if __name__ == '__main__':
    unittest.main()
