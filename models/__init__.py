#!/usr/bin/python3
""" reload object init """


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
