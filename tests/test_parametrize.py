import pytest # type: ignore

@pytest.mark.parametrize("test_input", [82, 78, 45, 66])
def test_params01(test_input):
    assert test_input > 50

@pytest.mark.parametrize("inp, out", [(2, 4), (3, 27), (4, 256)])
def test_params02(inp, out):
    assert inp ** inp == out