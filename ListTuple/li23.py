li=[1,6,2,3,4,8,9,5,10,7];
print(li);
even=[];
odd=[];
for x in li : 
    if x%2==0:
        even.append(x);
print(even);
for x in li :
    if x%2!=0 :
        odd.append(x);
print(odd);                