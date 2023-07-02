class Student:
    '''this student doc string'''
    a = 10

    def __init__(self, age, name) -> None:
        self.b = 10

class Parent:
    a = 'Sivakumar'
    def __init__(self, student) -> None:
        self.student = student

    def info(self):
        print(self.student.a, self.student.b)
        print(Parent.a)

s = Student(27, name='Shiv')
p = Parent(s)

p.info()
