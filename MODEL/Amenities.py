#!/usr/bin/python3
from datetime import datetime
import uuid
from PrimaryKeys import PrimaryKeys


"""
Create class PrimaryKeys
"""


class Amenities(PrimaryKeys):
    def __init__(self, name, adress, description, num_rooms, num_bathrooms, price_X_night, max_guests):
        super().__init__(uuid.uuid4(), datetime.now(), datetime.now())
        self.name = name
        self.adress = adress
        self.description = description
        self.num_rooms = self.validate_numbers(num_rooms)
        self.num_bathrooms = self.validate_numbers(num_bathrooms)
        self.price_X_night = self.validate_Price(price_X_night)
        self.max_guests = self.validate_numbers(max_guests)
        
    def validate_numbers(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Number must be positive")
        return value
    
    def validate_Price(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Number must be positive")
        return value
    
    
        
        