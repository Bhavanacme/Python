class Student:
    def details(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
        print(self.name,self.age,self.course)
s=Student()
s.details("Bhavana",17,"CSE")        
s.details("Sai",18,"ECE")
s.details("Varsha",16,"EEE")