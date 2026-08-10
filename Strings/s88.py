text=input("Enter a word : ")
upper_count=0
lower_count=0
for letters in text:
    if letters.isupper():
        upper_count+=1
        
    elif letters.islower():
        lower_count+=1
print("Upper case count :",upper_count)        
print("Lower case count : ",lower_count)    