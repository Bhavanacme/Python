students = {
    "Bhavana": 85,
    "Ravi": 72,
    "Sita": 90,
    "Rahul": 68,
    "Anu": 78
}

print("Students who scored above 75:")

for name, marks in students.items():
    if marks > 75:
        print(name, ":", marks)