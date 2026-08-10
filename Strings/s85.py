text=str(input("Enter a word : "))
vowels="aeiou"
count=0
for letter in text:
    if letter.isalpha() and letter not in vowels :
        count+=1
print("Consonanats count: ",count)         