class Bonus:
    def employee(self,name,sal,bonus):
        self.name=name
        self.sal=sal
        self.bonus=bonus
        
        print(self.name,self.sal,self.sal+self.bonus)
    def employee2(self,name,sal):
        self.name=name
        self.sal=sal
        
        print(self.name,self.sal)
b1=Bonus()
print("With bonus")
b1.employee("Varsha",25000,5000)
b1.employee("Harika",30000,5000)
b1.employee("Bhavya",45000,5000)
print("Without bonus")
b1.employee2("Varsha",25000)
b1.employee2("Harika",30000)
b1.employee2("Bhavya",45000)

