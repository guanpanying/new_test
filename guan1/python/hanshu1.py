class Student:
    __name = 1
    _name1 = 2
    name2 = 3

    def show(self):
        print(self.name2)
        print('show')

    def _show1(self):
        print('_show1')

    def __show2(self):
        print('__show2')


s = Student()
print(s._name1)
print(s.name2)
print(s._Student__name)
s.show()
s._show()
s.__show()
