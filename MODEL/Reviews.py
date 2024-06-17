#!/usr/bin/python3
from datetime import datetime
import uuid
from PrimaryKeys import PrimaryKeys


"""
Create class Reviews
"""


class Reviews(PrimaryKeys):
    def __init__(self, place_id, user_id, rating, comment):
        super().__init__(uuid.uuid4(), datetime.now(), datetime.now())
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment