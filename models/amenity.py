#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Represents a type of amenity.

    Attributes:
        amenity_name (str): The name of the amenity.
    """

    amenity_name = ""
