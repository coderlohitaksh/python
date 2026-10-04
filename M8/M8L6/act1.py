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


title("Power set")

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how power set has n elements has 2^n elements....") 

print(Fore.LIGHTGREEN_EX + "\nIf we have 3 elements , it means we have 2^3 = ",2**3," subsets.")
print(Fore.LIGHTGREEN_EX + "E.x.: The mask of 5 is the binary of 5 ,",bin(5)[2:]," which means the set bits are at the index 0 and 2.")

n = int(input(Fore.LIGHTBLUE_EX + ("Enter the number of elements (try 4 or 5): ")))
guess = int(input(Fore.LIGHTBLUE_EX + f"How many subsets does set {n} have ?"))
input(Fore.LIGHTYELLOW_EX + "Each element is in or out. Press Enter")
print(Fore.LIGHTYELLOW_EX + f"\nThe element's subsets is {2**n} your guess is {guess}")