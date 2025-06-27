print("hello friends!\nToday we are going to check whhich grade you are from A to F .\n")

math = float(input("Enter your marks in maths : "))
eng = float(input("Enter your marks in english : "))
sci = float(input("Enter your marks in sciense : "))
gk = float(input("Enter your marks in G.K. : "))
comp = float(input("Enter your marks in computer : "))

total = (math + eng + sci + gk + comp)
res = (total/5)

if (res >= 95 and res <= 100):
    print("you have the grade of A+")
elif (res >= 85 and res <= 95):
    print("you have the grade of A")
elif (res >= 75 and res <= 85):
    print("you have the grade of B+")
elif (res >= 70 and res <= 75):
    print("you have the grade of B")
elif (res >= 65 and res <= 70):
    print("you have the grade of C+")
elif (res >= 55 and res <= 65):
    print("you have the grade of C")
elif (res >= 50 and res <= 55):
    print("you have the grade of D+")
elif (res >= 45 and res <= 50):
    print("you have the grade of D")
elif (res >= 40 and res <= 45):
    print("you have the grade of E+")
elif (res >= 35 and res <= 40):
    print("you have the grade of E")
else:
    print("You have the grade of F")
