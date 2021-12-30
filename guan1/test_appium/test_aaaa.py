import pytest


class Testfixture:
    @pytest.mark.parametrize('a,b', [(1, 1), (2, 2), (3, 3)], ids=['关', 'testcase2', 'testcase3'])
    def test_para(self, login, a, b):
        print(a, b)

    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')
