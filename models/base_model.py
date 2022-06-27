#!/usr/bin/python3
""" base model create """

import uuid
import datetime

class BaseModel():
    """ base modles """

    def __init__(self):
        """ init method """
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
        self.created_at = datetime.datetime.now().isoformat()  
        self.updated_at = datetime.datetime.now().isoformat()
        res = self.__dict__
        res["__class__"] = "BaseModel"
        return res
