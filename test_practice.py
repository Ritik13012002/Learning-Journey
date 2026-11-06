import pytest


def add(a, b):
    return a + b


@pytest.mark.parametrize("a,b,expected", [(5, 3, 8), (2, 4, 6), (2, 3, 7)])
def test_add(a, b, expected):
    assert add(a, b) == expected


def is_empty(text):
    return len(text) == 0


@pytest.mark.parametrize("text, expected", [("", True), ("hello", False)])
def test_is_empty(text, expected):
    assert is_empty(text) == expected
