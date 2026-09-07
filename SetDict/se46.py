dictionary = {
    "apple": "A fruit",
    "computer": "An electronic machine",
    "python": "A programming language",
    "book": "A collection of written pages"
}

word = input("Enter a word: ")

if word in dictionary:
    print("Meaning:", dictionary[word])
else:
    print("Word not found")