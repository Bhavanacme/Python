class display:
    def fun(self,one,two,three):
        self.one=one
        self.two=two
        self.three=three
        print(self.one,self.two,self.three)
d=display()
d.fun(1,2,3)
d.fun(2,3,1)
d.fun(3,1,2)        
