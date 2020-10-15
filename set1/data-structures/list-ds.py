#creating empty list
l=[]
print("type of l : ",type(l))

#list() fucntion
m=range(5,20)
print("type of m before converting to list : ",type(m))
a=list(m)
print("list a values : ",a)
print("After converting to list : ",type(a))

#accessing elements of list using index
print("3rd element of a is : ",a[2])

#Nested lists
b=[1,5,[6,8,4],2]
print("Nested lists b[2][1] : ",b[2][1])

#slice operator in list
print("slice operation for a[3:7] : ",a[3:7])

#len() and count() function in list
l=[4,3,3,7,7,7,7,2,9,9]
print("length of list l is : ",len(l))
print("count of 7 in list l is : ",l.count(7))


#list manipulation
#append(),insert(),remove(),pop(),extend(),clear() funtions in list
list2=[]
list2.append(3)
list2.append(7)
list2.append(11)
list2.append(4)
list2.append(19)
print("adding elements in list2 using append() function : ",list2)

list2.insert(2,13)
print("inserting elements in specified location in list2 using insert() fucntion : ",list2)

list2.remove(4)
print("removing element 4 in list2 using remove() fucntion : ",list2)

    #list2.pop() returns last element from list2 and returns removed element
print("pop() function returning last element after removing it: ",list2.pop())
print("After pop() function : ",list2)
    #we can also remove specifed element in list using index by pop() function
print("removing 2nd index value in list2 : ",list2.pop(2))
print("After removing 2nd index value in list2 using pop() function : ",list2)

list3=[2,8,6,24,14]
list2.extend(list3)
print("adding another list3 to list2 using extend() fucntion : ",list2)

list2.clear()
print("removing all elements in list2 using clear() fucntion : ",list2)


#Ordering elements in list
#sort(),reverse()
list4=[11,3,19,21,1,7,5]
list4.sort()
print("sorted list4 elements using sort() function : ",list4)
list4.reverse()
print("reversed list4 elements using reverse() function : ",list4)
list4.reverse()
