class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')

    # instead of giving 'self' we can give 'object-reference-name' because it is the first parameter which is passed
    def greeting(smith):
        print('Hello')


# create a new object of Person class
harry = Person()
smith=Person()

# Output: <function Person.greet>
print("Person.greet : ",Person.greet)
print("Person.greeting : ",Person.greeting)

# Output: <bound method Person.greet of <__main__.Person object>>
print("harry.greet : ",harry.greet)

# Calling object's greet() method
# Output: Hello
harry.greet()