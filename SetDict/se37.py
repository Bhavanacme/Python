students = {
    "Bhavana": 85,
    "Ravi": 75,
    "Sita": 92,
    "Rahul": 80
}

highest_name = ""
highest_marks = 0

for name, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_name = name

print("Student with highest marks:", highest_name)
print("Marks:", highest_marks)