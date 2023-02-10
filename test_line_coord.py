import pytest


def test_find_line():
    from line_coord import find_line
    answer = find_line(3, 4, 5, 6, 7)
    expected = 8
    assert answer == expected
