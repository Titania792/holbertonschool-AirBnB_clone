#!/usr/bin/python3
""" testing fileStorage """

import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
from models import storage


class test_fileStorage(unittest.TestCase):
    """Test FileStorage Class"""

    def test_instances(self):
        """checking that instances are correct"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_docs(self):
        """checking correct docstring"""
        obj = FileStorage()
        self.assertTrue(obj.__doc__)
        self.assertIsNotNone(obj.all.__doc__)
        self.assertIsNotNone(obj.new.__doc__)
        self.assertIsNotNone(obj.save.__doc__)
        self.assertIsNotNone(obj.reload.__doc__)

    def test_new(self):
        """ checking new method """
        obj = FileStorage()
        base = BaseModel()
        base.name = "Holberton"
        bmid = base.id
        storage.new(base)
        self.assertIsNotNone(
            storage.all()[base.__class__.__name__ + "." + bmid])

    def test_all(self):
        """ checking all method """
        base = BaseModel()
        srg = storage.all()
        self.assertIsNotNone(srg)
        self.assertEqual(srg, storage.all())
        self.assertIs(srg, storage.all())

    def test_reload(self):
        """ checking reload method """
        obj = FileStorage()
        obj.reload()
        self.assertIsNotNone(obj.all())
        self.assertIs(obj.all(), obj.all())

    def test_save(self):
        """ checking save method """
        obj = FileStorage()
        base = BaseModel()
        base.name = "Holberton"
        bmid = base.id
        storage.new(base)
        storage.save()
        with open('file.json', 'r') as f:
            self.assertIsNotNone(f.read())
        self.assertIsNotNone(
            storage.all()[base.__class__.__name__ + "." + bmid])

    def test_save_reload(self):
        """ checking save and reload method """
        obj = FileStorage()
        base = BaseModel()
        base.name = "Holberton"
        bmid = base.id
        storage.new(base)
        storage.save()
        storage.reload()
        self.assertIsNotNone(
            storage.all()[base.__class__.__name__ + "." + bmid])

    if __name__ == '__main__':
        unittest.main()
