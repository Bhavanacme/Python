sentence = input("Enter a sentence: ")

words = sentence.split()

result = ""

for word in words:
    result += word[::-1] + " "

print("After reversing each word:", result)