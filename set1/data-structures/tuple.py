# creation of tuple
t = ()
print("type of t : ", type(t))

# tuple() function
l = [1, 3, 5, 7]
print("type of l : ", type(l))
t1 = tuple(l)
print("type of t1 : ", type(t1))

# if we have only one element inside parenthesis () braces it is considered as 'int' data type
t = (2)
print("type for one element inside parenthesis : ", type(t))
t = (2,)
print("type for one element inside parenthesis separated by comma : ", type(t))

# sorted() function
t1 = (1, 3, 5, 7, 2, 6, 12, 85, 12)
print("sorting tuple t1 using sorted() function : ", sorted(t1))

# count() function
t1 = (1, 3, 5, 7, 2, 6, 12, 85, 12)
print("count() function : ", t1.count(12))

# min() and max() functions
print("min() function in tuple : ", min(t1))
print("max() function in tuple : ", max(t1))
