#!/usr/bin/python3
"""Base class"""
import uuid
import datetime


class BaseModel:
    """Base Model class"""

    tformat = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """constructor"""

        if kwargs:
            for name, value in kwargs.items():
                if name == "__class__":
                    pass
                elif name == "created_at" or name == "updated_at":
                    value = datetime.datetime.strptime(value, tformat)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.datetime.today()
                    self.updated_at = datetime.datetime.today()

    def __str__(self):
        """str method"""

        return "[{}] ({}) {}" .format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """update updated_at"""
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        """to dict method"""

        mydict = self.__dict__.copy()
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict["__class__"] = self.__class__.__name__
        return mydict
