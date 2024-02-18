"""
Runtime factory module.
"""
from __future__ import annotations

import importlib
import typing

if typing.TYPE_CHECKING:
    from digitalhub_core.runtimes.base import Runtime
    from digitalhub_core.runtimes.registry import RuntimeRegistry


def build_runtime(kind: str) -> Runtime:
    """
    Runtime factory.

    Returns a runtime instance for the given kind. It looks for the
    runtime registry, imports the specific runtime module, and finally
    get the class from the module by its name.

    Parameters
    ----------
    kind : str
        The runtime kind.

    Returns
    -------
    Runtime
        Runtime instance.
    """
    try:
        registry = import_registry(kind)
        module = importlib.import_module(registry.module)
        return getattr(module, registry.class_name)()
    except (ModuleNotFoundError, ImportError):
        raise ValueError(f"Runtime {kind} not found")


def import_registry(kind: str) -> RuntimeRegistry:
    """
    Import registry from implemented module.

    Parameters
    ----------
    kind : str
        Module kind. Basically, the kind of the function due to correspondence
        function-runtime name.

    Returns
    -------
    dict
        Registry.
    """

    # Cycle over digitalhub layers modules (data, ml, ai).
    for layer in ["data", "ml", "ai"]:
        # Try to import module
        module_name = f"digitalhub_{layer}_{kind}"
        try:
            # Check if module is already imported in cache, otherwise import it
            if module_name not in _modules_cache:
                _modules_cache[module_name] = importlib.import_module(module_name)

            module = _modules_cache[module_name]
            # If module is imported succesfully, break, otherwise continue
            break

        except ModuleNotFoundError:
            continue
    # If module is not imported, raise error
    else:
        raise ModuleNotFoundError(f"Module not found in digitalhub layers data, ml, ai for runtime {kind}")

    # Get registry with classes string pointers
    try:
        return getattr(module, "registry")
    except AttributeError:
        raise ValueError(f"Registry not found in module {module_name}")


_modules_cache = {}
