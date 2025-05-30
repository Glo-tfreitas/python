import pytest # type: ignore
import sys
#Skips the full module
pytestmark = pytest.mark.skipif(sys.platform != 'win32', reason = "Will only work on macOS")

const = 9/5
def cent_to_fah(cent = 0):
    fah = (cent * const) + 32
    return fah

#skip without condition
@pytest.mark.skip(reason="Skipping for no reason specified")
def test_case01():
    assert type(const) == float

#skip if a condition is met
#@pytest.mark.skipif(sys.version_info > (3,8), reason="Doesn't work on py version above 3.8")
@pytest.mark.skipif(cent_to_fah()==32, reason="default value test, so skipping")
def test_case02():
    assert cent_to_fah() == 32

#skip if the pytest version is lower than 5.5.0.
@pytest.mark.skipif(pytest.__version__ < '5.5.0', reason="Pytest version is lower than 5.5.0")
def test_case03():
    assert cent_to_fah(38) == 100.4