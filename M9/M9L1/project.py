from colorama import Fore, Style, init
import time

init(autoreset=True)

def title(text):
    print(Fore.CYAN + Style.BRIGHT + "═" * 40)
    print(Fore.CYAN + Style.BRIGHT + text.center(40))
    print(Fore.CYAN + Style.BRIGHT + "═" * 40)

def section(text):
    print(Fore.YELLOW + "\n▶ " + text)
    print(Fore.YELLOW + "─" * 40)

def countdown(n):
    if n < 0:
        print(Fore.GREEN + "Time's up!")
        return
    print(Fore.CYAN + str(n))
    time.sleep(1)
    countdown(n - 1)

def countup(n):
    if n > 5:
        print(Fore.GREEN + "Count-up complete!")
        return
    print(Fore.MAGENTA + str(n))
    time.sleep(1)
    countup(n + 1)

title("MY COUNTDOWN TIMER")

while True:
    section("MENU")
    print(Fore.LIGHTYELLOW_EX + "1. Countdown")
    print(Fore.LIGHTYELLOW_EX + "2. Count-up")
    print(Fore.LIGHTYELLOW_EX + "3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        n = int(input(Fore.LIGHTCYAN_EX + "Start countdown from: "))
        countdown(n)

    elif choice == "2":
        countup(1)

    elif choice == "3":
        print(Fore.GREEN + "Goodbye!")
        break

    else:
        print(Fore.RED + "Invalid choice!")
