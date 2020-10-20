# global variables
x = "global_variable"
def foo():
    print("x inside:", x)
foo()
print("x outside:", x)


# local variables
def foo():
    y = "local"

foo()
print(y)