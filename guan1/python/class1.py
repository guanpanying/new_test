class SingleInstance:
    num = 'num'
    _num = 0
    __num1 = 1

    def __init__(self):
        print(self._num)
        print(self.__num1)

    def show(self):
        print('show')

    def _show1(self):
        print('_show')

    def __show2(self):
        print('__show')


class Two(SingleInstance):
    print('two', SingleInstance._num)
    SingleInstance.show
    SingleInstance._show1


# print('-'*30)
# print(t1._num)
# print(t1.__num1) #AttributeError: 'SingleInstance' object has no attribute '__num1'
t = Two()
