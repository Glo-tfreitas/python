from pytest_bdd import scenario, scenarios, given, when, then # type: ignore
from pathlib import Path
import pytest # type: ignore

featureFileDir = 'myfeatures'
featureFile = 'fixtures.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

scenarios(FEATURE_FILE)

@pytest.fixture()
def setup_set():
    print("\n In fixture... setup() function.. \n")
    countries = {'Poland', 'America', 'Brasil'}
    return countries

@given('A datatype set')
def check_set_type(setup_set):
    print("In background checking set type")
    if not isinstance(setup_set, set):
        pytest.xfail("The type is not a set type")

@given('the set is not empty')
def check_set_not_empty(setup_set):
    print("In background checking non-empty set")
    if len(setup_set) == 0:
        pytest.xfail("The set of elems is empty")

@given('A set with 3 elements')
def set_of_elems(setup_set):
    if len(setup_set) == 0:
        pytest.xfail("Te set of elems is empty")
    elif len(setup_set) > 3:
        while len(setup_set > 3):
            setup_set.pop()
    return setup_set

@when('Add 2 elements to the set')
def add_elements(setup_set1):
    setup_set1.add('India')
    setup_set1.add('UK')

@then('The set should have 5 elements')
def final_set_elements(setup_set1):
    print(setup_set1)
    assert len(setup_set1) == 5 