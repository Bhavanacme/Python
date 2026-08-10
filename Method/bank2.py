class Bankaccount:
    def withdraw(self):
        print("Money is withdrawl")
class Savings(Bankaccount):
    def withdraw(self):
        print("Money is withdrawl in main account")
b=Savings()
b.withdraw()                