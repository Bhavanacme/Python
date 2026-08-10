class Temperature:
    def converter(self,c):
        self.c=c
        print("Celsisus to Farenheit : ",(c*9/5)+32)
        print("Cdelsisus to Kelvin : ",c+273.15)
c1=Temperature()
c1.converter(275)
c1.converter(500)      