#!/usr/bin/python3
"""This module defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_of_rooms (int): The number of rooms of the place.
        number_of_bathrooms (int): The number of bathrooms of the place.
        max_guests (int): The maximum number of guests of the place.
        price_per_night (int): The price by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_of_rooms = 0
    number_of_bathrooms = 0
    max_guests = 0
    price_per_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
