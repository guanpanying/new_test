class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"姓名：{self.name},年龄：{self.age}")


#定义子类

class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score = score

stu = Student("guan",30,100)
stu.info()
