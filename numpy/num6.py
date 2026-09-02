import numpy as np
numbers=np.array([1,2,3,4,5,6,7,8,9,10])
print(numbers)
even_numbers=numbers[numbers%2==0]
print("Even numbers:", even_numbers)
odd_numbers=numbers[numbers%2!=0]
print("Odd numbers:", odd_numbers)