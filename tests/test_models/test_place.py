#!/usr/bin/python3
""" tests for the class Place """


import unittest
import models
from models.place import Place
from models.base_model import BaseModel
from models import storage


class TestPlace(unittest.TestCase):
    """ tests for the class Place """

    def test_subclass(self):
        """ checks if Place is a subclass of BaseModel """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_instance(self):
        """ checks if an instance of Place is created """
        pl = Place()
        pl1 = Place()
        self.assertNotEqual(pl.id, pl1.id)
        self.assertNotEqual(pl.created_at, pl1.created_at)
        self.assertNotEqual(pl.updated_at, pl1.updated_at)
        self.assertIn(pl, storage.all().values())
        self.assertIn(pl1, storage.all().values())
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, ())

    def test_attributes(self):
        """ checks if the attributes are correct """
        my_place = Place()
        self.assertEqual(my_place.city_id, "")
        self.assertEqual(my_place.user_id, "")
        self.assertEqual(my_place.name, "")
        self.assertEqual(my_place.description, "")
        self.assertEqual(my_place.number_rooms, 0)
        self.assertEqual(my_place.number_bathrooms, 0)
        self.assertEqual(my_place.max_guest, 0)
        self.assertEqual(my_place.price_by_night, 0)
        self.assertEqual(my_place.latitude, 0.0)
        self.assertEqual(my_place.longitude, 0.0)
        self.assertEqual(my_place.amenity_ids, ())


if __name__ == '__main__':
    unittest.main()
