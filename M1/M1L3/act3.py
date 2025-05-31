#input a word

text = str(input("Enter a word or sentence :  "))

#revese the string
#using step value as [::1]

revtext = text[::-1]
text = revtext

print("Reverse of string is : ")
print(text)