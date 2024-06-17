#!/usr/bin/python3
from datetime import datetime
import uuid
import re
from PrimaryKeys import PrimaryKeys


"""
Create class Users
"""


class Users:
    
    registered_emails = {}
    
    def __init__(self, email, first_name, last_name):
        super().__init__()
        self.email = self.validate_email(email)
        self.first_name = first_name
        self.last_name = last_name
        
        if self.email in Users.registered_emails:
            raise ValueError(f"El email '{self.email}' ya está registrado.")

        Users.registered_emails[self.email] = self
    
    @staticmethod
    def validate_email(email):
        formatoValido = r"^([a-z0-9]+[-_.])*[a-z0-9]+@[a-z0-9]+(\.[a-z] {2,})+$"
        if re.match(formatoValido, email, re.IGNORECASE):
            return True
        return False
    