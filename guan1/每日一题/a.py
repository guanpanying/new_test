class AA:
    _aa = 2

    def abc(self):
        print(self._aa, 'aa')

    def bc(self):
        self._aa = 555


class BB(AA):
    def a2(self):
        print(self.bc())
        print('BB')


b = BB()
b.a2()
