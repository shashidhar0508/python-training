# creating a file and writing into that file
try:
    f = open("D:/test-folder/test-write.txt", 'w')
    f.write("Python is high level programming language")
finally:
    f.close()

# creating a file and writing into that file using write and writeLines
# Here as path(folder name) is not mentioned it creates file in this same directory
try:
    f = open("test.txt", 'w')
    f.write("Python \n")
    f.write("programming\n")
    list = ["Python\n", "Java\n", "Angular\n", "React"]
    f.writelines(list)
finally:
    f.close()

# reading from a file
try:
    f = open("D:/test-folder/test.txt", 'r')
    for line in f:
        print(line, end='')
finally:
    f.close()

# reading from a file using read(), read(n), readline(), readlines() fucntions
f1 = open("test.txt", 'r')
data1 = f1.read()
print("data1 : ", data1)
f1 = open("test.txt", 'r')
data2 = f1.read(10)
print("data2 : ", data2)
f1 = open("test.txt", 'r')
line1 = f1.readline()
print("line1 : ", line1, end='')
f1 = open("test.txt", 'r')
lines = f1.readlines()
for line in lines:
    print("all lines : ", line, end='')
