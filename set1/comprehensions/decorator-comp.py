def smart_divide(func):
    def inner(a, b):
        if b == 0: return print("Whoops! cannot divide with Zero")
        return func(a, b)

    return inner


@smart_divide
def divide(a, b): print("Result of a/b is : ", a / b)


divide(2, 0)
divide(4, 2)
