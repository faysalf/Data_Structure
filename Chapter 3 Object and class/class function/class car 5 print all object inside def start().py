class car:
    name = ""
    color = ""
    def __init__(self,n,c):
        self.name = n
        self.color = c
    def start(self):
        print("name:",self.name)
        print("color:",self.color)
        print("Starting the engine")
my_car = car("Corolla","White")
my_car.start()
