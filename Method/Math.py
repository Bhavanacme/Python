class Math:
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)
    def sub(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1-self.num2)
    def mul(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1*self.num2)
    def div(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1/self.num2)    
m1=Math()
m1.mul(10,20)
m1.add(10,20)
m1.sub(10,20)
m1.div(10,20)       