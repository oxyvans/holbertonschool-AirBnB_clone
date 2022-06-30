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

clases = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
            "Place": Place, "Review": Review, "State": State, "User": User}


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
            with open(self.__file_path, "r") as f:
                dict_ = json.load(f)
            for key in dict_:
                self.__objects[key] = clases[dict_[key]["__class__"]](**dict_[key])
        except FileNotFoundError:
            pass
