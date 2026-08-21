li=[["Bhavana",50,45,48],["Sai",45,46,47],["Janu",50,50,49]];

for x in li:
    name=x[0];
    marks=x[1:];

    total=sum(marks);
    average=total/3;

    print("Name : ",name);
    print("Total : ",total);
    print("Average : ",average);
    print();
    
    