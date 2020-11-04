# reduce() function
from functools import *

list1 = [10, 20, 30, 40, 50]
result = reduce(lambda x, y: x + y, list1)
print("adding all the elements in the list to single result using reduce() function : ", result)
