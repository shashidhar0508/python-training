import re

# match()
m = re.match("abc", "abcabdefg")
if m != None:
    print("Match is available at the beginning of the String")
    print("Start Index:", m.start(), "and End Index:", m.end())
else:
    print("not available")

# fullmatch()
fm = re.fullmatch('abcabdefg', "abcabdefg")
print("Full string matched" if fm != None else "String not matched")

# search()
sm = re.search("aaa", "abaaaba")
print("search is available " if sm != None else "search not matched")

# findall()
fa = re.findall("[0-9]", "a7b9c5kz")
print("findall : ", fa)

# sub()
s = re.sub("[a-z]", "#", "a7b9c5k8z")
print(s)

# subn()
t = re.subn("[a-z]", "#", "a7b9c5k8z")
print(t)
print("The Result String:", t[0])
print("The number of replacements:", t[1])

# spllit()
l = re.split(",", "java,python,angular,react,django")
for t in l:
    print(t)
