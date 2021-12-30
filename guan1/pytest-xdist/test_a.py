import pytest
import requests


@pytest.mark.parametrize('a', range(50))
def test_one(a):
    print('a', a)
    r = requests.get('https://www.baidu.com', verify=False)
    assert 1 != 2
