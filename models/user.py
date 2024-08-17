#!/usr/bin/env python3

from models import storage
from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs is None or len(kwargs.keys()) == 0:
            self.found_ids = []
    
    def add_found_id(self, id_card):
        self.found_ids.append(f"{id_card.__class__.__name__}.{id_card.id}")

    def remove_found_id(self, id_card):
        key = f"{id_card.__class__.__name__}.{id_card.id}"
    
        if key not in self.found_ids:
            storage.show(self.__class__.__name__, id_card.id).set_found()
