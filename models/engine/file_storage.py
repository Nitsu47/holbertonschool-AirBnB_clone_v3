#!/usr/bin/python3
"""This module defines the FileStorage class"""
import json
from models.base_model import BaseModel

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
                for key, value in FileStorage.__objects.items():
                    cls_name = value['__class__']
                    cls = eval(cls_name)
                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Deletes the object from __objects if it exists """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def get(self, cls, id):
        """ Retrieves an object """
        all_objs = self.all()
        for obj_key, obj in all_objs.items():
            if obj.id == id and type(obj) == cls:
                return obj
        return None

    def count(self, cls=None):
        """ Counts the number of objects in storage """
        if cls:
            count = 0
            for obj_key in self.__objects:
                if type(self.__objects[obj_key]) == cls:
                    count += 1
            return count
        else:
            return len(self.__objects)

