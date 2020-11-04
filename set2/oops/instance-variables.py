class Test:

    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        self.c = 30


t = Test()
t.m1()
t.d = 40
print("a, b, c, d : ", t.a, t.b, t.c, t.d)
print(t.__dict__)
