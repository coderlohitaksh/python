# BMI Calculator

# Get user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display the result
print("Your BMI is: ")

# Interpret the result
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
