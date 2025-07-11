print("Welcome to the Number Swapper!\n")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

print("\nBefore swapping:")
print("First number:", num1)
print("Second number:", num2)
print("Third number:", num3)

temp = num1 
num1 = num2
num2 = num3
num3 = temp

print("\nAfter swapping:")
print("First number:", num1)
print("Second number:", num2)
print("Third number:", num3)
