"""
Client Base module.
"""
from __future__ import annotations

from abc import abstractmethod


class Client:
    """
    Base Client class interface.

    A client handles the lifeciycle of an object during a coding session.
    It manages the creation, reading, updating and deleting of objects and comes
    into 2 subclasses: Local and DHCore.
    """

    @abstractmethod
    def create_object(self, obj: dict, api: str) -> dict:
        """
        Create object method.
        """

    @abstractmethod
    def read_object(self, api: str) -> dict:
        """
        Read object method.
        """

    @abstractmethod
    def update_object(self, obj: dict, api: str) -> dict:
        """
        Update object method.
        """

    @abstractmethod
    def delete_object(self, api: str) -> dict:
        """
        Delete object method.
        """

    @staticmethod
    @abstractmethod
    def is_local() -> bool:
        """
        Flag to check if client is local.
        """
