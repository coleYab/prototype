#!/usr/bin/env python3
"""
Model package
"""

from models.engine.file_storage import FileEngine

storage = FileEngine('file.json')
storage.reload()
