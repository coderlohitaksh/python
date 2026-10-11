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


title("Sum_down")

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how a function calls itself until it reaches a base case, and calculates the total from a number down to 0...."
)

print(Fore.LIGHTMAGENTA_EX + f"The sum down of 3 is 3 + 2 + 1 + 0 , which gives the result {sum_down(3)}.")
print(Fore.LIGHTMAGENTA_EX + f"The sum down of 5 is 5 + 4 + 3 + 2 + 1 + 0 , which gives the result {sum_down(5)}.")

n = int(input(Fore.LIGHTGREEN_EX + "Enter a number to be sum downed : "))
guess = int(input(Fore.LIGHTGREEN_EX + f"Which number are you thinking that is the sum down of {n}.: "))
input(Fore.LIGHTGREEN_EX + f"Sum down adds the number to the (number - 1) untill it reaches 0 . Press Enter to proceed ")
print(Fore.LIGHTGREEN_EX + f"Sum down of {n} is {sum_down(n)} . your guess is {guess} .")
