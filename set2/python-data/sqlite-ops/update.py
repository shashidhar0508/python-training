import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")

print("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
print("cursor : ", cursor)
for rows in cursor:
    print("ID = ", rows[0])
    print("NAME = ", rows[1])
    print("ADDRESS = ", rows[2])
    print("SALARY = ", rows[3], "\n")

conn.commit()
print("Operation done successfully")
conn.close()
