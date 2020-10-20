import os

cwd=os.getcwd()
print("Current Working Directory:",cwd)

os.mkdir("mysub")
print("mysub directory created in cwd")

os.mkdir("mysub/mysub2")
print("mysub directory created in cwd")

os.rmdir("mysub/mysub2")
print("mysub2 directory deleted")

os.rename("mysub","newdir")
print("mysub directory renamed to newdir")

print(os.listdir("."))