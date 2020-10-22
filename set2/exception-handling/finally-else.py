f = open("test.txt", 'r')
try:
  data = f.read()
  print(data)
except IOError as e:
  print(e)
except:
  print("File operations Failed")
finally:
  print("Finally!")
  f.close()
print("All Done")