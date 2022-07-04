#!/usr/bin/python3
""" tests for the class State """


from models.state import State
from models.base_model import BaseModel
import unittest
import models
from models import storage


class TestState(unittest.TestCase):
    """ tests for the class State """

    def test_subclass(self):
        """ checks if state is a subclass of BaseModel """
        self.assertTrue(issubclass(State, BaseModel))

    def test_instance(self):
        """ checks if an instance of State is created """
        st = State()
        st1 = State()
        self.assertNotEqual(st.id, st1.id)
        self.assertNotEqual(st.created_at, st1.created_at)
        self.assertNotEqual(st.updated_at, st1.updated_at)
        self.assertIn(st, storage.all().values())
        self.assertIn(st1, storage.all().values())
        self.assertEqual(State.name, "")

    def test_attr(self):
        """ checks if the attributes are correct """
        my_state = State()
        self.assertEqual(my_state.name, "")


if __name__ == '__main__':
    unittest.main()
