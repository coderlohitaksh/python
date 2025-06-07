#Write a program to calculate the number of notes in the given amount?

#Total as input
amount = int(input("Please enter your amount for withdraw"))

#Calculating the number of notes

n1 = amount//100
n2 = (amount%100)//50
n3 = ((amount%100)%50)//10


print ("note of 100 rupees is : " , n1)
print ("note of 50 rupees is : " , n2)
print ("note of 10 rupees is : " , n3
       