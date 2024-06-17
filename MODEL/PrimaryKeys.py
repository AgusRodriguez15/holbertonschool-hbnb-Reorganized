#!/usr/bin/python3
import datetime
import uuid


"""
Create class PrimaryKeys
"""


class PrimaryKeys:
    def __init__(self, id, crate_at, update_at):
        self.id = uuid.uuid4()
        self.create_at = datetime.datetime.now()
        self.update_at = datetime.datetime.now()
        