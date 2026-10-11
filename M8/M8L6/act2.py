from colorama import Fore, Style, init

init(autoreset=True)ki/yh/

def bits(n, width=8):
    return format(n & ((1 << width) - 1), f"0{width}b")


def title(text):
    print(Fore.CYAN + Style.BRIGHT + "╔" + "═" * 50 + "╗")
    print(Fore.CYAN + Style.BRIGHT + f"║{text.center(50)}║")
    print(Fore.CYAN + Style.BRIGHT + "╚" + "═" * 50 + "╝")


def section(text):
    print("\n" + Fore.YELLOW + Style.BRIGHT + f"▶ {text}")
    print(Fore.YELLOW + "─" * 52)


def reveal(text):
    print(Fore.LIGHTYELLOW_EX + text)


title("Bit Probe")

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how (n >> j) & 1 checks whether a bit is ON or OFF..."
)

print(
    Fore.MAGENTA
    + f"\n12's binary is {bin(12)[2:]}, "
    f"bit 2 is {(12 >> 2) & 1}, "
    f"bit 1 is {(12 >> 1) & 1}."
)

print(
    Fore.MAGENTA
    + f"\n7's binary is {bin(7)[2:]}, "
    f"bit 2 is {(7 >> 2) & 1}, "
    f"bit 1 is {(7 >> 1) & 1}."
)

n = int(input(Fore.LIGHTMAGENTA_EX + "Enter a number (try 9 or 6): "))

print(Fore.LIGHTMAGENTA_EX + f"{n}'s binary is {bin(n)[2:]}")

correct = (n >> 2) & 1

guess = input(
    Fore.LIGHTMAGENTA_EX
    + f"What is bit 2 of {n}? Enter 0 or 1: "
).strip()

input(
    Fore.LIGHTYELLOW_EX
    + "Bit probe: (n >> 2) & 1 gives the bit value. Press Enter to reveal."
)

print(Fore.LIGHTMAGENTA_EX + f"\n{n}'s bit 2 is {correct}.")

if guess == str(correct):
    reveal(Fore.LIGHTGREEN_EX + "Correct! Excellent work!")
else:
    reveal(
        Fore.LIGHTRED_EX
        + f"Not quite. Your answer was {guess}. "
        + f"The correct answer is {correct}."
    )
