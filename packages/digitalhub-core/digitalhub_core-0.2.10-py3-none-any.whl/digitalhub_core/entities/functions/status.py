"""
FunctionStatus class module.
"""
from __future__ import annotations

from digitalhub_core.entities._base.status import Status


class FunctionStatus(Status):
    """
    Status class for function entities.
    """

    def __init__(self, state: str, message: str | None = None, tasks: list[dict] | None = None) -> None:
        """
        Constructor.

        Parameters
        ----------
        tasks : list[dict]
            List of tasks associated to function.
        """
        super().__init__(state, message)
        self.tasks = {}
        self._set_tasks(tasks)

    def _set_tasks(self, tasks: list[dict] | None) -> None:
        """
        Set tasks.

        Parameters
        ----------
        tasks : list[dict]
            List of tasks associated to function.

        Returns
        -------
        None
        """
        if tasks is None:
            return
        try:
            self.tasks = {t["kind"]: t for t in tasks}
        except KeyError:
            raise ValueError("Malformed tasks.")
