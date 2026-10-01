numbers = [10, 20, 10, 30, 10, 40]

search = 10
count = 0

for i in numbers:
    if i == search:
        count += 1

print("Occurrences:", count)