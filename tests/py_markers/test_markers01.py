import pytest # type: ignore

letters = 'abcdefghijklmnopqrstuvwxyz'

@pytest.mark.sanity
def test_str01():
    num = 9/4
    s1 = 'I like ' + 'pytest automation'
    assert str(num) ==  '2.25'
    assert s1 == 'I like pytest automation'
    assert s1 + str(num) == 'I like pytest automation2.25'

def test_str02():
    assert len(letters) == 26

def test_str03():
    assert letters[0] == 'a'
    assert letters[-1] == 'z' == letters[25]

@pytest.mark.str
def test_strslice():
    assert letters[:] == letters
    assert letters[10:] =='klmnopqrstuvwxyz'
    assert letters[-3:] == 'xyz'
    assert letters[:21:5] == 'afkpu'

@pytest.mark.sanity
@pytest.mark.str
def test_strsplit():
    s1 = 'Python,Pytest and Automation'
    assert s1.split() == ['Python,Pytest', 'and', 'Automation']
    assert s1.split(',') == ['Python', 'Pytest and Automation']

@pytest.mark.str
def test_strjoin():
    pass
    s1 = 'Python,Pytest and Automation'
    l1 = ['Python,Pytest' 'and', 'Automation']
    l2 = ['Python', 'Pytest and Automation']