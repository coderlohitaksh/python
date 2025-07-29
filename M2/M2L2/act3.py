#reversing orders

str = input("Enter a string to reverse: ")
rstr = str[::-1]
print("🔀 Reversed string:", rstr)

# Reverse a Number
num = input("Enter a number to reverse: ")
# Check if it's a valid number (optional)
if num.isdigit():
    reversed_number = num[::-1]
    print("🔀 Reversed number is ", reversed_number)
else:
    print("❌ Invalid input! ❌( You cannot enter that !)❌")
