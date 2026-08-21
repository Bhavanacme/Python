string=str(input("Enter a string: "));
count=0;
for i in string:
    if i.isdigit():
        count=count+1;
print(count);
