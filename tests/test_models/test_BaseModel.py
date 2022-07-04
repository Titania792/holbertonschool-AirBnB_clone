#!/usr/bin/python3
""" Testing BaseModel """

from time import sleep
import unittest
from models.base_model import BaseModel
from datetime import datetime


class test_basemodel(unittest.TestCase):
    """ Test BaseModel Class """

    def test_basemodel_init(self):
        """ checking BaseModel init """
        bm = BaseModel()
        self.assertEqual(bm.id, str(bm.id))
        self.assertEqual(str(bm.created_at), str(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")))
        self.assertEqual(str(bm.updated_at), str(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")))

    def test_basemodel_str(self):
        """ checking BaseModel str """
        bm = BaseModel()
        self.assertEqual(
            str(bm), "[BaseModel] ({}) {}".format(bm.id, bm.__dict__))

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


if __name__ == '__main__':
    unittest.main()
