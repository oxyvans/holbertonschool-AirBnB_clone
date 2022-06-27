#!/usr/bin/python3
""" base model create """

import uuid
import datetime

class BaseModel():
    """ base modles """

    def __init__(self, *args, **kwargs):
        """ init method """
        if (kwargs == None)
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()  
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ retrun string """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ savee """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ to dict """
        res = self.__dict__
        res["__class__"] = self.__class__.__name__
        res["created_at"] = self.created_at.isoformat()
        res["updated_at"] = self.updated_at.isoformat()
        return res
