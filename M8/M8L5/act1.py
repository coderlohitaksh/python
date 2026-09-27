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


title("XOR Swap")

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how XOR swaps two nmbers without a third variable..."
)

print(Fore.LIGHTGREEN_EX + "\nBefore, a = 5 and b = 9")
a , b = 5 , 9
a ^= b ; b ^= a ; a ^= b
print(Fore.LIGHTGREEN_EX + f"Now, a = {a} and b = {b}")

n = int(input(Fore.LIGHTRED_EX + "\nEnter a number (try 3 or 7) : "))
guess = input(Fore.LIGHTRED_EX + f"After XOR swap of {n} and 8 what does n become? ")
a , b = n , 8
a ^= b ; b ^= a ; a ^= b
input(Fore.LIGHTBLUE_EX + "\nXOR swap changes the values . Press Enter")
print(Fore.LIGHTBLUE_EX + f"The n becomes {a} , your guess is {guess}.")