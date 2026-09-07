students = {
    "Bhavana": 85,
    "Ravi": 75,
    "Sita": 90,
    "Rahul": 80
}

name = input("Enter student name: ")

if name in students:
    print("Student exists")
else:
    print("Student does not exist")