"""
Project metadata module.
"""
from __future__ import annotations

from digitalhub_core.entities._base.metadata import Metadata


class ProjectMetadata(Metadata):
    """
    A class representing Project metadata.
    """

    def __init__(
        self,
        name: str | None = None,
        source: str | None = None,
        labels: list[str] | None = None,
        created: str | None = None,
        updated: str | None = None,
        description: str | None = None,
        embedded: bool = True,
        **kwargs,
    ) -> None:
        """
        Constructor.

        Parameters
        ----------
        description : str
            Description of the entity.

        See Also
        --------
        Metadata.__init__
        """
        super().__init__(name, source, labels, embedded, created, updated)
        self.description = description
