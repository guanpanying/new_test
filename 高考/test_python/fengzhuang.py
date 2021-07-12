

class FengZhuang:
    def __init__(self,name):
        self.name = name
        self.__age = 20

    def age(self):
        print(self.__age)

stu1 = FengZhuang("guan")
stu1.age()

print(dir(stu1))
print(stu1._FengZhuang__age)