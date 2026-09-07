sentence = input("Enter a sentence: ")

words = sentence.split()

result = []

for word in words:
    if len(word) > 5:
        result.append(word)

print("Words with more than 5 characters:", result)