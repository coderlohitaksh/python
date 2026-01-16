class Vehicle:
    def __init__(self , max_speed , mileage , model) :
        self.max_speed = max_speed
        self.mileage = mileage
        self.model = model

modelX = Vehicle(240 , 18 , "i20 Hyundai")
print("Max speed of i20 is",modelX.max_speed)
print("Mileage of i20 is",modelX.mileage)
print("The model is",modelX.model)
