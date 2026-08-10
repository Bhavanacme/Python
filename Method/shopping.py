class Shopping:
    def total(self,product1,product2,product3):
        self.product1=product1
        self.product2=product2
        self.product3=product3
        print("Total cost : ",self.product1+self.product2+self.product3)
sum=Shopping()

sum.total(200,50,350)    
sum.total(200,450,450)    
sum.total(2000,50,350)        