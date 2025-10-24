import random
import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

choice = ("rock", "paper", "scissor")
user_choice = str(input(Fore.CYAN + "rock, paper or scissor:\n")).lower()

print(Fore.YELLOW + "Computer is choosing", end="")
for i in range(3):
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(0.5)
print()

comp_choice = random.choice(choice)

print(Fore.GREEN + "You chose:", user_choice)
print(Fore.MAGENTA + "Computer chose:", comp_choice)

if user_choice == comp_choice:
    print(Fore.YELLOW + "It's a tie.")
elif user_choice == "rock" and comp_choice == "scissor":
    print(Fore.GREEN + "Rock smashes scissor, you win 🎉")
elif user_choice == "paper" and comp_choice == "rock":
    print(Fore.GREEN + "Paper covers rock, you win 🎉")
elif user_choice == "scissor" and comp_choice == "paper":
    print(Fore.GREEN + "Scissor cuts paper, you win 🎉")
else:
    print(Fore.RED + "You lost 😢")

print(Style.RESET_ALL)
