import pytest # type: ignore
import os

weekdays1 = ['mon', 'tue', 'wed']
weekdays2 = ['fri', 'sat', 'sun']
filename = "file1.txt"

# Setup and teardown of a fixture
@pytest.fixture()
def setup01():
    wk1 = weekdays1.copy()
    wk1.append('thur')
    yield wk1
    print(f"\nAfter yield in setup01 fixture. wk1: {wk1}]")
    #wk1.clear() --> teardown
    wk1.pop()
    print(f"\nAfter yield in setup01 fixture. After a pop() wk1: {wk1}]")

# Setup of a fixture, yield is like a return but the function doesn't end after calling it
@pytest.fixture()
def setup02():
    wk2 = weekdays2.copy()
    wk2.insert(0, 'thur')
    yield wk2

# More realistic case of a fixture (preparing an environment and after using it tearing it down)
@pytest.fixture()
def setup03():
    f = open(filename, 'w')
    f.write("Pytest is good")
    f.close()
    f = f.open(filename, "fw")
    yield f
    os.remove(filename)

def test_extendList(setup01):
    setup01.extend(weekdays2)
    assert setup01 == ['mon', 'tue', 'wed', 'thu' ,'fri' ,'sat', 'sun']

def test_list(setup01):
    assert setup01 == ['mon', 'tue', 'wed', 'thu']

def test_len(setup01, setup02):
    assert len(weekdays1 + setup02) == len(setup01 + weekdays2)

def test_filetest(setup03):
    assert (setup03.readLine() == "Pytest is good")