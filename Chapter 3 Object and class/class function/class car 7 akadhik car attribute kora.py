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
my_car1 = car("Corolla","White")
my_car1.start()
my_car2 = car("Premio","Black")
my_car2.start()
my_car3 = car("Allion", "Blue")
my_car3.start()
