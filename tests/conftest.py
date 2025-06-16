import pytest # type: ignore

QA_config = 'qa.prop'
prod_config = 'prod.prop'

def pytest_addoption(parser):
    parser.addoption("--cmdopt", default="QA")

@pytest.fixture()
def CmdOpt(pytestconfig):
    print("\n In CmdOpt fixture function")
    opt = pytestconfig.getoption("cmdopt")
    if opt == "PROD":
        f = open(prod_config, 'r')
    else: 
        f = open(QA_config, 'r')
    yield f


def pytest_configure():
    pytest.weekdays1 = ['mon', 'tue', 'wed']
    pytest.weekdays2 = ['fri', 'sat', 'sun']
    pytest.filename = "file1.txt"

# Setup and teardown of a fixture
@pytest.fixture()
def setup01():
    wk1 = pytest.weekdays1.copy()
    wk1.append('thur')
    yield wk1
    print(f"\nAfter yield in setup01 fixture. wk1: {wk1}]")
    #wk1.clear() --> teardown
    wk1.pop()
    print(f"\nAfter yield in setup01 fixture. After a pop() wk1: {wk1}]")

# Setup of a fixture, yield is like a return but the function doesn't end after calling it
@pytest.fixture()
def setup02():
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0, 'thur')
    yield wk2

# More realistic case of a fixture (preparing an environment and after using it tearing it down)
@pytest.fixture()
def setup03():
    f = open(pytest.filename, 'w')
    f.write("Pytest is good")
    f.close()
    f = f.open(pytest.filename, "fw")
    yield f
    os.remove(pytest.filename)

@pytest.fixture()
def setup04(request):
    mon = getattr()
    print("\n In fixture setup04")
    print("\n Fixture scope: " + str(request.scope))
    print("\n Calling function : " + str(request.function.__name__))
    print("\n Calling module : " + str(request.module.__name__))