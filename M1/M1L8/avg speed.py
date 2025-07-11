s1 = int(input("Enter your cyclist 1 speed : "))
s2 = int(input("Enter your cyclist 2 speed : "))

avg = (s1 + s2)/2

if (s1 > avg):
    print("Cyclist 2 is slower than cyclist 1 with the avg difference of ",s1 - avg)

if (s2 > avg):
    print("Cyclist 1 is slower than cyclist 2 with the avg difference of ",s2 - avg)
