"""
Base Function specification module.
"""
from __future__ import annotations

from digitalhub_core.entities._base.spec import Spec, SpecParams


class FunctionSpec(Spec):
    """
    Specification for a Function.
    """

    def __init__(
        self,
        source: str | None = None,
        **kwargs,
    ) -> None:
        """
        Constructor.

        Parameters
        ----------
        source : str
            Path to the Function's source code on the local file system.
        **kwargs
            Keyword arguments.
        """
        self.source = source

        self._any_setter(**kwargs)


class FunctionParams(SpecParams):
    """
    Function parameters model.
    """

    source: str = None
    """Path to the Function's source code on the local file system."""
