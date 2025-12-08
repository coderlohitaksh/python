L = [4 , 5 , 1 , 2 , 9 , 7 , 10 , 8]
print("The original list is :",L)
count = 0 

for i in L :
    count += i

avg = count/len(L)
print("\nThe sum of the numbers in the list is : ",count)
print("The average is : ",avg)

L.sort()
print("Smallest element of the list is : ",L[0])
print("Largest element of the list is : ",L[-1])
