class Creditpay:
    def pay(self):
        print("Payment is completed in creditcard")
class Upipay(Creditpay):
    def pay(self):
        print("Payment is completed in UPI")
class Cashpay(Upipay):
    def pay(self):
        print("Payment is completed with cash")
class payment(Cashpay):
    def pay(self):
        print("Payment is completed")
p=payment()
p.pay()                                