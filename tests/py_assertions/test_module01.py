import pytest # type: ignore

def test_a1():
    print("This is my first test")
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1

@pytest.mark.mathOperations
def test_a2():
    assert 4 != 3

def test_a3():
    assert 1

def test_a4():
    assert "abc" == "abc"

def test_a5():
    assert ((3-1)*4/2) == 4.0

def test_a6():
    assert 1 in divmod(9,5)
    assert "py" in "this is pytest" 
    # assert "put" in "this is pytest" will give us an error  
    assert 2 in [1, 2, 4] 
    # assert [1, 2] in [1, 2, 4] will give us an error