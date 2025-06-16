import pytest # type: ignore
from utils.util import get_data

@pytest.mark.parametrize("id, name, course, city", get_data())
def tet_checkdata_from_file(id, name, course, city):
    print(city)