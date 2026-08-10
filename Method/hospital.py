class Hospital:
    def display(self):
        print("Hospital")
class SpclHospital(Hospital):
    def display(self):
        print("Specialized hospital")
class Hsptl(SpclHospital):
    def display(self):
        print("Hospital is called")
h=Hsptl()
h.display()                        