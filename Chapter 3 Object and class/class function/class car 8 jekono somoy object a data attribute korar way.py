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
my_car.year = 2020  #kono akti data rakhte korte vule gel jekono somoy object a data attribut kora jabe

print("name:",my_car.name)
print("Color:",my_car.color)
print("year:",my_car.year)
