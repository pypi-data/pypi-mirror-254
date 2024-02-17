"""
Run module.
"""
from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from digitalhub_core.entities.artifacts.entity import Artifact


class RunResults:
    """
    A class representing a run results.
    """

    def __init__(
        self,
        artifacts: list[Artifact] | None = None,
    ) -> None:
        """
        Constructor.

        Parameters
        ----------
        artifacts : list[Artifact]
            The artifacts.
        """
        self.artifacts = artifacts
