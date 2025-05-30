import pytest # type: ignore
pytestmark = [pytest.mark.mathOperations]

n1 = 5
n2 = 2

def test_addition():
    assert n1 + n2 == 7

def test_substraction():
    assert n1 - n2 == 3

def test_multiplication():
    assert n1 * n2 == 10

def test_division():
    assert n1 / n2 == 2.5