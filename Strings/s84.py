text=str(input("Enter a word : "))
vowels="aeiou"
count=0
for letter in text:
    if letter in vowels :
        count+=1
print("Vowels count : ",count)         