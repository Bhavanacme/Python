students = {
    "Bhavana": 85,
    "Ravi": 72,
    "Sita": 95,
    "Rahul": 68,
    "Anu": 80
}

topper_name = ""
topper_marks = 0

lowest_name = ""
lowest_marks = 101

for name, marks in students.items():

    if marks > topper_marks:
        topper_marks = marks
        topper_name = name

    if marks < lowest_marks:
        lowest_marks = marks
        lowest_name = name

print("Topper:", topper_name)
print("Topper marks:", topper_marks)

print("Lowest scorer:", lowest_name)
print("Lowest marks:", lowest_marks)