#!/usr/bin/python3
""" base model create """


import uuid
import datetime
import models


class BaseModel():
    """ base modles """

    def __init__(self, *args, **kwargs):
        """ init method """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()  
        self.updated_at = datetime.datetime.now()

        if (kwargs == None):
            for k, value in kwargs.items():
                if k == "updated_at" or k == "created_at":
                    value = datetime.strptime(value, "Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, key, value)

        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """ retrun string """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ savee """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ to dict """
        res = self.__dict__
        res["__class__"] = self.__class__.__name__
        res["created_at"] = self.created_at.isoformat()
        res["updated_at"] = self.updated_at.isoformat()
        return res
