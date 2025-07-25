# Reversing everything 

str = str(input("Enter your string ( sentence or word ) : "))

str2 = ('')

for i in str:
    str2 = i + str2

print("\nThe original string was : ",str)
print("The reversed string was : ",str2)

