"""
General utilities module.
"""
from __future__ import annotations

import base64
import os
from datetime import datetime
from uuid import uuid4

from digitalhub_core.utils.io_utils import read_text


def build_uuid(uuid: str | None = None) -> str:
    """
    Create a uuid if not given

    Parameters
    ----------
    uuid : str
        UUID. Optional.

    Returns
    -------
    str
        The uuid.
    """
    if uuid is not None:
        return uuid
    return str(uuid4())


def get_timestamp() -> str:
    """
    Get the current timestamp timezoned.

    Returns
    -------
    str
        The current timestamp.
    """
    return datetime.now().astimezone().isoformat()


def decode_string(string: str) -> str:
    """
    Decode a string from base64.

    Parameters
    ----------
    string : str
        The string to decode.

    Returns
    -------
    str
        The string decoded from base64.
    """
    return base64.b64decode(string).decode()


def encode_string(string: str) -> str:
    """
    Encode a string in base64.

    Parameters
    ----------
    string : str
        The string to encode.

    Returns
    -------
    str
        The string encoded in base64.
    """
    return base64.b64encode(string.encode()).decode()


def encode_source(path: str) -> str:
    """
    Read a file and encode in base64 the content.

    Parameters
    ----------
    path : str
        The file path to read.

    Returns
    -------
    str
        The file content encoded in base64.
    """
    return encode_string(read_text(path))


def set_dhub_env(
    endpoint: str | None = None,
    user: str | None = None,
    password: str | None = None,
    token: str | None = None,
) -> None:
    """
    Function to set environment variables for DHub Core config.

    Parameters
    ----------
    endpoint : str
        The endpoint of DHub Core.
    user : str
        The user of DHub Core.
    password : str
        The password of DHub Core.
    token : str
        The token of DHub Core.

    Returns
    -------
    None
    """
    if endpoint is not None:
        os.environ["DIGITALHUB_CORE_ENDPOINT"] = endpoint
    if user is not None:
        os.environ["DIGITALHUB_CORE_USER"] = user
    if password is not None:
        os.environ["DIGITALHUB_CORE_PASSWORD"] = password
    if token is not None:
        os.environ["DIGITALHUB_CORE_TOKEN"] = token


def parse_entity_key(key: str) -> tuple[str, str, str]:
    """
    Parse the entity key.

    Parameters
    ----------
    key : str
        The entity key.

    Returns
    -------
    tuple[str, str, str]
        The project, the name and the uuid of the entity.
    """
    try:
        # Remove "store://" from the key
        key = key.replace("store://", "")
        # Split the key into parts
        parts = key.split("/")
        project = parts[0]
        # The name and uuid are separated by a colon in the last part
        name, uuid = parts[-1].split(":")
        return project, name, uuid
    except Exception as e:
        raise ValueError("Invalid key format.") from e
