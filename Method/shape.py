class Rectangle:
    def area(self,l,b):
        self.l=l
        self.b=b
        print("Area of Rectangle :",l*b)
class Circle(Rectangle):
    def area(self,l):
        self.l=l
        print("Area of circle : ",3.14*l*l)
class Triangle(Circle):
    def area(self,l,b):
         self.l=l
         self.b=b
         print("Area of Triangle : ",0.5*l*b)
class Shape(Triangle):
    def area(self):c
        print("Shape is not given")
s=Shape()
s.area()                

