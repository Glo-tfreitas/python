import pytest # type: ignore


#The test fails intentionally (Known bug for example) [XFAIL]
@pytest.mark.xfail(reason="known issue")
def test_type():
    assert type(1.3) == int

#Normal test [PASS]
def test_type2():
    assert type(1.3) == float

#The test is marked to fail intentionally but passes [XPASS]
@pytest.mark.xfail
def test_type3():
    assert type(1.3) == float