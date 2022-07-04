#!/usr/bin/python3
""" Unittest for all the methods of the class Base
Check pycodestyle "PEP8" for the complete module """
import unittest
import pycodestyle
from models.base_model import BaseModel
import models


base_model1 = BaseModel()
base_model2 = BaseModel()

class TestBaseModule(unittest.TestCase):
    """ A class to test Base Module """

    def test_pycodestyle_pep8(self):
        """ Style code meets PEP8 """
        style = pycodestyle.StyleGuide(quit=True)
        check = style.check_files(['models/base_model.py'])
        self.assertEqual(
            check.total_errors, 0,
            'PEP8 style errors: %d' % check.total_errors)

    def test_uuid(self):
        """ Test uuid """
        self.assertTrue(hasattr(base_model1, "id"))
        self.assertNotEqual(base_model1.id, base_model2.id)
        self.assertEqual(type(base_model1.id), str)
        self.assertEqual(type(base_model2.id), str)

    def test_save(self):
        """ Test save method """
        old_updete = base_model1.updated_at
        base_model1.save()
        new_updete = base_model1.updated_at
        self.assertTrue(old_updete != new_updete)

    def test_update(self):
        """ Test update functionality """
        base_model1.name = "Guillaume"
        self.assertTrue(hasattr(base_model1, "name"))

    def test_init_kwargs(self):
        """ Test init with kwargs """
        base_model1.name = "Guillaume"
        json_model = base_model1.to_dict()
        base_model3 = BaseModel(**json_model)
        self.assertDictEqual(json_model, base_model3.to_dict())
        self.assertIn("name", base_model3.to_dict())
        self.assertIsNot(base_model1, base_model3)

    def test_storage(self):
        """ Test staorage"""
        objs_dict_rep = models.storage.all()
        self.assertTrue(objs_dict_rep)
