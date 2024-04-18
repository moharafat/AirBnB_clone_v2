#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from os import getenv

how_to_store = getenv('HBNB_TYPE_STORAGE', 'db')

if how_to_store == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
