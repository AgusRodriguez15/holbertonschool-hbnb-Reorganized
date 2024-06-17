#!/usr/bin/python3
from datetime import datetime
import uuid
from PrimaryKeys import PrimaryKeys


"""
Create class City
"""


class City:
    def __init__(self, longitude, latitude, name, country):
        super().__init__(uuid.uuid4(), datetime.now(), datetime.now())
        self.longitude = self.validate_latitudeANDlongitude(longitude)
        self.latitude = self.validate_latitudeANDlongitude(latitude)
        self.name = name 
        
    def validate_latitudeANDlongitude(self, value):
        if not isinstance(value, float) or value <= 0:
            raise ValueError("Number must be positive")
        return value