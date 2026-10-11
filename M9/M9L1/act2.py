from colorama import Fore, Style, init

init(autoreset=True)

def bits(n, width=8):
    return format(n & ((1 << width) - 1), f"0{width}b")


def title(text):
    print(Fore.CYAN + Style.BRIGHT + "╔" + "═" * 50 + "╗")
    print(Fore.CYAN + Style.BRIGHT + f"║{text.center(50)}║")
    print(Fore.CYAN + Style.BRIGHT + "╚" + "═" * 50 + "╝")


def section(text):
    print("\n" + Fore.YELLOW + Style.BRIGHT + f"▶ {text}")
    print(Fore.YELLOW + "─" * 52)

def factorial(n):
    if n == 0 :
        return 1
    return n * factorial(n - 1)

title("Factorials")

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how factorial using recursion, multiplies n by factorial(n-1), and stops at the base case 0! = 1...."
)

print(Fore.LIGHTCYAN_EX + f"4's factorial is 4 * 3 * 2 * 1 , which gives the result {factorial(4)}.")
print(Fore.LIGHTCYAN_EX + f"7's factorial is 7 * 6 * 5 * 4 * 3 * 2 * 1 , which gives the result {factorial(7)}.")

n = int(input(Fore.LIGHTGREEN_EX + "Enter any number you like : "))
guess = int(input(Fore.LIGHTGREEN_EX + f"Enter the factorial of the number {n} : "))
input(Fore.LIGHTGREEN_EX + 
      "A number's factorial means number * (the same number - 1) until base case 0! = 1 . Press Enter to Proceed .")
print(Fore.LIGHTGREEN_EX + f"{n}'s factorial is {factorial(n)} , your guess is {guess}.")