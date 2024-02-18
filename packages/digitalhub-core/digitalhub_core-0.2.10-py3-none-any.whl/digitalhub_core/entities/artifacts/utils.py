"""
Artifact utils module.
"""
from __future__ import annotations

import typing
from hashlib import sha1
from mimetypes import guess_type
from pathlib import Path

if typing.TYPE_CHECKING:
    from digitalhub_core.entities.artifacts.entity import Artifact


def get_artifact_info(artifact: Artifact) -> dict:
    """
    Get the information of an artifact.

    Parameters
    ----------
    artifact : Artifact
        The artifact.

    Returns
    -------
    dict
        The information of the artifact.
    """
    return {
        "id": f"store://{artifact.project}/artifacts/{artifact.kind}/{artifact.name}:{artifact.id}",
        "key": artifact.name,
        "kind": artifact.kind,
    }


def calculate_blob_hash(data_path: str) -> str:
    """
    Calculate the hash of a file.

    Parameters
    ----------
    data_path : str
        Path to the file.

    Returns
    -------
    str
        The hash of the file.
    """
    with open(data_path, "rb") as f:
        data = f.read()
        return f"sha1_{sha1(data).hexdigest()}"


def get_file_size(data_path: str) -> int:
    """
    Get the size of a file.

    Parameters
    ----------
    data_path : str
        Path to the file.

    Returns
    -------
    int
        The size of the file.
    """
    return Path(data_path).stat().st_size


def get_file_mime_type(data_path: str) -> str:
    """
    Get the mime type of a file.

    Parameters
    ----------
    data_path : str
        Path to the file.

    Returns
    -------
    str
        The mime type of the file.
    """
    return guess_type(data_path)[0]


def get_file_extension(data_path: str) -> str:
    """
    Get the extension of a file.

    Parameters
    ----------
    data_path : str
        Path to the file.

    Returns
    -------
    str
        The extension of the file.
    """
    return Path(data_path).suffix[1:]
