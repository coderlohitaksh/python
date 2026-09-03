from colorama import Fore, Style, init

init(autoreset=True)


print(Fore.CYAN + "\n╔══════════════════════════════════════════════╗")

print(
    Fore.CYAN
    + "║"
    + Fore.GREEN
    + "       TWO ODD-OCCURRING NUMBERS              "
    + Fore.CYAN
    + "║"
)

print(Fore.CYAN + "╚══════════════════════════════════════════════╝")


input(
    Fore.LIGHTGREEN_EX
    + "\nXOR cancels numbers that occur in pairs. "
      "Press Enter to proceed."
)

print(
    Fore.LIGHTGREEN_EX
    + "\nExample: [1, 4, 3, 3]"
)

print(
    Fore.LIGHTGREEN_EX
    + "XOR of all numbers = ",
    1 ^ 4 ^ 3 ^ 3,
    "  binary = ",
    bin(1 ^ 4 ^ 3 ^ 3)[2:]
)


input(
    Fore.LIGHTRED_EX
    + "\nThe two 3s cancel each other. "
      "The remaining XOR is 1 ^ 4 = 5. "
      "Press Enter to proceed."
)


print(
    Fore.LIGHTRED_EX
    + "1 ^ 4 ^ 3 ^ 3 = ",
    1 ^ 4 ^ 3 ^ 3
)

print(
    Fore.LIGHTRED_EX
    + "Binary: ",
    bin(1 ^ 4 ^ 3 ^ 3)[2:]
)


input(
    Fore.LIGHTYELLOW_EX
    + "\nNow find the RIGHTMOST SET BIT. "
      "This bit is ON in one odd-occurring number "
      "and OFF in the other. "
      "Press Enter to proceed."
)


print(
    Fore.LIGHTYELLOW_EX
    + "\nFor 1 ^ 4 = 5:"
)

print(
    Fore.LIGHTYELLOW_EX
    + "1 in binary = 001"
)

print(
    Fore.LIGHTYELLOW_EX
    + "4 in binary = 100"
)

print(
    Fore.LIGHTYELLOW_EX
    + "5 in binary = 101"
)


input(
    Fore.LIGHTMAGENTA_EX
    + "\nThe rightmost set bit is bit 0. "
      "Press Enter to see the split."
)


print(
    Fore.LIGHTMAGENTA_EX
    + "\nSplit using bit 0:"
)

print(
    Fore.LIGHTMAGENTA_EX
    + "Group A (bit 0 ON)  → 1"
)

print(
    Fore.LIGHTMAGENTA_EX
    + "Group B (bit 0 OFF) → 4"
)


n = int(
    input(
        Fore.LIGHTBLUE_EX
        + "\nEnter a number (Try 6 or 9): "
    )
)


guess = input(
    Fore.LIGHTBLUE_EX
    + f"Is bit 0 of {n} ON? (yes/no): "
)


input(
    Fore.LIGHTBLUE_EX
    + "\nCheck the split bit. Press Enter to proceed."
)


print(
    Fore.LIGHTGREEN_EX
    + f"\n{n} in binary = {bin(n)[2:]}"
)


if n & 1:

    print(
        Fore.LIGHTGREEN_EX
        + f"{n} → bit 0 ON → Group A"
    )

    print(
        Fore.LIGHTGREEN_EX
        + "Your guess: ",
        guess
    )

else:

    print(
        Fore.LIGHTRED_EX
        + f"{n} → bit 0 OFF → Group B"
    )

    print(
        Fore.LIGHTRED_EX
        + "Your guess: ",
        guess
    )