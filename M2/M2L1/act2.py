# Electricity bill checker

unit = int(input("Enter your unit of electricity : "))

if (unit < 50):
    amount = unit * 2.60
    charge = 25

elif (unit >= 100):
    amount = 130 + (unit - 50 (* 3.25))
    charge = 35

elif (unit >= 100):
    amount = 130 + 162.50 + (unit - 100 (* 5.25))
    charge = 45

else:
    amount = 130 + 162.50 + 526 + (unit - 200 (* 8.45))
    charge = 45

total = amount + charge
print("\n electricity bill = %.2f " %total)
