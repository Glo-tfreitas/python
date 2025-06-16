#Object oriented form of tests
class TestMyStuff():
    def test_type(self):
        assert type(1.3) == float

    def test_strs(self):
        assert str.upper("python") == "PYTHON"
        assert "pytest".capitalize() == "Pytest"

class TestFailsIntentionally():
    def test_type(self):
        assert type(1.3) == int

    def test_strs(self):
        assert str.upper("python") == "Python"
        assert "pytest".capitalize() == "pytest"