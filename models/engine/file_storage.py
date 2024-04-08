#!/usr/bin/python3
"""File Storage"""
import json
import os


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
            for key, value in FileStorage.__objects.items():
                json.dump(FileStorage.__objects, file)

    def reload(self):
        """Reload Method"""

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                FileStorage.__objects = json.load(file)
