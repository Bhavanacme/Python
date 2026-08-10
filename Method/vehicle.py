class car:
    def start(self):
        print("Car start")
class bus(car):
    def start(self):
        print("Bus start")
class bike(bus):
    def start(self):
        print("Bike start")
class vehicle(bike):
    def start(self):
        print("Start")
o=vehicle()
o.start()   
b=bus()
b.start()                             