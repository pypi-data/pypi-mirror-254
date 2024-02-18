"""
Module for performing operations on tasks.
"""
from __future__ import annotations

import typing

from digitalhub_core.context.builder import check_context, get_context
from digitalhub_core.entities.tasks.entity import task_from_dict, task_from_parameters
from digitalhub_core.utils.api import api_base_delete, api_base_read, api_base_update
from digitalhub_core.utils.io_utils import read_yaml

if typing.TYPE_CHECKING:
    from digitalhub_core.entities.tasks.entity import Task


def create_task(**kwargs) -> Task:
    """
    Create a new object instance.

    Parameters
    ----------
    **kwargs
        Keyword arguments.

    Returns
    -------
    Task
       Object instance.
    """
    return task_from_parameters(**kwargs)


def create_task_from_dict(obj: dict) -> Task:
    """
    Create a new object instance.

    Parameters
    ----------
    obj : dict
        Object dictionary.

    Returns
    -------
    Task
       Object instance.
    """
    return task_from_dict(obj)


def new_task(
    project: str,
    kind: str,
    uuid: str | None = None,
    source: str | None = None,
    labels: list[str] | None = None,
    function: str | None = "",
    node_selector: dict | None = None,
    volumes: list[dict] | None = None,
    resources: dict | None = None,
    env: list[dict] | None = None,
    **kwargs,
) -> Task:
    """
    Create a new object instance.

    Parameters
    ----------
    project : str
        Name of the project.
    kind : str
        The type of the task.
    uuid : str
        UUID.
    source : str
        Remote git source for object.
    labels : list[str]
        List of labels.
    function : str
        The function string identifying the function.
    node_selector : dict
        The node selector of the task.
    volumes : list[dict]
        The volumes of the task.
    resources : dict
        Kubernetes resources for the task.
    env : list[dict]
        The env variables of the task.
    **kwargs
        Spec keyword arguments.

    Returns
    -------
    Task
       Object instance.
    """
    obj = create_task(
        project=project,
        kind=kind,
        uuid=uuid,
        source=source,
        labels=labels,
        function=function,
        node_selector=node_selector,
        volumes=volumes,
        resources=resources,
        env=env,
        **kwargs,
    )
    obj.save()
    return obj


def get_task(project: str, name: str) -> Task:
    """
    Get object from backend.

    Parameters
    ----------
    project : str
        Name of the project.
    name : str
        The name of the task.

    Returns
    -------
    Task
        Object instance.
    """
    api = api_base_read("tasks", name)
    obj = get_context(project).read_object(api)
    return create_task_from_dict(obj)


def import_task(file: str) -> Task:
    """
    Get object from file.

    Parameters
    ----------
    file : str
        Path to the file.

    Returns
    -------
    Task
        Object instance.
    """
    obj: dict = read_yaml(file)
    check_context(obj.get("project"))
    return create_task_from_dict(obj)


def delete_task(project: str, name: str, cascade: bool = True) -> dict:
    """
    Delete task from the backend.

    Parameters
    ----------
    project : str
        Name of the project.
    name : str
        The name of the task.
    cascade : bool
        Whether to cascade delete.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_base_delete("tasks", name, cascade=cascade)
    return get_context(project).delete_object(api)


def update_task(task: Task) -> dict:
    """
    Update task.

    Parameters
    ----------
    task : Task
        The task object to update.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_base_update("tasks", task.id)
    return get_context(task.project).update_object(task.to_dict(), api)
