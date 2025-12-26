my_set = {1 , 2 , 3 , 4 , 4 , 5 , 5 , 6 , 7 , 8 , 9}
print(my_set)

my_set = {1.0 , "Hello" , (1 , 2 , 3)}
print(my_set)

my_set = {1 , 2 , 3 , 4 , 5 , 5 , 5 , 5 , 6 , 7 , 8}
print("\nInfo : Sets get rid of duplicates")
print(my_set)

my_set = set([1 , 2 , 3 , 4 , 3 , 2 , 1])
print(my_set ,"\n")

num_set = {0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10}
print("Orginal list is ",num_set)
num_set.pop()
print("After removing the first element from the set")
print(num_set , "becomes a part of natural numbers list from whole numbers list. \n")
