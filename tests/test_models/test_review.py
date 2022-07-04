#!/usr/bin/python3
""" tests for the class review """


import unittest
import models
from models.review import Review
from models.base_model import BaseModel
from models import storage


class TestReview(unittest.TestCase):
    """ tests for the class review """

    def test_subclass(self):
        """checks if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_instance(self):
        """ checks if an instance of Review is created """
        rw = Review()
        rw1 = Review()
        self.assertNotEqual(rw.id, rw1.id)
        self.assertNotEqual(rw.created_at, rw1.created_at)
        self.assertNotEqual(rw.updated_at, rw1.updated_at)
        self.assertIn(rw, storage.all().values())
        self.assertIn(rw1, storage.all().values())
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")

    def test_attributes(self):
        """ checks if the attributes are correct """
        my_review = Review()
        self.assertEqual(my_review.place_id, "")
        self.assertEqual(my_review.user_id, "")
        self.assertEqual(my_review.text, "")


if __name__ == '__main__':
    unittest.main()
