class Boy:
    species = "boy"
    def __init__(self , name , age):
        self.name = name
        self.age = age

L = Boy("Lohitaksh" , 8)
T = Boy("Takshwik" , 2)

print(f"{L} is a {L.species}.")
print(f"{T} is a {T.species}.")
print(f"{L} is {L.age} old.")
print(f"{T} is {T.age} old.")
