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

def sum_down(n):
    if n == 0:
        return 0 
    return n + sum_down(n - 1)

title("Stack Overflow")

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how each recursive call adds a new frame to the call stack and demonstrates how the number of stack frames grows with the input value....")

print(Fore.LIGHTRED_EX + f"The sum down of 3 is {sum_down(3)} , which uses 3 frames.")
print(Fore.LIGHTRED_EX + f"The sum down of 5 is {sum_down(5)} , which uses 5 frames.")

n = int(input(Fore.LIGHTYELLOW_EX + f"Enter any number you like : "))
input(Fore.LIGHTYELLOW_EX + "The Sum down of n is n + (n-1) + ... + 1 uses n frames. Press Enter to Proceed.")
print(Fore.LIGHTYELLOW_EX + f"\nThe sum down of {n} is {sum_down(n)} , {n} frames were used.")