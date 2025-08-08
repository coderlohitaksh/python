# Character occurence

str = (input("Enter your own word : "))
char = (input("Enter your own character : "))

i = 0
count = 0

while (i < len(str)):
    if(str[i] == char):
        count = count + 1
    i = i + 1

print("The total number of times ",char ,"has occured is ",count)

