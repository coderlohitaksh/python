try :
    num1 = int(input("Enter your first number :"))
    num2 = int(input("Enter your second number :"))
    result = (num1/num2)
    print("result is", result)
except ZeroDivisionError :
    print("Division by zero is not allowed .")
except ValueError:
    print("Please enter numerical value .")
except NameError as ex :
    print("The exception is ",ex)
except :
    print("Some error occured .")
finally :
    print("I will print no matter what happens !")
