def sum(*n):
    total=0
    for n1 in n:
        total=total+n1
    print("The Sum=",total)

sum()
sum(10)
sum(10,20)
sum(10,20,30,40)