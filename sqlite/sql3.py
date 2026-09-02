import sqlite3

a=sqlite3.connect("college.db")

b=a.cursor()

P=a.execute("SELECT * FROM STUDENTS1")
for i in P:
    print(i[1]);
a.commit()
a.close()    