text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

print("Character frequency:")

for ch in frequency:
    print(ch, ":", frequency[ch])