import pytest
from pyusage.bytecode import function_globals


def test_function_globals_arg_not_a_function():
    with pytest.raises(TypeError):
        function_globals(None)


def test_function_globals_identity_function():
    assert function_globals(lambda x: x) == set()


def test_function_globals_use_one_global():
    assert function_globals(lambda: map) == {map}


def test_function_globals_use_repeated_globals():
    assert function_globals(lambda x: list(set(list(x)))) == {set, list}
