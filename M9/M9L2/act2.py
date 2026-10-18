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

def mirror(n):
    if n == 0:
        return 0
    rest = mirror(n-1)
    return rest + 2*n

title("Bounce")

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how Python uses head recursion by making the recursive call first and then adding values while the function unwinds back up.....")

print(Fore.LIGHTGREEN_EX + f"\nThe mirror of 3 is {mirror(3)} , which is 3 + 2 + 1 + 0 + 1 + 2 + 3.")
print(Fore.LIGHTGREEN_EX + f"The mirror of 4 is {mirror(4)} , which is 4 + 3 + 2 + 1 + 0 + 1 + 2 + 3 + 4.")

n = int(input(Fore.LIGHTCYAN_EX + "\nEnter a number you like : "))
guess = input(Fore.LIGHTCYAN_EX + f"What do you think is the mirror of {n} ?: ")

input(Fore.LIGHTYELLOW_EX + "\nThe mirror of a number is {(mirror of the number) - 1} + (2 * the number) , this line adds (2 * the number) because it unwinds the number back up from down.    Press Enter to Proceed")

print(Fore.LIGHTCYAN_EX + f"\nThe mirror of {n} is {mirror(n)}, your guess is {guess}.")