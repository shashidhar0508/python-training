# creating empty string
s='python programming'
print("type of s : ",type(s))

# defining multi line strings
s1='''python is 
    high level
    programming language'''
print("multi line string : ",s1)

# indexing in strings
# Python supports both left and right indexing
# left indexing starts with 0
# right indexing starts with -1
s='python programming'
print("right index s[4] : ", s[4])
print("left index s[-4] : ", s[-4])


# slice operator
s='python programming'
print("s[0:7] : ",s[0:7])
print("s[-1:7] : ",s[-7:-1])
print("s[0:11:2]] : ",s[0:11:2])


# string comparisons
s1="python programming"
s2="java programming"
s3="java programming"
s4="aava programming"
# compares string characters based on their ASCII codes
print("s1>s2 : ",s1>s2)
print("s1==s2 : ",s3==s2)
print("s4<s3 : ",s4<s3)


# finding substring
# find(),rfind()
s1="python programming"
print("finding o in s1 : ",s1.find('o'))    #finds first occurrence from left side of string
print("finding o in s1 : ",s1.rfind('o'))    #finds first occurrence from right side of string
print("finding z in s1 : ",s1.find('z'))    #returns -1 if substring is not found
print("finding y in s1 : ",s1.find('y',0,7))    #finds substring in specified range


# index(),rindex()
s1="python programming"
print("finding o in s1 : ",s1.index('o'))    #finds first occurrence from left side of string
print("finding o in s1 : ",s1.rindex('o'))    #finds first occurrence from right side of string
# print("finding z in s1 : ",s1.index('z'))    #returns valueError if substring is not found

# count() in strings
s1="python programming"
print("finding count of 'o' in s1 : ",s1.count('o'))    #finds first occurrence from left side of string

# replace() in strings
s1="python programming"
print("replacing 'o' with 'm' in s1 : ",s1.replace('o','m'))

# split() in strings
# default separator is space and return type of split is list
s='python is a high level programming language'
l=s.split()
print("return type of split : ",type(l))
print("string split result : ",s.split())

# joining of strings
s='-'.join(l)
print("list l converted to string with - joining : ",s)