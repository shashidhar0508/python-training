# Class Method Implementation in python
class Student:
    name = 'Student'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def info(cls):
        return cls.name


print(Student.info())