import sqlite3

con=sqlite3.connect("college.db")

curr=con.cursor()
B=curr.execute("SELECT * FROM STUDENTS1 WHERE MARKS>=840")
for i in B:
    print(i);
con.close()    