class Sparrow:
    def fly(self):
        print("Sparrow is flying")
class Eagle(Sparrow):
    def fly(self):
        print("Eagle is flying")
class Penguin(Eagle):
    def fly(self):
        print("Penguin is flying")
class Birds(Penguin):
    def fly(self):
        print("Birds are flying")
b=Birds()
b.fly()                                