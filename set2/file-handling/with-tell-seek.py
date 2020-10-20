with open("abc.txt","w") as f:
    print("first before reading : ",f.tell())
    list = ["Python\n", "Java\n", "Angular\n", "React"]
    f.writelines(list)
    print("first after reading : ",f.tell())
    f.seek(21)
    f.write("   vue")
    f.seek(0)
