import sys
from types import ModuleType
from typing import Any


def find_imported_module(name: str) -> ModuleType:
    return sys.modules[name]


def lookup_global(name: str, module: ModuleType) -> Any:
    try:
        return getattr(module, name)
    except AttributeError:
        return module.__builtins__[name]
