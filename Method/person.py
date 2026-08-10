class Person:
    def details(self):
        print("Bhavana is a student")
class Teacher(Person):
    def details(self):
        print("Harika is a Teacher")
p=Teacher()
p.details()