import inspect
from dis import HAVE_ARGUMENT, opmap
from types import FunctionType

from pyusage.introspections import find_imported_module, lookup_global

GLOBAL_OPS = opmap["LOAD_GLOBAL"], opmap["STORE_GLOBAL"]  # bytecode instructions that use globals
EXTENDED_ARG = opmap["EXTENDED_ARG"]  # extend argument of next instruction


def function_globals(func: FunctionType):
    if not inspect.isfunction(func):
        raise TypeError(f"Expected {FunctionType}")

    glob_names = set()

    names = func.__code__.co_names
    ops = iter(func.__code__.co_code)

    extarg = 0
    for op in ops:
        if op in GLOBAL_OPS:
            arg = next(ops) + extarg
            extarg = 0
            glob_names.add(names[arg])
        elif op == EXTENDED_ARG:
            extarg = extarg * 256 + next(ops)
            continue
        elif op >= HAVE_ARGUMENT:
            next(ops)

    module = find_imported_module(func.__module__)
    globs = {lookup_global(name, module) for name in glob_names}

    return globs
