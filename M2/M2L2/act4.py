# Ask the user for a number

n = int(input("Enter a number: "))

sum = 0

for i in range(n + 1):
    sum = sum + i  

print("The sum of whole numbers from 0 to", n, "is:", sum)
