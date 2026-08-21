string=str(input("Enter a string: "));
vowels="aeiouAEIOU";
for i in string:
    if i in vowels:
        count=string.count(i);
print(count);
        
