# Sum of natural numbers

print("\nHello !! Welcome to my project .\n Firstly, enter a number in the prompt .")
n = int(input(" Enter your value of terms : "))

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1

print("\nThe sum is : ",sum,".")
