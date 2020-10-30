#!/usr/bin/python3
""" Import the modules need it for this storage """

import json
import models.base_model import BaseModel
"""Future models to import in the project"""
import models.user import User
from models.place import Place
from models.state import State
from models.city import City
from moels.amenity import Amenity
from models.review import review


class FileStorage:
    """ File Storage Class"""
    """FileStorage that serializes instances to a JSON file"""
    """and deserializes JSON file to instances"""
    __file_path = "file.json"
    __obejects = {}

    def all(self):
        """public instance return  dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """ public instance taht sets in __obejects the obj with key """
        key = type(obj).__name__ + "." + str(obj.id)
        FileStorage.__obejects[key] = obj

    def save(self):
        """public instance that serializes __objects"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8")
        data = json.dumps(new_dict)
