import json

from ghostcall.suggest import suggest


def test_suggest_close_match():
    result = suggest("dump", json)
    assert "dumps" in result


def test_no_match_returns_empty():
    result = suggest("zzzzzzzzzzz", json)
    assert result == []


def test_filters_private_attrs():
    class Foo:
        _private = 1
        public = 2

    result = suggest("private", Foo())
    assert "_private" not in result


def test_handles_object_with_no_dir():
    class Weird:
        def __dir__(self):
            raise RuntimeError("nope")

    assert suggest("foo", Weird()) == []
