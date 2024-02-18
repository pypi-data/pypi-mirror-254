"""
Artifact operations module.
"""
from __future__ import annotations

import typing

from digitalhub_core.context.builder import check_context, get_context
from digitalhub_core.entities.artifacts.entity import artifact_from_dict, artifact_from_parameters
from digitalhub_core.utils.api import api_ctx_delete, api_ctx_read, api_ctx_update
from digitalhub_core.utils.generic_utils import parse_entity_key
from digitalhub_core.utils.io_utils import read_yaml

if typing.TYPE_CHECKING:
    from digitalhub_core.entities.artifacts.entity import Artifact


def create_artifact(**kwargs) -> Artifact:
    """
    Create a new artifact with the provided parameters.

    Parameters
    ----------
    **kwargs
        Keyword arguments.

    Returns
    -------
    Artifact
        Object instance.
    """
    return artifact_from_parameters(**kwargs)


def create_artifact_from_dict(obj: dict) -> Artifact:
    """
    Create a new Artifact instance from a dictionary.

    Parameters
    ----------
    obj : dict
        Dictionary to create the Artifact from.

    Returns
    -------
    Artifact
        Artifact object.
    """
    check_context(obj.get("project"))
    return artifact_from_dict(obj)


def new_artifact(
    project: str,
    name: str,
    kind: str,
    uuid: str | None = None,
    description: str | None = None,
    source: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = True,
    key: str | None = None,
    src_path: str | None = None,
    target_path: str | None = None,
    **kwargs,
) -> Artifact:
    """
    Create an instance of the Artifact class with the provided parameters.

    Parameters
    ----------
    project : str
        Name of the project.
    name : str
        Identifier of the artifact.
    kind : str
        The type of the artifact.
    uuid : str
        UUID.
    description : str
        Description of the artifact.
    source : str
        Remote git source for object.
    labels : list[str]
        List of labels.
    embedded : bool
        Flag to determine if object must be embedded in project.
    key : str
        Representation of "artifacts"act like store://etc..
    src_path : str
        Path to the artifact on local file system.
    targeth_path : str
        Destination path of the artifact.
    **kwargs
        Spec keyword arguments.

    Returns
    -------
    Artifact
       Object instance.
    """
    obj = create_artifact(
        project=project,
        name=name,
        kind=kind,
        uuid=uuid,
        description=description,
        source=source,
        labels=labels,
        embedded=embedded,
        key=key,
        src_path=src_path,
        target_path=target_path,
        **kwargs,
    )
    obj.save()
    return obj


def get_artifact(project: str, name: str, uuid: str | None = None) -> Artifact:
    """
    Retrieves artifact details from the backend.

    Parameters
    ----------
    project : str
        Name of the project.
    name : str
        The name of the artifact.
    uuid : str
        UUID.

    Returns
    -------
    Artifact
        Object instance.
    """
    api = api_ctx_read(project, "artifacts", name, uuid=uuid)
    obj = get_context(project).read_object(api)
    return create_artifact_from_dict(obj)


def get_artifact_from_key(key: str) -> Artifact:
    """
    Get artifact from key.

    Parameters
    ----------
    key : str
        Key of the artifact.
        It's format is store://<project>/artifacts/<kind>/<name>:<uuid>.
    """
    project, name, uuid = parse_entity_key(key)
    return get_artifact(project, name, uuid)


def import_artifact(file: str) -> Artifact:
    """
    Import an Artifact object from a file using the specified file path.

    Parameters
    ----------
    file : str
        Path to the file.

    Returns
    -------
    Artifact
        Object instance.
    """
    obj: dict = read_yaml(file)
    check_context(obj.get("project"))
    return create_artifact_from_dict(obj)


def delete_artifact(project: str, name: str, uuid: str | None = None) -> dict:
    """
    Delete artifact from the backend. If the uuid is not specified, delete all versions.

    Parameters
    ----------
    project : str
        Name of the project.
    name : str
        The name of the artifact.
    uuid : str
        UUID.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_ctx_delete(project, "artifacts", name, uuid=uuid)
    return get_context(project).delete_object(api)


def update_artifact(artifact: Artifact) -> dict:
    """
    Update a artifact.

    Parameters
    ----------
    artifact : Artifact
        The artifact to update.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_ctx_update(artifact.project, "artifacts", artifact.name, uuid=artifact.id)
    return get_context(artifact.project).update_object(artifact.to_dict(), api)
