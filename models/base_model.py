#!/usr/bin/env python3

from models import storage
from datetime import datetime
from uuid import uuid4

class BaseModel:
    def __init__(self, *args, **kwargs) -> None:
        if kwargs is not None and len(kwargs.keys()) != 0:
            for key, val in kwargs.items():
                if key != '__class__':
                    self.__setattr__(key, val)
            return

        self.id = str(uuid4())
        self.updated_at = datetime.now().isoformat()
        self.created_at = datetime.now().isoformat()
        self.save()

    def __str__(self):
        return f"[{self.__class__.__name__}] (<{self.id}>) <{self.__dict__}>"

    def save(self):
        self.updated_at = datetime.now().isoformat()
        storage.save(self)

    def to_dict(self):
        diction = self.__dict__.copy()
        diction['__class__'] = self.__class__.__name__
        return diction

    def update(self, dict_reper):
        for key, val in dict_reper:
            if key not in self.__dict__.keys():
                raise Exception("Unable to update property doesn't exists")
            self.__setattr__(key, val)
    