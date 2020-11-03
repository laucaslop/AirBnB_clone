#!/usr/bin/pyhton3
"""Let's import the modules"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """ Base Model Class """

    def __init__(self, *args, **kwargs):
        """ Initialize Public Attributes """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    if key != '__class__':
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        def __str__(self):
            """ Print the str representation """
            return "[{}] [{}] [{}]".foramt(
                self.__class__.name__, self.id, self.__dict__)

        def save(self):
            """ saving and updating the public instance into storage """
            self. updated_at = datetime.now()
            models.storage.save()

        def to_dict(self):
            """ create a dictionary from an instance """
            new_dict["__class__"] = self.__class__.__name__
            new_dict["updated_at"] = new_dict["updated_at"].isoformat()
            new_dict['created_at'] = new_dict["created_at"].isoformat()

            return new_dict
