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


title("Sign Detection")

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how XOR compares the signs of two numbers and shows how a negative XOR result can indicate that the numbers have different signs....") 

input(Fore.LIGHTRED_EX + "XOR sign detection - n ^ m < 0 means different signs.  Press Enter ")
print(Fore.LIGHTRED_EX + "  4 ^ 2 =", 4 ^ 2, Fore.LIGHTRED_EX + "  same signs  positive")
print(Fore.LIGHTRED_EX + "  4 ^ -2 =", 4 ^ -2,Fore.LIGHTRED_EX + "  different signs  negative")

n = int(input(Fore.LIGHTYELLOW_EX + "Enter a number (try 5 or -3): "))
guess = input(Fore.LIGHTYELLOW_EX + f"Will {n}^ -8 be positive or negative? ")
input(Fore.LIGHTYELLOW_EX + "XOR is negative when signs differ.  Press Enter ")
print(Fore.LIGHTYELLOW_EX + f"\n {n}  ^ -8 = {n ^ - 8} , your guess is {guess}")