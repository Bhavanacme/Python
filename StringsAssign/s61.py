sentence = input("Enter a sentence: ")

words = sentence.split()

result = []

for word in words:
    if word not in result:
        result.append(word)

print("Sentence without duplicate words:", ' '.join(result))