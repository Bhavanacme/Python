numbers = {}

for num in range(1, 11):
    numbers[num] = num * num * num

print("Numbers and their cubes:")

for key, value in numbers.items():
    print(key, ":", value)