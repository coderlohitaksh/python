num = int(input("Enter your number : "))
flag = False

for i in range (2 , num):
    if (num % i == 0):
        flag = True
        break

if flag : 
    print(num ,"is not a prime number .")
else :
    print(num ,"is a prime number .")