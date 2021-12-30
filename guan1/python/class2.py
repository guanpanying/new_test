'''继承
'''


class Animal:
    def __init__(self, name):
        self._name = name

    def run(self):
        print('animal run')

    def sleep(self):
        print('animal sleep')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class Dog(Animal):
    def bark(self):
        print('dog bark')

    def run(self):
        print('dog run')


d = Dog('gou')
d.name = 'xiaohei'
print(d.name)
