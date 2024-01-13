#!/usr/bin/python3
"""Defining the Amenity classes"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity class

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
