class Area:
    def areas(self,l,b):
        self.l=l
        self.b=b
        print("**AREA**") 
        print("Square :",self.l*self.l)
        print("Rectangle :",self.l*self.b)
        print("Circle:",3.14*self.l*self.l)
a=Area()
a.areas(10,20)        
