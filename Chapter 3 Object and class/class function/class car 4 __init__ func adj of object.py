class car:
    name = ""
    color = ""
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def start(self):
        print("Starting the engine")
my_car = car("Corolla","white")
print(my_car.name)
print(my_car.color)
my_car.start()

'''
class car:
    name = ""
    color = ""
    def __init__(self,n,c):
        self.name = n
        self.color = c
    def start(self):
        print("Starting the engine")
my_car = car("Corolla","white")
print(my_car.name)
print(my_car.color)
my_car.start()
'''
