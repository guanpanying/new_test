# class TestAa:
#     @classmethod
#     def setup_class(cls):
#         print(1)
#     def test_1(self):
#         print(222)
#     def teardown_class(self):
#         print(333)

import pytest


#
# @pytest.fixture()
# def login():
#     print('login方法')
#     return ('tom',123)
#
# @pytest.fixture()
# def operate():
#     print('登录后的操作')
#
# def test_case(login,operate):
#     print(login)
#     print('test_case')
#
# def test_case1():
#     print('test_case1')
#
# def test_case2(login):
#     print('test_case2')


###2
@pytest.fixture(scope='module')
def open():
    print('open')
    yield
    print('执行teardown')
    print('close')


@pytest.mark.usefixtures('open')
def test_search1():
    print('test_search1')
    raise NameError
    pass


def test_search2(open):
    print('test_search2')


def test_search3():
    print('test_search3')
