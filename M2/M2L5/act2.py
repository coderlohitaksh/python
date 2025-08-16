#Floyd's triangle
#Floyd's triangle is a right - angle triangle

rows = int(input("Enter the number the total number of rows : "))
number = 1
print("Presenting : Floyd's Triangle ")

for i in range (1 , rows + 1):
    for j in range (1 , i + 1):
        print(number , end = "")
        number - number + 1
    print()

