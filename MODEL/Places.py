#!/usr/bin/python3
from datetime import datetime
import uuid
from PrimaryKeys import PrimaryKeys

"""
Create class Place
"""


class Place(PrimaryKeys):
    """Class for Place entity"""

    assigned_hosts = {}
    
    def __init__(self, amenities, host, city, reviews):
        super().__init__()
        self.amenities = amenities
        self.host = host
        self.city = city
        self.reviews = reviews 
        
        if host in Place.assigned_hosts:
            raise ValueError(f"El host '{host}' ya existe en Place.")