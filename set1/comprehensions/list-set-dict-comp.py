# List Comprehension
list1=[x for x in range(21) if x%2==0]
print("list Comprehension : ",list1)


# Set Comprehension
set1={x for x in range(21) if x%2!=0}
print("Set Comprehension : ",set1)


# dictionary Comprehension
values=[1,2,3,4,5,6,7,8,9,10]
NewDictionary = {x: x**2 for x in values if x**2 % 4 == 0}
print("Dictionary Comprehension : ",NewDictionary)
