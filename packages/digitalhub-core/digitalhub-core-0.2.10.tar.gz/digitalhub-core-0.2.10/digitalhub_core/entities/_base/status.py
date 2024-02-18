"""
Status class module.
"""
from __future__ import annotations

from enum import Enum

from digitalhub_core.entities._base.base import ModelObj


class State(Enum):
    """
    State enumeration.
    """

    BUILT = "BUILT"
    COMPLETED = "COMPLETED"
    CREATED = "CREATED"
    ERROR = "ERROR"
    IDLE = "IDLE"
    PENDING = "PENDING"
    READY = "READY"
    RUNNING = "RUNNING"
    STOP = "STOP"


class Status(ModelObj):
    """
    Base Status class.
    """

    def __init__(self, state: str, message: str | None = None) -> None:
        """
        Constructor.

        Parameters
        ----------
        state : str
            The state of the entity.
        message : str
            Error message.
        """
        self.state = state
        self.message = message

    @classmethod
    def from_dict(cls, obj: dict) -> "Status":
        """
        Return entity specification object from dictionary.

        Parameters
        ----------
        obj : dict
            A dictionary containing the attributes of the entity specification.

        Returns
        -------
        EntitySpec
            An entity specification object.
        """
        return cls(**obj)
