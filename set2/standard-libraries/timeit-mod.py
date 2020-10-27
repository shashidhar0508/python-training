import timeit

print("checking time taken to execute following program : ",
      timeit.timeit("""list1=["apple","banana","cherry"] 
list1.remove("banana") 
print(list1)""",number=1))

print("time taken to execute code 5 times : ",
      timeit.timeit("""list1=["apple","banana","cherry"] 
list1.remove("banana") 
print(list1)""",number=10))