import sqlite3
conn=sqlite3.connect("Mydb.db")
cur=conn.cursor()
cur.execute("DROP TABLE IF EXISTS STUDENTS")
cur.execute('''create table STUDENTS (
                name varchar(10),
                id int(5),
                marks int(5))''')
data=[("Bhavana",101,808),
      ("Sai",102,529),
      ("Varsha",103,843)]
cur.executemany("INSERT INTO STUDENTS VALUES(?,?,?)",data)
conn.commit()
a=cur.execute("SELECT * FROM STUDENTS")
for i in a:
    print(i);
cur.execute("UPDATE STUDENTS SET id=1 WHERE marks=808")
conn.commit()
b=cur.execute("SELECT * FROM STUDENTS")
print("fetchone : ",b.fetchone())
print("fetchmany : ",b.fetchmany(2))
print("fetchall : ",b.fetchall())
conn.close();                         
