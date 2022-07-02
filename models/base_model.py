#!/usr/bin/python3
""" base model create """


import uuid
from datetime import datetime
import models


class BaseModel():
    """ base modles """

    def __init__(self, *args, **kwargs):
        """ init method """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self,
                                key,
                                datetime.strptime(value,
                                                  "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """ retrun string """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ savee """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ to dict """
        res = dict(self.__dict__)
        res["__class__"] = self.__class__.__name__
        res["created_at"] = self.created_at.isoformat()
        res["updated_at"] = self.updated_at.isoformat()
        return res
