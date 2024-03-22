#!/usr/bin/python3
"""Function that defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Representation of a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
