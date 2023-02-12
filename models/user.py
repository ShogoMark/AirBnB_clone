#!/usr/bin/python3
""" User module that creates a new user """
from models.base_model import BaseModel


class User(BaseModel):
    """ Defines a class User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
