# Amstrong number

print("\nHello !! welcome to my project , it is called an amstrong calculator .")
print("A number that is equal to the sum of its own digits each raised to the power of the number of digits")
num = int(input("Enter your number to be amstronged : "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp // 3

if num == sum :
    print("\nThe number ",num," is an amstrong number . ")
else :
    print("\nThe number ",num," is an not amstrong number . ")
