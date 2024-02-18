"""
Client builder module.
"""
from __future__ import annotations

import typing

from digitalhub_core.client.objects.dhcore import ClientDHCore
from digitalhub_core.client.objects.local import ClientLocal

if typing.TYPE_CHECKING:
    from digitalhub_core.client.objects.base import Client


class ClientBuilder:
    """
    The client builder class.

    It implements the builder pattern to create a client instance.
    The client builder can be used to create a local or non-local client instance.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        self._local = None
        self._dhcore = None

    def build(self, local: bool = False) -> Client:
        """
        Method to create a client instance.

        Parameters
        ----------
        local : bool
            Whether to create a local client or not.

        Returns
        -------
        Client
            Returns the client instance.
        """
        if local:
            if self._local is None:
                self._local = ClientLocal()
            return self._local

        if self._dhcore is None:
            self._dhcore = ClientDHCore()
        return self._dhcore


def get_client(local: bool = False) -> Client:
    """
    Wrapper around ClientBuilder.build.

    Parameters
    ----------
    local : bool
        Whether to create a local client or not.

    Returns
    -------
    Client
        The client instance.
    """
    return client_builder.build(local)


client_builder = ClientBuilder()
