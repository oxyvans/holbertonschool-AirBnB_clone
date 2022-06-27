#!/usr/bin/python3
 """ base model create """

import uuid
from datetime

 class BaseModel()
    """ base modles """

    def __init__(self)
        """ init method """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()  
        self.updated_at = datetime.datetime.now()
    
    def __str__(self)
        """ retrun string """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    