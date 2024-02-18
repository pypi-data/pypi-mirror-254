"""
Task specification module.
"""
from __future__ import annotations

from digitalhub_core.entities._base.spec import Spec, SpecParams
from digitalhub_core.entities.tasks.models import Env, NodeSelector, Resource, Volume


class TaskSpec(Spec):
    """Task specification."""

    def __init__(
        self,
        function: str,
        node_selector: NodeSelector | None = None,
        volumes: list[Volume] | None = None,
        resources: Resource | None = None,
        env: list[Env] | None = None,
        **kwargs,
    ) -> None:
        """
        Constructor.

        Parameters
        ----------
        function : str
            The function string of the task.
        node_selector : NodeSelector
            The node selector of the task.
        volumes : list[Volume]
            The volumes of the task.
        resources : Resource
            Kubernetes resources for the task.
        env : list[Env]
            The env variables of the task.
        """
        self.function = function
        self.node_selector = node_selector
        self.volumes = volumes
        self.resources = resources
        self.env = env

        self._any_setter(**kwargs)


class TaskParams(SpecParams):
    """
    Base task model.
    """

    function: str
    """Function string."""

    node_selector: NodeSelector = None
    """Node selector."""

    volumes: list[Volume] = None
    """List of volumes."""

    resources: Resource = None
    """Resources restrictions."""

    env: list[Env] = None
    """Env variables."""
