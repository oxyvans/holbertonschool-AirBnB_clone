#!/usr/bin/env python3
""" file storage """


import json
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User

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
        aux = {}
        for key in self.__objects:
            aux[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(aux, f)


    def reload(self):
        """ reload jsno """
        try:
            with open(self.__objects, "w") as f:
                dic = json.load(f)

        except FileNotFoundError:
            pass
