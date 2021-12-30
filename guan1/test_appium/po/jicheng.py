class A:
    # base
    def __init__(self, aa=None):
        print('aaaa', aa)


class B(A):
    # app
    def start(self):
        print('b(a)')


class C(A):
    # main
    def bbb(self):
        print('bbbb')


c = C()


class D(C):
    # test
    def test_a(self):
        d = C()
        d.bbb()
