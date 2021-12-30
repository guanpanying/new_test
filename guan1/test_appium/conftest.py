import pytest


@pytest.fixture(autouse=True)
def login():
    print('conftest login')
