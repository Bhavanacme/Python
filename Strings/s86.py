text=str(input("Enter a word : "))
count=0
for letter in text:
    if letter.isdigit():
        count+=1
print("Digits is : ",count)    