numbers = [10, 45, 23, 67, 12]

smallest = numbers[0]
second_smallest = numbers[0]

for i in numbers:
    if i < smallest:
        second_smallest = smallest
        smallest = i
    elif i < second_smallest and i != smallest:
        second_smallest = i

print("Second smallest:", second_smallest)