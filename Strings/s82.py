text=str(input("Enter a word : ")).lower()
if text==text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")    