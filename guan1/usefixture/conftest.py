import pytest


@pytest.fixture(scope='session')
def open():
    print('fixture,打开浏览器')

    yield 'aaa'

    print('fixture,关闭浏览器')
