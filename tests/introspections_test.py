import empty_module
import pytest
import simple_module

from pyusage.introspections import find_imported_module, lookup_global


def test_find_imported_module_not_found():
    with pytest.raises(KeyError):
        find_imported_module('foobar')


def test_find_imported():
    assert find_imported_module('empty_module') == empty_module


def test_lookup_global():
    with pytest.raises(KeyError):
        lookup_global('foo', simple_module)


def test_lookup_existing():
    assert lookup_global('X', simple_module) == simple_module.X


def test_lookup_builtin():
    assert lookup_global('dict', empty_module) == dict
