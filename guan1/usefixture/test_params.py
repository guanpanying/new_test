import pytest


@pytest.fixture(params=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def data(request):
    return request.param


def test_data(data):
    print(f'数据是:{data}')


def test_data1(data):
    print(f'数据是：{data + 1}')
