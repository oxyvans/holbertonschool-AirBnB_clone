#!/usr/bin/python3
""" Unittest for all the methods of the class FileStorage
Check pycodestyle "PEP8" for the complete module """
import unittest
import pycodestyle
from models.engine.file_storage import FileStorage


class TestAmenityModule(unittest.TestCase):
    """ A class to test FileStorage Module """
    def test_pycodestyle_pep8(self):
        """ Style code meets PEP8 """
        style = pycodestyle.StyleGuide(quit=True)
        check = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(
            check.total_errors, 0,
            'PEP8 style errors: %d' % check.total_errors)
