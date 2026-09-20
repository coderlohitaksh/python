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


title("BITWISE POWER OF 2")

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how n & (n-1) clears the rightmost set bit..."
)

section("Clearing the rightmost set bit")

print(Fore.LIGHTYELLOW_EX + "12 & 11 =", 12 & 11)
print("12 in binary :", bits(12))
print("11 in binary :", bits(11))
print("Result       :", bits(12 & 11))

print()

print(Fore.LIGHTYELLOW_EX + "8 & 7 =", 8 & 7)
print("8 in binary  :", bits(8))
print("7 in binary  :", bits(7))
print("Result       :", bits(8 & 7))


section("Checking whether a number is a power of 2")

n = int(
    input(
        Fore.LIGHTGREEN_EX
        + "Enter a number (try 4 or 6): "
    )
)

guess = input(
    Fore.LIGHTGREEN_EX
    + f"Is {n} a power of 2? (Yes / No): "
).strip().lower()

input(
    Fore.LIGHTYELLOW_EX
    + "\nPress Enter to check using n & (n-1)..."
)

is_power_of_2 = n > 0 and (n & (n - 1)) == 0

print()
print("Number :", n)
print("Binary :", bits(n))

if is_power_of_2:
    print(Fore.GREEN + "Result : YES — it is a power of 2.")
else:
    print(Fore.RED + "Result : NO — it is not a power of 2.")

correct_guess = (
    (guess == "yes" and is_power_of_2)
    or
    (guess == "no" and not is_power_of_2)
)

if correct_guess:
    print(Fore.GREEN + "Your guess is CORRECT!")
else:
    print(Fore.RED + "Your guess is INCORRECT.")