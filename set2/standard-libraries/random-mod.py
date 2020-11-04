import random as r

print("Generates a random float number between 0.0 to 1.0 : ", r.random())

print("random integer between the specified integers : ", r.randint(1, 100))

print("Returns a randomly selected element from the range created by the start, stop and step arguments : ",
      r.randrange(0, 101, 10))

print("Returns a randomly selected element from a non-empty sequence. : ", r.choice([12, 23, 45, 67, 65, 43]))

numbers = [12, 23, 45, 67, 65, 43]
r.shuffle(numbers)
print("This functions randomly reorders the elements in a list : ", numbers)
