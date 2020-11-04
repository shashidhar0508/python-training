import csv
import pandas as pd

# for reading from csv file
with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# for writing into csv file
with open('protagonist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])

# reading csv files as dictionary
with open("people.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))

# creating a data frame using csv
df = pd.DataFrame([['Jack', 24], ['Rose', 22]], columns=['Name', 'Age'])
df.to_csv('person1.csv')  # writing data frame to a CSV file
