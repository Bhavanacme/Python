string=str(input("Enter a string: "));
vowels="aeiouAEIOU";
count=0;
for i in string:
    if i not in vowels:
       count=count+1;
print(count);       