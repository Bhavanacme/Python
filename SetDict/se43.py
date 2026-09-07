employees = {
    "Ravi": 45000,
    "Sita": 60000,
    "Rahul": 55000,
    "Anu": 40000,
    "Kiran": 75000
}

print("Employees earning more than ₹50,000:")

for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)