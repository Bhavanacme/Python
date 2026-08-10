class Manager:
    def calculate_salary(self):
        print("Manager salary")
class Developer(Manager):
    def calculate_salary(self):
        print("Developer salary")
class Employee(Developer):
    def calculate_salary(self):
        print("Salary")
e=Employee()
e.calculate_salary()                      