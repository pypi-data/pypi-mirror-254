"""
Models for task specifications.
"""
from __future__ import annotations

from pydantic import BaseModel
from typing_extensions import Literal


class Volume(BaseModel):
    """
    Volume model.
    """

    volume_type: Literal["config_map", "secret", "persistent_volume_claim"]
    """Volume type."""

    name: str
    """Volume name."""

    mount_path: str
    """Volume mount path."""


class NodeSelector(BaseModel):
    """
    NodeSelector model.
    """

    key: str
    """Node selector key."""

    value: str
    """Node selector value."""


class Resource(BaseModel):
    """
    Resource model.
    """

    resource_type: Literal["cpu", "memory", "gpu"]
    """Resource kind (cpu, memory, gpu)."""

    requests: int
    """Resource requests."""

    limits: int
    """Resource limits."""


class Env(BaseModel):
    """
    Env variable model.
    """

    name: str
    """Env variable name."""

    value: str
    """Env variable value."""


class K8sResources(BaseModel):
    """
    K8sResources model.
    """

    node_selector: NodeSelector = {}
    """Node selector."""

    volumes: list[Volume] = []
    """List of volumes."""

    resources: Resource = {}
    """Resources restrictions."""

    env: list[Env] = []
    """Env variables."""
