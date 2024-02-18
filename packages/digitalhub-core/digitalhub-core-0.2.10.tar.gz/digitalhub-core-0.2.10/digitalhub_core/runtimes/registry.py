from __future__ import annotations


class RuntimeRegistry:
    """
    Registry for runtimes to organize the import of classes.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        self.module = None
        self.class_name = None

    def register(self, module: str, class_name: str) -> None:
        """
        Register a runtime class.

        Parameters
        ----------
        module : str
            Module name.
        class_name : str
            Class name.

        Returns
        -------
        None
        """
        self.module = module
        self.class_name = class_name
