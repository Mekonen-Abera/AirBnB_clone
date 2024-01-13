#!/usr/bin/python3
"""Defining the State classes """
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state class

    Attributes:
        name (str): The name of the state.
    """

    name = ""
