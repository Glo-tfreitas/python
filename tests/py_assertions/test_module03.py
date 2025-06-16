# Assertions about expected exceptions
import pytest # type: ignore

def test_case01():
    with pytest.raises(ZeroDivisionError):
        assert 1/0

def test_case02():
    with pytest.raises(Exception) as excinfo:
        assert (1,2,3) == (1,2,4)
    print(excinfo)