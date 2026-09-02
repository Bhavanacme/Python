import sqlite3

v=sqlite3.connect("college.db")

c=v.cursor()
s=c.execute("SELECT * FROM STUDENTS1 WHERE COURSE = CSE")
for i in s:
    print(i);
v.close()