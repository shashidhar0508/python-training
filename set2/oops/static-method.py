# Static Method Implementation in python
class Student:
    name = 'Student'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def info():
        return "This is a student class"


print(Student.info())