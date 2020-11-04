# creating of empty dictionary
d = {}
print("Type of d : ", type(d))
l = dict()
print("Type of l : ", type(l))

# retrieving dictionary values using keys
d = {1: 'python', 2: 'java', 3: 'c', 4: 'c++'}
print("retrieving value of key 2 d[2] : ", d[2])

# len() function
print("length of d : ", len(d))

# dictionary manipulation
# adding entries
d1 = {}
d1[1] = "python"
d1[2] = "java"
d1[3] = "c"
d1[4] = 'c++'
print("entries in dictionary d after insertion of entries : ", d1)

# updating entries
d1[3] = "java script"
print("dictionary d1 after updating : ", d1)

# deleting entries
del d1[4]
print("dictionary d1 after deleting : ", d1)

# for removing all entries in dictionary
d1.clear()
print("after removing all entries in dictionary using clear() function: ", d1)

# get(key) function
d1 = {1: 'python', 2: 'java', 3: 'java script', 4: 'c++'}
# d.get(key) => if key is present returns value else returns None
print("d.get(key) : ", d1.get(3))
# d.get(key,defaultValue) => if key is present returns value else returns default value
print("d.get(key, defaultValue) : ", d1.get(5, "no language"))

# setdefault(key,defaultValue) function
d1 = {1: 'python', 2: 'java', 3: 'java script', 4: 'c++'}
# if key is already present returns the value corresponding to that key
# if key is not present adds that entry in dictionary
d1.setdefault(4, "swift")
print("d.setdefault(key,value) : ", d1.setdefault(4, "swift"))
d1.setdefault(5, "swift")
print("d.setdefault(key,value) : ", d1)

# pop(key) function
d1 = {1: 'python', 2: 'java', 3: 'java script', 4: 'c++'}
# removes entry(key,value) and returns corresponding value of the key which is passed
print("d.pop() fucntion : ", d1.pop(4))

# popitem() function
# removes last entry(key,value) in dictionary and returns it
print("d.popitem() fucntion : ", d1.popitem())

# keys() function
d1 = {1: 'python', 2: 'java', 3: 'java script', 4: 'c++'}
# returns all the keys present in dictionary
print("all keys of dictionary using keys() function : ", d1.keys())

# values() function
d1 = {1: 'python', 2: 'java', 3: 'java script', 4: 'c++'}
# returns all the values present in dictionary
print("all values of dictionary using values() function : ", d1.values())

# items() function
d1 = {1: 'python', 2: 'java', 3: 'java script', 4: 'c++'}
# returns all the entries present in dictionary
for k, v in d1.items():
    print("key : ", k, "value : ", v)
