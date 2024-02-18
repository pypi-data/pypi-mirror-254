"""
Module for performing operations on functions.
"""
from __future__ import annotations

import typing

from digitalhub_core.context.builder import check_context, get_context
from digitalhub_core.entities.functions.entity import function_from_dict, function_from_parameters
from digitalhub_core.utils.api import api_ctx_delete, api_ctx_read, api_ctx_update
from digitalhub_core.utils.io_utils import read_yaml

if typing.TYPE_CHECKING:
    from digitalhub_core.entities.functions.entity import Function


def create_function(**kwargs) -> Function:
    """
    Create a new object instance.

    Parameters
    ----------
    **kwargs
        Keyword arguments.

    Returns
    -------
    Function
       Object instance.
    """
    return function_from_parameters(**kwargs)


def create_function_from_dict(obj: dict) -> Function:
    """
    Create a new Function instance from a dictionary.

    Parameters
    ----------
    obj : dict
        Dictionary to create the Function from.

    Returns
    -------
    Function
        Function object.
    """
    check_context(obj.get("project"))
    return function_from_dict(obj)


def new_function(
    project: str,
    name: str,
    kind: str,
    uuid: str | None = None,
    description: str | None = None,
    source: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = True,
    source_code: str | None = None,
    **kwargs,
) -> Function:
    """
    Create a new Function instance and persist it to the backend.

    Parameters
    ----------
    project : str
        Name of the project.
    name : str
        Identifier of the function.
    kind : str
        The type of the function.
    uuid : str
        UUID.
    description : str
        Description of the function.
    source : str
        Remote git source for object.
    labels : list[str]
        List of labels.
    embedded : bool
        Flag to determine if object must be embedded in project.
    source_code : str
        Path to the function's source code on the local file system.
    **kwargs
        Spec keyword arguments.

    Returns
    -------
    Function
       Object instance.
    """
    obj = create_function(
        project=project,
        name=name,
        kind=kind,
        uuid=uuid,
        description=description,
        source=source,
        labels=labels,
        source_code=source_code,
        embedded=embedded,
        **kwargs,
    )
    obj.save()
    return obj


def get_function(project: str, name: str, uuid: str | None = None) -> Function:
    """
    Get object from backend.

    Parameters
    ----------
    project : str
        Name of the project.
    name : str
        The name of the function.
    uuid : str
        UUID.

    Returns
    -------
    Function
        Object instance.
    """
    api = api_ctx_read(project, "functions", name, uuid=uuid)
    obj = get_context(project).read_object(api)
    return create_function_from_dict(obj)


def import_function(file: str) -> Function:
    """
    Get object from file.

    Parameters
    ----------
    file : str
        Path to the file.

    Returns
    -------
    Function
        Object instance.
    """
    obj = read_yaml(file)
    if isinstance(obj, list):
        func_dict = obj[0]
        task_dicts = obj[1:]
    else:
        func_dict = obj
        task_dicts = []
    check_context(func_dict.get("project"))
    func = create_function_from_dict(func_dict)
    func.import_tasks(task_dicts)
    return func


def delete_function(project: str, name: str, uuid: str | None = None) -> dict:
    """
    Delete function from the backend. If the uuid is not specified, delete all versions.

    Parameters
    ----------
    project : str
        Name of the project.
    name : str
        The name of the function.
    uuid : str
        UUID.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_ctx_delete(project, "functions", name, uuid=uuid)
    return get_context(project).delete_object(api)


def update_function(function: Function) -> dict:
    """
    Update a function.

    Parameters
    ----------
    function : Function
        The function to update.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_ctx_update(function.project, "functions", function.name, uuid=function.id)
    return get_context(function.project).update_object(function.to_dict(), api)
