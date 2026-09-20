# 02-not-xor-shifts.py
# Topic: NOT, XOR, Left Shift, Right Shift

from colorama import Fore, Style, init

init(autoreset=True)


def bits(n, width=8):
    return format(n & ((1 << width) - 1), f"0{width}b")


def title(text):
    print(Fore.CYAN + Style.BRIGHT + "╔" + "═" * 50 + "╗")
    print(Fore.CYAN + Style.BRIGHT + f"║{text.center(50)}║")
    print(Fore.CYAN + Style.BRIGHT + "╚" + "═" * 50 + "╗")


def section(text):
    print("\n" + Fore.YELLOW + Style.BRIGHT + f"▶ {text}")
    print(Fore.YELLOW + "─" * 52)


# ---------------------------------------------------------
# INPUT
# ---------------------------------------------------------

title("NOT • XOR • SHIFT EXPLORER")

n = int(input(
    Fore.YELLOW +
    "\nEnter a number (try 5 or 12): "
))

guess = input(
    Fore.CYAN +
    f"Left shift doubles it. Guess: {n} << 1 = ? "
)


# ---------------------------------------------------------
# NOT
# ---------------------------------------------------------

input(
    Fore.YELLOW +
    "\nNOT — flips every bit. Press Enter to continue..."
)

section("NOT (~)")

print(
    Fore.GREEN +
    f"12       = {bits(12)}"
)

print(
    Fore.RED +
    f"~12      = {~12 & 0xFF:<3}" +
    Fore.WHITE +
    f"  Binary : {bits(~12)}"
)

print(
    Fore.WHITE +
    "\nNOT flips every bit:"
)

print(
    Fore.CYAN +
    "1 → 0    0 → 1"
)


# ---------------------------------------------------------
# XOR
# ---------------------------------------------------------

input(
    Fore.YELLOW +
    "\nXOR — different bits give 1. Press Enter to continue..."
)

section("XOR (^)")

a = 12
b = 10
result = a ^ b

print(
    Fore.GREEN +
    f"12       = {bits(a)}"
)

print(
    Fore.GREEN +
    f"10       = {bits(b)}"
)

print(
    Fore.LIGHTMAGENTA_EX +
    f"12 ^ 10  = {result:<3}" +
    Fore.WHITE +
    f"  Binary : {bits(result)}"
)

print(
    Fore.WHITE +
    "\nXOR rule:"
)

print(
    Fore.CYAN +
    "Same bits → 0     Different bits → 1"
)


# ---------------------------------------------------------
# LEFT SHIFT
# ---------------------------------------------------------

input(
    Fore.YELLOW +
    "\nLeft shift — multiplies by 2. Press Enter to continue..."
)

section("Left Shift (<<)")

left_result = n << 1

print(
    Fore.GREEN +
    f"{n:<3} << 1 = {left_result:<3}" +
    Fore.WHITE +
    f"  Binary : {bits(left_result)}"
)

print(
    Fore.WHITE +
    f"\nYour guess : {guess}"
)

if str(left_result) == guess.strip():
    print(
        Fore.GREEN +
        Style.BRIGHT +
        "✔ Correct! Left shift by 1 doubles the number."
    )
else:
    print(
        Fore.RED +
        Style.BRIGHT +
        f"✘ The answer is {left_result}."
    )


# ---------------------------------------------------------
# RIGHT SHIFT
# ---------------------------------------------------------

input(
    Fore.YELLOW +
    "\nRight shift — divides by 2. Press Enter to continue..."
)

section("Right Shift (>>)")

right_result = n >> 1

print(
    Fore.GREEN +
    f"{n:<3} >> 1 = {right_result:<3}" +
    Fore.WHITE +
    f"  Binary : {bits(right_result)}"
)

print(
    Fore.CYAN +
    "\nFor positive integers:"
)

print(
    Fore.WHITE +
    "Left shift  << 1  → × 2"
)

print(
    Fore.WHITE +
    "Right shift >> 1  → ÷ 2"
)


# ---------------------------------------------------------
# SUMMARY
# ---------------------------------------------------------

section("Quick Summary")

print(
    Fore.RED +
    "~n       → NOT → flips bits"
)

print(
    Fore.LIGHTMAGENTA_EX +
    "a ^ b    → XOR → different bits become 1"
)

print(
    Fore.GREEN +
    "n << 1   → Left shift → × 2"
)

print(
    Fore.BLUE +
    "n >> 1   → Right shift → ÷ 2"
)


print(
    "\n" +
    Fore.GREEN +
    Style.BRIGHT +
    "✔ Program Finished Successfully!"
) 