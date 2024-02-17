"""
Metadata factory module.
"""
from __future__ import annotations

import typing

from digitalhub_core.utils.generic_utils import get_timestamp

if typing.TYPE_CHECKING:
    from digitalhub_core.entities._base.metadata import Metadata


def build_metadata(metadata_cls: Metadata, **kwargs) -> Metadata:
    """
    Build entity metadata object.

    Parameters
    ----------
    metadata_cls: Metadata
        Metadata object.
    **kwargs
        Keyword arguments.

    Returns
    -------
    Metadata
        An entity metadata object.
    """
    kwargs = parse_arguments(**kwargs)
    return metadata_cls(**kwargs)


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
        A dictionary containing the entity metadata attributes.
    """
    if "created" not in kwargs or kwargs["created"] is None:
        kwargs["created"] = get_timestamp()
    if "updated" not in kwargs or kwargs["updated"] is None:
        kwargs["updated"] = kwargs["created"]
    return kwargs
