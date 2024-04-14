#!/usr/bin/python3
"""File Storage"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """File Storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """All Method"""

        return FileStorage.__objects

    def new(self, obj):
        """New Method"""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Save Method"""

        with open(FileStorage.__file_path, "w") as file:
            ser_objects = {}
            for key, value in FileStorage.__objects.items():
                ser_objects[key] = value.to_dict()
            json.dump(ser_objects, file)

    def reload(self):
        """Reload Method"""

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    obj_dict = value
                    class_ = BaseModel
                    obj = class_(**obj_dict)
                    FileStorage.__objects[key] = obj
