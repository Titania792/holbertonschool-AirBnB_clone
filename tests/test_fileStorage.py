#!/usr/bin/python3
""" testing fileStorage """

from models.engine.file_storage import FileStorage
import unittest


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

    if __name__ == '__main__':
        unittest.main()
