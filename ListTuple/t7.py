t1=(1,2,4,5,3,8,6);
largest=0;
smallest=10;
for x in t1 :
    if largest < x :
        largest=x;
print("Largest : ",largest);
for x in t1 :
    if smallest > x :
        smallest=x;
print("Smallest : ",smallest);
        
                    