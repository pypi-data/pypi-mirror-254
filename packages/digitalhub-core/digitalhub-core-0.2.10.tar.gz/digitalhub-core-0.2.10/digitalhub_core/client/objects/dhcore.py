"""
DHCore Client module.
"""
from __future__ import annotations

import os

import requests
from digitalhub_core.client.objects.base import Client
from digitalhub_core.utils.exceptions import BackendError


class ClientDHCore(Client):
    """
    DHCore client.

    The DHCore client is used to communicate with the Digitalhub Core backendAPI via REST.
    At creation, the client trys to get the endpoint and authentication parameters
    from the environment variables. In case the endpoint is not set, it raises an exception.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        super().__init__()
        self._endpoint = self._get_endpoint()
        self._auth = self._get_auth()

    def create_object(self, obj: dict, api: str) -> dict:
        """
        Create an object.

        Parameters
        ----------
        obj : dict
            The object to create.
        api : str
            The api to create the object with.

        Returns
        -------
        dict
            The created object.
        """
        return self._call("POST", api, json=obj)

    def read_object(self, api: str) -> dict:
        """
        Get an object.

        Parameters
        ----------
        api : str
            The api to get the object with.

        Returns
        -------
        dict
            The object.
        """
        return self._call("GET", api)

    def update_object(self, obj: dict, api: str) -> dict:
        """
        Update an object.

        Parameters
        ----------
        obj : dict
            The object to update.
        api : str
            The api to update the object with.

        Returns
        -------
        dict
            The updated object.
        """
        return self._call("PUT", api, json=obj)

    def delete_object(self, api: str) -> dict:
        """
        Delete an object.

        Parameters
        ----------
        api : str
            The api to delete the object with.

        Returns
        -------
        dict
            A generic dictionary.
        """
        resp = self._call("DELETE", api)
        if isinstance(resp, bool):
            resp = {"deleted": resp}
        return resp

    def _call(self, call_type: str, api: str, **kwargs) -> dict:
        """
        Make a call to the DHCore API.
        Keyword arguments are passed to the session.request function.

        Parameters
        ----------
        call_type : str
            The type of call to make.
        api : str
            The api to call.
        **kwargs
            Keyword arguments.

        Returns
        -------
        dict
            The response object.
        """
        url = self._endpoint + api
        kwargs["auth"] = self._auth
        response = None
        try:
            response = requests.request(call_type, url, timeout=60, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if isinstance(e, requests.exceptions.Timeout):
                msg = "Request to DHCore backend timed out."
            elif isinstance(e, requests.exceptions.ConnectionError):
                msg = "Unable to connect to DHCore backend."
            else:
                msg = f"Backend error: {e}"
            raise BackendError(msg) from e

    @staticmethod
    def _get_endpoint() -> str:
        """
        Get DHub Core endpoint environment variables.

        Returns
        -------
        str
            DHub Core endpoint environment variables.

        Raises
        ------
        Exception
            If the endpoint of DHCore is not set in the env variables.
        """
        endpoint = os.getenv("DIGITALHUB_CORE_ENDPOINT")
        if endpoint is None:
            raise BackendError("Endpoint not set as environment variables.")
        if endpoint.endswith("/"):
            endpoint = endpoint[:-1]
        return endpoint

    @staticmethod
    def _get_auth() -> tuple[str, str] | None:
        """
        Get authentication parameters from the config.

        Returns
        -------
        tuple[str, str]
            The authentication parameters.
        """
        user = os.getenv("DIGITALHUB_CORE_USER")
        password = os.getenv("DIGITALHUB_CORE_PASSWORD")
        if user is None or password is None:
            return None
        return user, password

    @staticmethod
    def is_local() -> bool:
        """
        Declare if Client is local.

        Returns
        -------
        bool
            False
        """
        return False
