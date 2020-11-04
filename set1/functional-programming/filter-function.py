# filter() function
list1 = [0, 5, 10, 15, 20, 25, 30]
list2 = list(filter(lambda x: x % 2 == 0, list1))
print("Getting values in list1 which are even numbers by using filter() function : ", list2)
