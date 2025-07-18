# exam eligibility

mr = str(input("Did you have any medical reports Y or N : "))
atend = int(input("Enter the number of days you were present : "))

if (mr == 'Y'):
    print(" You are allowed for the exam .")
else:
    if (atend >= 75):
        print("You are allowed for the exam .")
    else:
        print("You are not allowed for the exam .")

