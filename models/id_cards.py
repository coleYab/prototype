#!/usr/bin/env python3

from models import storage
from models.base_model import BaseModel

class IdCards(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
    def set_found(self):
        self.is_found = True

