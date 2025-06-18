# Checking if the number is greater or not.
# Check if the number is greater than 15 or not.


comp = float(input("Enter your limit : "))
n = float(input("Enter your number to be compared : "))


if (n > comp):
    print("The number" ,n,"is greater than" ,comp)
elif n < comp:
    print("The number" ,n,"is less than" ,comp)
else:
    print("The number" ,n,"is equal to" , comp)
