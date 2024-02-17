"""
Project base specification module.
"""
from __future__ import annotations

from digitalhub_core.entities._base.spec import Spec, SpecParams


class ProjectSpec(Spec):
    """
    Project specification.
    """

    def __init__(
        self,
        context: str | None = None,
        functions: list | None = None,
        artifacts: list | None = None,
        workflows: list | None = None,
        dataitems: list | None = None,
    ) -> None:
        """
        Initializes a new instance of the ProjectSpec class.

        Parameters
        ----------
        context : str
            The project's context.
        functions : list
            List of project's functions.
        artifacts : list
            List of project's artifacts.
        workflows : list
            List of project's workflows.
        dataitems : list
            List of project's dataitems.

        Returns
        -------
        None
        """
        self.context = context
        self.functions = functions if functions is not None else []
        self.artifacts = artifacts if artifacts is not None else []
        self.workflows = workflows if workflows is not None else []
        self.dataitems = dataitems if dataitems is not None else []


class ProjectParams(SpecParams):
    """
    Parameters model for project.
    """

    context: str = None
    """The project's context."""

    functions: list = None
    """List of project's functions."""

    artifacts: list = None
    """List of project's artifacts."""

    workflows: list = None
    """List of project's workflows."""

    dataitems: list = None
    """List of project's dataitems."""


SPEC_REGISTRY = {
    "project": [ProjectSpec, ProjectParams],
}
