"""
Module for performing operations on runs.
"""
from __future__ import annotations

import typing

from digitalhub_core.context.builder import check_context, get_context
from digitalhub_core.entities.runs.entity import run_from_dict, run_from_parameters
from digitalhub_core.utils.api import api_base_delete, api_base_read, api_base_update
from digitalhub_core.utils.io_utils import read_yaml

if typing.TYPE_CHECKING:
    from digitalhub_core.entities.runs.entity import Run


def create_run(**kwargs) -> Run:
    """
    Create a new object instance.

    Parameters
    ----------
    **kwargs
        Keyword arguments.

    Returns
    -------
    Run
       Object instance.
    """
    return run_from_parameters(**kwargs)


def create_run_from_dict(obj: dict) -> Run:
    """
    Create a new Run instance from a dictionary.

    Parameters
    ----------
    obj : dict
        Dictionary to create the Run from.

    Returns
    -------
    Run
        Run object.
    """
    return run_from_dict(obj)


def new_run(
    project: str,
    task: str,
    task_id: str,
    kind: str,
    uuid: str | None = None,
    source: str | None = None,
    labels: list[str] | None = None,
    inputs: dict | None = None,
    outputs: list | None = None,
    parameters: dict | None = None,
    local_execution: bool = False,
    **kwargs,
) -> Run:
    """
    Create run.

    Parameters
    ----------
    project : str
        Name of the project.
    task_id : str
        Identifier of the task associated with the run.
    task : str
        Name of the task associated with the run.
    kind : str
        The type of the run.
    uuid : str
        UUID.
    source : str
        Remote git source for object.
    labels : list[str]
        List of labels.
    inputs : dict
        Inputs of the run.
    outputs : list
        Outputs of the run.
    parameters : dict
        Parameters of the run.
    local_execution : bool
        Flag to determine if object has local execution.
    embedded : bool
        Flag to determine if object must be embedded in project.
    **kwargs
        Spec keyword arguments.

    Returns
    -------
    Run
        Run object.
    """
    obj = create_run(
        project=project,
        task=task,
        task_id=task_id,
        kind=kind,
        uuid=uuid,
        source=source,
        labels=labels,
        inputs=inputs,
        outputs=outputs,
        parameters=parameters,
        local_execution=local_execution,
        **kwargs,
    )
    obj.save()
    return obj


def get_run(project: str, name: str) -> Run:
    """
    Get object from backend.

    Parameters
    ----------
    project : str
        Name of the project.
    name : str
        The name of the run.

    Returns
    -------
    Run
        Object instance.
    """
    api = api_base_read("runs", name)
    obj = get_context(project).read_object(api)
    return create_run_from_dict(obj)


def import_run(file: str) -> Run:
    """
    Get object from file.

    Parameters
    ----------
    file : str
        Path to the file.

    Returns
    -------
    Run
        Object instance.
    """
    obj: dict = read_yaml(file)
    check_context(obj.get("project"))
    return create_run_from_dict(obj)


def delete_run(project: str, name: str) -> dict:
    """
    Delete run from the backend.

    Parameters
    ----------
    project : str
        Name of the project.
    name : str
        The name of the run.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_base_delete("runs", name)
    return get_context(project).delete_object(api)


def update_run(run: Run) -> dict:
    """
    Update run.

    Parameters
    ----------
    run : Run
        The run object to update.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_base_update("runs", run.id)
    return get_context(run.project).update_object(run.to_dict(include_all_non_private=True), api)
