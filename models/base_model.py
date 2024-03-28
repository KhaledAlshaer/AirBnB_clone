#!/usr/bin/python3
"""Base class"""
import uuid
import datetime


class BaseModel:
    """Base Model class"""

    def __init__(self, *args, **kwargs):
        """constructor"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """str method"""

        return "[{}] ({}) {}" .format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """update updated_at"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """to dict method"""

        mydict = self.__dict__.copy()
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict["__class__"] = self.__class__.__name__
        return mydict
