"""
Base Runtime module.
"""
from __future__ import annotations

import typing
from abc import abstractmethod
from typing import Any, Callable

from digitalhub_core.utils.exceptions import EntityError
from digitalhub_core.utils.logger import LOGGER

if typing.TYPE_CHECKING:
    from digitalhub_core.runtimes.results import RunResults


class Runtime:
    """
    Base Runtime class.
    """

    ##################################
    # Abstract methods
    ##################################

    allowed_actions = []

    @abstractmethod
    def build(self, function: dict, task: dict, run: dict) -> dict:
        """
        Build run spec.
        """

    @abstractmethod
    def run(self, run: dict) -> dict:
        """
        Execute run task.
        """

    @staticmethod
    @abstractmethod
    def _get_function(action: str) -> Callable:
        """
        Get function from action.
        """

    @staticmethod
    @abstractmethod
    def results(run_status: dict) -> RunResults:
        """
        Get run results.
        """

    ##################################
    # Private methods
    ##################################

    def _validate_task(self, run: dict) -> str:
        """
        Validate task.

        Parameters
        ----------
        run : dict
            Run object dictionary.

        Returns
        -------
        str
            Action to execute.
        """
        action = self._get_action(run)
        if action not in self.allowed_actions:
            msg = f"Task {action} not allowed for {self.__class__.__name__} runtime."
            LOGGER.error(msg)
            raise EntityError(msg)
        return action

    @staticmethod
    def _get_action(run: dict) -> str:
        """
        Get action to execute from run.

        The run object stores in its spec the identifier of the task
        it is associated with. The task string is derived from the
        function string, and has the following format:

        <function-kind>+<task-action>://<function-name>:<function-id>

        Parameters
        ----------
        run : dict
            Run object dictionary.

        Returns
        -------
        str
            Action to execute.

        Raises
        ------
        RuntimeError
            If malformed run spec.

        Examples
        --------
        >>> run = {"spec": {"task": dbt+transform://dbt-example-function:some-uuid4}}
        >>> Runtime._get_action(run)
        'transform'
        """
        try:
            return run["spec"]["task"].split(":")[0].split("+")[1]
        except (KeyError, IndexError):
            msg = "Malformed run spec."
            LOGGER.exception(msg)
            raise RuntimeError(msg)

    @staticmethod
    def _execute(func: Callable, *args, **kwargs) -> Any:
        """
        Execute function.

        Parameters
        ----------
        func : Callable
            Function to execute.
        *args
            Function arguments.
        **kwargs
            Function keyword arguments.

        Returns
        -------
        Any
            Function result.
        """
        try:
            return func(*args, **kwargs)
        except Exception:
            msg = "Something got wrong during function execution."
            LOGGER.exception(msg)
            raise RuntimeError(msg)
