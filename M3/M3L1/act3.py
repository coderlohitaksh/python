# calculator

# add
def add (P , Q):
    return P + Q 
# subtract
def subtract (P , Q):
    return P - Q
# multiply
def multiply (P , Q):
    return P * Q
# divide 
def divide (P , Q):
    return P / Q

print("Please select your option 💖.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter your choice (a / b / c / d) : ")

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

if choice == 'a' :
    print(num1 , "+" ,num2 , "=" , num1 + num2)
elif choice == 'b' :
    print(num1 , "-" ,num2 , "=" , num1 - num2)
elif choice == 'c' :
    print(num1 , "*" ,num2 , "=" , num1 * num2)
else:
    print(num1 , "/" ,num2 , "=" , num1 / num2)
