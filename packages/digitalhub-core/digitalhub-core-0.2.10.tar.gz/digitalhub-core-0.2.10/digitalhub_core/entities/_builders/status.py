"""
Status factory module.
"""
from __future__ import annotations

import typing

from digitalhub_core.entities._base.status import State

if typing.TYPE_CHECKING:
    from digitalhub_core.entities._base.status import Status


def build_status(status_cls: Status, **kwargs) -> Status:
    """
    Build entity status object.

    Parameters
    ----------
    status_cls: Status
        Status object.
    **kwargs
        Keyword arguments.

    Returns
    -------
    Status
        An entity status object.
    """
    kwargs = parse_arguments(**kwargs)
    return status_cls(**kwargs)


def parse_arguments(**kwargs) -> dict:
    """
    Parse keyword arguments and add default values.

    Parameters
    ----------
    **kwargs
        Keyword arguments.

    Returns
    -------
    dict
        Keyword arguments with default values.
    """
    state = kwargs.get("state")
    if state is None:
        kwargs["state"] = State.CREATED.value
    else:
        if kwargs["state"] not in State.__members__:
            raise ValueError(f"Invalid state: {state}")
    return kwargs
