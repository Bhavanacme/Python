employees = {
    "Ravi": 25000,
    "Sita": 30000,
    "Rahul": 35000,
    "Anu": 40000
}

total = 0

for salary in employees.values():
    total += salary

average = total / len(employees)

print("Average salary:", average)