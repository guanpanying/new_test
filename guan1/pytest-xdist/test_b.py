import pytest
import requests


@pytest.mark.parametrize('a', range(2))
def test_one(a):
    print('bbb')
    r = requests.get('https://www.baidu.com', verify=False)
    assert 1 != 2
