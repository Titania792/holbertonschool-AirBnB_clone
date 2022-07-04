#!/usr/bin/python3
""" Testing BaseModel """

from time import sleep
import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage
import os


class test_basemodel(unittest.TestCase):
    """ Test BaseModel Class """

    def test_basemodel_save(self):
        """ checking BaseModel save """
        bm = BaseModel()
        bm.save()
        sleep(0.1)
        bm.save()
        self.assertNotEqual(bm.created_at, bm.updated_at)

    def test_basemodel_to_dict(self):
        """ checking BaseModel to_dict """
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertEqual(type(bm_dict["created_at"]), str)
        self.assertEqual(type(bm_dict["updated_at"]), str)
        self.assertEqual(bm_dict["id"], bm.id)
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_basemodel_to_dict_with_kwargs(self):
        """ checking BaseModel to_dict with kwargs """
        dict = {"name": "Holberton", "age": 89, "id": "0"}
        bm = BaseModel(**dict)
        self.assertEqual(bm.id, "0")
        self.assertEqual(bm.name, "Holberton")
        self.assertEqual(bm.age, 89)
        self.assertEqual(bm.__dict__, dict)

    def test_doc(self):
        """ checking BaseModel docstring """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_datetime(self):
        """ checking datetime """
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_id(self):
        """ checking id """
        bm = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm.id, str)
        self.assertNotEqual(bm.id, bm2.id)
        self.assertFalse(bm.id == bm2.id)

    def test_inst(self):
        """ checks if the instances of BaseModel are correctly created"""
        bm = BaseModel()
        bm1 = BaseModel()
        self.assertNotEqual(bm.id, bm1.id)
        self.assertNotEqual(bm.created_at, bm1.created_at)
        self.assertNotEqual(bm.updated_at, bm1.updated_at)
        self.assertIn(bm, storage.all().values())
        self.assertIn(bm1, storage.all().values())

    def test_attr(self):
        """checks the types of the attributes"""
        bm = BaseModel()
        bm.name = "Holberton"
        bm.age = 89
        self.assertIs(datetime, type(bm.updated_at))
        self.assertIs(datetime, type(bm.created_at))
        self.assertIs(str, type(bm.id))
        self.assertEqual(int, type(bm.age))
        self.assertIn(bm.name, bm.to_dict().values())

    def test__str__(self):
        """ checks the __str__ method """
        bm = BaseModel()
        self.assertEqual(
            f"[{type(bm).__name__}] ({bm.id}) {bm.__dict__}", str(bm))

    def test_save(self):
        """ checks the save method """
        bm = BaseModel()
        updated_at = bm.__dict__['updated_at']
        bm.save()
        self.assertNotEqual(bm.__dict__['updated_at'], updated_at)
        self.assertTrue(os.path.isfile('file.json'))
        new_updated_at = bm.__dict__['updated_at']
        storage.reload()
        self.assertEqual(bm.__dict__['updated_at'], new_updated_at)
        bm1 = BaseModel()
        updated_at = bm1.__dict__['updated_at']
        bm1.save(self)
        self.assertNotEqual(bm1.__dict__['updated_at'], updated_at)
        self.assertTrue(os.path.isfile('file.json'))
        new_updated_at = bm1.__dict__['updated_at']
        storage.reload()
        self.assertEqual(bm1.__dict__['updated_at'], new_updated_at)
        

    def test_to_dict(self):
        """ checkss to_dict method """
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict["id"], bm.id)
        self.assertEqual(bm_dict["created_at"], bm.created_at.isoformat())
        self.assertEqual(bm_dict["updated_at"], bm.updated_at.isoformat())
        self.assertEqual(bm_dict['__class__'], bm.__class__.__name__)


if __name__ == '__main__':
    unittest.main()
