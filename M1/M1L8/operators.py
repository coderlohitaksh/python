#1st

a = 12
b = 19
c = 34
d = 10
res = b ** c + d / b ** a + c
print(res)

#2nd

n1 = int(input("Enter you numerator : "))
n2 = int(input("Enter your demoninator : "))

if (n1 % n2 == 0):
    print("The number",n1 ,"is divisible by the",n2 ,".")
else:
    print("The number ",n1 ,"is not divisble by ",n2 ,".")