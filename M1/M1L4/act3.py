#Raj scored 40, 70, 50 and 60 out of 100 in maths, science, Hindi and English. Find the percentage he got?

# take marks as input

print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

# Let's calculate the percentage of marks

sum = math + english + science + hindi
print ("The sum of Maths English Science and Hindi :" ,sum)

perc = (sum/400)*100

print(end="Percentage Mark = ")
print (perc)

