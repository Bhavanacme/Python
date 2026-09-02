employee=[("Bhavana","IAS",50000),("Sai","Bussiness",100000),("Janu","Doctor",75000)];
highest=0;
for x in employee:
    name,job,salary=x;
    if highest < salary:
        highest=salary
print("Highest salary : ",highest);
