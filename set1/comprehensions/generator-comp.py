def num_generator(n):
    num =1
    while True:
        yield num
        if num == n:
            return
        else:
            num += 1
for i in num_generator(2000):
    i=i*i
    print (i)