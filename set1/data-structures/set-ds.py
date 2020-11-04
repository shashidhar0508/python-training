# creation of set
s = set()
d = {}  # By default {} is dictionary
print("type of d: ", type(d))
print("type of s: ", type(s))

# set() function
l = [10, 20, 30, 40]
print("type of l : ", type(l))
s1 = set(l)
print("type of s1 : ", type(s1))

# functions in set
# add(),update(),pop(),remove(),discard(),clear()
s2 = set()
print("type of s2 : ", type(s2))
s2.add(11)
s2.add(13)
s2.add(17)
s2.add(19)
s2.add(23)
print("set s2 after add() function : ", s2)

s2.update(l, range(4))
print("set s2 after update() function : ", s2)

# pop() function returns deleted element
print("after using pop() function : ", s2.pop())

s2.remove(19)
print("set s2 after removing 19 element using remove() function : ", s2)

s2.discard(23)
print("set s2 after discarding 23 element using discard() function : ", s2)
# remove() functions returns keyError if value not present in set,
# discord() function doesn't return any error if value is not present in list

s2.clear()
print("set s2 after using clear() function : ", s2)

# Mathematical operations in set
# union(),intersection(),difference(),symmetric difference()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# a.union(b), a|b returns all elements in both sets
print("all elements in both sets using union() function : ", a | b)

# a.intersection(b), a&b returns common elements in both sets
print("common elements in both sets using intersection() function : ", a & b)

# a.difference(b), a-b returns elements present in a but not in b
print("returning elements in a and not in b using difference() function : ", a - b)

# a.symmetric_difference(b), a^b returns remaining elements other than common elements in both sets
print("elements after using symmetric_difference() function : ", a ^ b)
