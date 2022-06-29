#!/usr/bin/env python3
""" file storage """


import jsno
import models.base_model import BaseModel

class FileStorage:
    """ filestorage """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return objects """
        return self.__objects

    def new(self, obj):
        """ set a new objects """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """ save a jsno """


    def reload(self):
        """ reload jsno """
