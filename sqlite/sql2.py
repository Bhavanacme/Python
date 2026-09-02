import sqlite3
conn=sqlite3.connect("college.db")
cur=conn.cursor()
cur.execute("DROP TABLE IF EXISTS STUDENTS1")
cur.execute('''CREATE TABLE STUDENTS1(
               ID INT(5),
               NAME VARCHAR(10),
               AGE INT(5),
               COURSE VARCHAR(10),
               MARKS INT(10))''')
data=[(101,"Bhavana",17,"CSE",808),
      (102,"Sai",18,"ECE",529),
      (103,"Varsha",17,"EEE",843),
      (104,"Jyothi",18,"Civil",879),
      (105,"Divya",18,"CSE",856)]
cur.executemany("INSERT INTO STUDENTS1 VALUES(?,?,?,?,?)",data)
conn.commit()
a=cur.execute("SELECT * FROM STUDENTS1")
for i in a:
    print(i);
conn.commit()
conn.close();                         