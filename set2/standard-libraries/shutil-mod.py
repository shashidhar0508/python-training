import shutil

f = open('abc.txt', 'r')
f1 = open('abc1', 'w')

# for copying from one file to another file using file objects
shutil.copyfileobj(f, f1)

# for copying from one file to another file using paths
shutil.copy("abc.txt", "data1.txt")

# for copying from one file to another file using paths
# Here we need to provide file name if we change folder
shutil.copyfile("abc.txt", "data1.txt")

# for copying from one file to another file using paths along with meta data
# meta data means same file creation time and others
shutil.copy2("abc.txt", "data2.txt")

# for moving files form one folder to another folder
shutil.move("data2.txt", "D:/pycharm workspaces/python-training/set2/file-handling")

# for moving complete folder along with inner files to another folder
shutil.copytree("set2/standard-libraries/data2.txt", "set1/file-handling")

f.close()
f1.close()
