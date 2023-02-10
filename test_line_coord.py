import pytest


def test_find_line():
    from line_coord import find_line
    input = [3, 4, 5, 6, 7]
    answer = find_line(input)
    expected = 8
    assert answer == expected
