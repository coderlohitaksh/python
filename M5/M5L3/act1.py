from colorama import Fore

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus('School Volvo', 220, 16)

print()
print(Fore.LIGHTYELLOW_EX + "My school bus name:", School_bus.name, ", it's maxspeed is", School_bus.max_speed, "and it's mileage is", School_bus.mileage)
print()