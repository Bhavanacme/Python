class Graduatedstudent:
    def display(self,name,marks,idno):
        self.name=name
        self.marks=marks
        self.idno=idno
        print("Student is Graduated")
class Student(Graduatedstudent):
    def display(self,name,marks,idno):
        self.name=name
        self.marks=marks
        self.idno=idno
        print("Student is not Graduated")
s=Student()        
s.display("Bhavana",848,256)
