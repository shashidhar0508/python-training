#creating of empty dictionary
d={}
print("Type of d : ",type(d))
l=dict()
print("Type of l : ",type(l))

#retrieving dictionary values using keys
d={1:'python',2:'java',3:'c',4:'c++'}
print("retrieving value of key 2 d[2] : ",d[2])

#dictionary manipulation
#adding entries
d1={}
d1[1]="python"
d1[2]="java"
d1[3]="c"
d1[4]='c++'
print("entries in dictionary d after insertion of entries : ",d1)
#updating entries
d1[3]="java script"
print("dictionary d1 after updating : ",d1)
#deleting entries
del d1[4]
print("dictionary d1 after deleting : ",d1)
#for removing all entries in dictionary
d1.clear()
print("after removing all entries in dictionary using clear() function: ",d1)
