from colorama import Fore, Style, init

init(autoreset=True)

def bits(n, width=8):
    return format(n & ((1 << width) - 1), f"0{width}b")


def title(text):
    print(Fore.CYAN + Style.BRIGHT + "╔" + "═" * 50 + "╗")
    print(Fore.CYAN + Style.BRIGHT + f"║{text.center(50)}║")
    print(Fore.CYAN + Style.BRIGHT + "╚" + "═" * 50 + "╝")

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def section(text):
    print("\n" + Fore.YELLOW + Style.BRIGHT + f"▶ {text}")
    print(Fore.YELLOW + "─" * 52)

title("Fibonacci")

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how Python uses Fibonacci to demonstrate tree recursion, where each function call creates two more recursive calls until the base cases are reached.....")

print(Fore.LIGHTGREEN_EX + f"\nThe fibonacci number of 5th position is {fib(5)}.")
print(Fore.LIGHTGREEN_EX + f"The fibonacci number of 6th position is {fib(6)}.")

n = int(input(Fore.LIGHTCYAN_EX + "\nEnter a number you want so it will be fibonacci : ")) 
guess = input(Fore.LIGHTCYAN_EX + f"What do you think will be the fibonacci of {n} : ")

input(Fore.LIGHTYELLOW_EX + "\nThe formula of Fibonacci is (the fibonacci of number) = (the fibonacci of (number - 1)) + (the fibonacci of (number - 2)) . The base is (fibonnaci of 0) = 1 & (fibonnaci of 1) = 1. Press Enter to Proceed.")

print(Fore.LIGHTCYAN_EX + f"\nThe fibbonaci of {n} is {fib(n)} , your guess is {guess}.")
