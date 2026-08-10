t1=("Bhavana","Sai","Rohith","Gayatri","Pavani","Teju","Dimple","Sai")
print(t1[0])
n=len(t1)
print(t1[n-1])
print(t1[-1])
print(t1[2])
print(t1[0:4])
print(t1[2:6])
print(t1[-3:])
print(t1[1:])
print(t1[ :-1])
print("Tuple reverse")
print(t1[::-1])
print("Alternate")
print(t1[::2])
print("Even index")
s=t1[::2]
print(s)
print("odd index")
print(t1[1::2])
print(t1[2])
print(t1[1] in t1)
print('Rohith' in t1)
t2=("Java","C","HTML","Python")
print(t2[0])
print(t2.index("Python"))
print(t1.count('Sai'))
print('Java' in t2)
print(t1+t2)
print(t1*3)
t3=[1,2,3,4,5]
print(type(t3))
t4=tuple(t3)
print(type(t4))
print(type(t2))
t5=list(t2)
print(type(t5))
t5.append("C++")
print(type(t5))
print(t5)
t6=tuple(t5)
print(type(t6))
print(t6)
t7=list(t3)
print(type(t7))
t7.remove(4)
print(t7)
t8=tuple(t7)
print(type(t8))
t9=list(t8)
print(type(t9))
t9[-1]=6
print(t9)
t10=int(input("Enter the values : "))
list=[]
list.append(t10)
t11=tuple(list)
print(t11)
print(max(t3))
print(min(t3))
sum=0
for x in t3:
    sum+=x
print(sum)    
t14=sum
t13=len(t3)
avg=t14/t13
print(avg)















































