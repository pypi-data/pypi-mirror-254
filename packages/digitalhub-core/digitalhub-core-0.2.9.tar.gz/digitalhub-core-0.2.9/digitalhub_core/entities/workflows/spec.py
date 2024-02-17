"""
Workflow base specification module.
"""
from __future__ import annotations

from digitalhub_core.entities._base.spec import Spec, SpecParams


class WorkflowSpec(Spec):
    """
    Workflow specifications.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """


class WorkflowParams(SpecParams):
    """
    Workflow parameters.
    """


SPEC_REGISTRY = {
    "workflow": [WorkflowSpec, WorkflowParams],
}
