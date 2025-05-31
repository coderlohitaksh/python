name = input ("Enter a name : ")
age = input (" Enter a number :")
is_student = True
weight = 38.5

#printing variables and data type

print("Name : ",name)
print("Data type of name is :", type(name))

print("Age : " , age)
print("Data type of Age is :", type(age))

print("Is student : " , is_student)
print("Data type of Is student is :", type(is_student))

print("Weight : " , weight)
print("Data type of weight is :", type(weight))

#typecasting now happens

print("\n after typecasting")
age = str(age)
print(age)
print("Data type of Age is " , type(age))

weight = int(weight)
print(weight)
print("Data type of weight is :" , type(weight))

