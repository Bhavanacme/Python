t1=[1,2,6,5,3,98,]
print(type(t1))
t1.sort()
print(t1)
print("Largest second : ",t1[-2])
lar=0
sec=0
for x in t1:
    if x>lar:
        sec=lar
        lar=x
    elif x>sec:
        sec=x
print(sec)      
even=0      
odd=0
for x in t1:
        if x%2==0:
            even=even+1
        else:
            odd=odd+1    
print(even)
print(odd)   
t2=("Bhavana","Sai","Rohith","Gayatri","Pavani","Teju","Dimple","Sai")
for x in t2:
    print(x)
marks=(45,78,90,23,52,60)    
for x in marks:
    if x>50:
        print(x)
for x in t1:
    if x%2==0:
        print("Even : ",x)
for x in t1:
    if x%2!=0:
        print("Odd: ",x)        

t3=(("Name:","Bhavana"),("Marks:",848),("Course:","Cse"))
for x in t3:
    print(x[0],x[1])
