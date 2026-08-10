class Dog:
    def sound(self):
        print("Bow-Bow")
class cat(Dog):
    def sound(self):
        print("Meow-Meow")
class cow(cat):
    def sound(self):
        print("Ambha")
class Animals(cow):
    def sound(self):
        print("Sounds")
a=Animals()
a.sound()               
d=Dog()
d.sound()                 