from colorama import Fore

num1 = [1 , 2 , 3 , 4 , 5]
num2 = [6 , 7 , 8 , 9 , 10]
result = map(lambda x , y: x + y , num1 , num2)
print(Fore.RED + "\nAddition of 2 lists is ",(list(result)))

nums = [1 , 2 , 3 , 4 , 5 , 6]
def sq(n):
    return n * n

square = list(map(sq , nums))
print(Fore.GREEN + "Square of number in list are ",square)