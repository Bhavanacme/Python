class Bank:
    def deposit(self,rupees,name):
        self.rupees=rupees
        self.name=name
        print(self.rupees,self.name)
        print("Deposited Successfully")
b1=Bank()
b1.deposit(2000,"Two thousand rupees only")
b1.deposit(10000,"Ten thousand rupees only")        
b1.deposit(4500,"Four thousand five hundred rupees only")