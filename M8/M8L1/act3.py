# 03-parity-bits.py
# Topic: Parity Check and Counting Bits

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


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

title("PARITY • BIT COUNTING EXPLORER")


# ---------------------------------------------------------
# PARITY
# ---------------------------------------------------------

input(
    Fore.YELLOW +
    "\nParity — last bit tells even or odd. "
    "Press Enter to continue..."
)

section("Parity Check (& 1)")

print(
    Fore.WHITE +
    "\nThe last binary bit tells us whether a number is:"
)

print(
    Fore.CYAN +
    "Last bit = 0  →  EVEN"
)

print(
    Fore.CYAN +
    "Last bit = 1  →  ODD"
)

print(
    Fore.WHITE +
    "\nExample:"
)

numbers = [2, 3, 4, 5, 8, 9]

for n in numbers:

    if n & 1:
        print(
            Fore.RED +
            f"  {n:<3} = {bits(n)}  →  ODD"
        )
    else:
        print(
            Fore.GREEN +
            f"  {n:<3} = {bits(n)}  →  EVEN"
        )


# ---------------------------------------------------------
# HOW & 1 WORKS
# ---------------------------------------------------------

input(
    Fore.YELLOW +
    "\nHow does n & 1 work? Press Enter to continue..."
)

section("Why n & 1 Detects Parity")

n = 5

print(
    Fore.GREEN +
    f"\n{n:<3} = {bits(n)}"
)

print(
    Fore.GREEN +
    f"1   = {bits(1)}"
)

print(
    Fore.LIGHTMAGENTA_EX +
    f"{n} & 1 = {n & 1}"
)

print(
    Fore.WHITE +
    "\nOnly the last bit matters:"
)

print(
    Fore.CYAN +
    "0 & 1 = 0  → EVEN"
)

print(
    Fore.CYAN +
    "1 & 1 = 1  → ODD"
)


# ---------------------------------------------------------
# USER INPUT
# ---------------------------------------------------------

input(
    Fore.YELLOW +
    "\nNow you try it. Press Enter to continue..."
)

n = int(
    input(
        Fore.YELLOW +
        "\nEnter a number (try 13 or 7): "
    )
)

result = n & 1

print(
    Fore.WHITE +
    f"\n{n:<3} = {bits(n)}"
)

print(
    Fore.LIGHTMAGENTA_EX +
    f"{n} & 1 = {result}"
)

if result == 1:
    print(
        Fore.RED +
        Style.BRIGHT +
        f"✔ {n} is ODD."
    )
else:
    print(
        Fore.GREEN +
        Style.BRIGHT +
        f"✔ {n} is EVEN."
    )


# ---------------------------------------------------------
# COUNTING 1s
# ---------------------------------------------------------

input(
    Fore.YELLOW +
    "\nCount the 1s — watch the bits drop off. "
    "Press Enter to continue..."
)

section("Counting 1 Bits")

temp = n
count = 0

while temp > 0:

    last_bit = temp & 1

    print(
        Fore.WHITE +
        f"  {bits(temp):>8}" +
        Fore.CYAN +
        f"   last bit = {last_bit}"
    )

    if last_bit == 1:
        count += 1

    temp >>= 1


# ---------------------------------------------------------
# RESULT
# ---------------------------------------------------------

section("Bit Count Result")

print(
    Fore.GREEN +
    f"\nNumber      : {n}"
)

print(
    Fore.GREEN +
    f"Binary      : {bits(n)}"
)

print(
    Fore.LIGHTMAGENTA_EX +
    f"Number of 1s: {count}"
)

print(
    Fore.WHITE +
    f"\nPython check: bin({n}).count('1') = "
    + Fore.CYAN +
    f"{bin(n).count('1')}"
)


# ---------------------------------------------------------
# QUICK SUMMARY
# ---------------------------------------------------------

section("Quick Summary")

print(
    Fore.GREEN +
    "n & 1       → checks whether n is even or odd"
)

print(
    Fore.CYAN +
    "Last bit 0  → EVEN"
)

print(
    Fore.RED +
    "Last bit 1  → ODD"
)

print(
    Fore.LIGHTMAGENTA_EX +
    "n >> 1      → removes the last binary bit"
)

print(
    Fore.YELLOW +
    "Counting 1s → count how many 1-bits are present"
)


# ---------------------------------------------------------
# FINISHED
# ---------------------------------------------------------

print(
    "\n" +
    Fore.GREEN +
    Style.BRIGHT +
    "✔ Program Finished Successfully!"
)