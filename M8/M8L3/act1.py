
from colorama import Fore, Style, init

init(autoreset=True)


print(Fore.CYAN + "\n╔══════════════════════════════════════════════╗")
print(Fore.CYAN + "║" + Fore.GREEN + "              BIT OPERATIONS                  " + Fore.CYAN + "║")
print(Fore.CYAN + "╚══════════════════════════════════════════════╝")

input(Fore.LIGHTGREEN_EX + "\nXOR with 0 means we keep the number as it is . Press Enter to proceed .")
print(Fore.LIGHTGREEN_EX + "For example 5^0 gives ",5^0)
print(Fore.LIGHTGREEN_EX + "And also 9^0 gives ",9^0)

input(Fore.LIGHTRED_EX + "\nXOR with the number itself gives 0 . Press Enter to proceed .")
print(Fore.LIGHTRED_EX + "For example 5^5 gives ",5^5)
print(Fore.LIGHTRED_EX + "And also 9^9 gives ",9^9)

n = int(input(Fore.LIGHTBLUE_EX + "\nEnter a number (Try 6 or 11): "))
guess = input(Fore.LIGHTBLUE_EX + f"What is 3 ^ {n} ^ 3 ? ")
input(Fore.LIGHTBLUE_EX + "\nXor cancels the 3s because the 3s are repeated twice so the 3s disappear . Press Enter to proceed.")
print(Fore.LIGHTBLUE_EX + f"3 ^ {n} ^ 3 = ",3 ^ n ^ 3," your guess is ",guess)