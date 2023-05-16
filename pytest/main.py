import pytest

@pytest.fixture
def add(a, b):
    return a+b

def test_false():
    assert add(1, 2) == 5


def test_true():
    assert add(1, 2) == 3