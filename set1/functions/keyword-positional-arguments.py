# positional arguments
def children(child3, child2, child1):
    print("The youngest child is " + child3)


children(child1="Emil", child2="Tobias", child3="Linus")


# keyword arguments
def fn1(a, b, c):
    print("calculation of a+b*c is : ", a + b * c)


fn1(10, 20, 30)
fn1(30, 20, 10)
