a = str(input("Enter your word : "))
al = input("Enter the alphabet you want to search for : ")
for i in a:
    if (i == al):
        print(al ,"is found .")
        break
    else:
        print(al ,"is not found .")
