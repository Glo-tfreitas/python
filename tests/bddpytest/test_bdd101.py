from pytest_bdd import scenario, scenarios, given, when, then # type: ignore
from pathlib import Path
import pytest # type: ignore

featureFileDir = 'myfeatures'
featureFile = 'first101.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

def pytest_configure(): # GLOBAL VARIABLE
    pytest.AMT = 0

# scenarios(FEATURE_FILE)

# First scenario

@scenario('Withdrawal of money')
def test_withdrawal():
    print("End of withdrawal test")
    pass

@given('the account balance is 100')
def current_balance():
    pytest.AMT = 100

@when('the account holder withdraws 30')
def withdraw_amount():
    pytest.AMT -= 30

@then('the account balance should be 70')
def final_balance():
    assert pytest.AMT == 70

# Second scenario

@scenario('Removal of items from set')
def test_removal_of_items():
    pass

@given('a set of three fruits', target_fixture="myset")
def create_set():
    myset = {'Apple', 'Pear', 'Orange'}
    return myset

@when('we remove a fruit from the set')
def remove_fruit(myset):
    myset.pop()
    print(myset)

@then('the set will have two fruits')
def final_set(myset):
    assert len(myset) == 2