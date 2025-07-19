# checkin the age beetween 10 and 20 

print("\nHello ! today let me check your eligibillity to join a class .\n")
name = str(input("Enter your name : "))
print("")
age = int(input("Enter your age : "))
print("")
print("Hello ,", name ,"so you are", age,".")

if (10 <= age <= 20):
    print("You are ",age," so you are eligibillble to join this class . ")
elif (age > 20):
    print("You are ",age," so you crossed the age to join this class . ")
else:
    res = 10 - age
    print("You are ",age," so you have to wait for ",res," years to join this class . \n")
