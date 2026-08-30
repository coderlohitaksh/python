# 03-mask-and-check.py
# Topic: Building a Bit Mask, Check if Nth Bit is Set

from colorama import Fore, Style, init

init(autoreset=True)


print(Fore.CYAN + "\n╔══════════════════════════════════════════════╗")
print(Fore.CYAN + "║" + Fore.GREEN + "              BIT MASK & CHECK               " + Fore.CYAN + "║")
print(Fore.CYAN + "╚══════════════════════════════════════════════╝")


# --------------------------------------------------
# What is a Bit Mask?
# --------------------------------------------------

print(Fore.CYAN + "\nWhat is a Bit Mask?")

print(Fore.YELLOW + "\n┌──────────────────────────────┬────────────────────┐")
print(Fore.YELLOW + "│ Term                         │ Meaning            │")
print(Fore.YELLOW + "├──────────────────────────────┼────────────────────┤")
print(Fore.CYAN + "│ Bit mask                     │ A number used to   │")
print(Fore.CYAN + "│                              │ check specific bit │")
print(Fore.CYAN + "│ Set bit                      │ A bit with value 1 │")
print(Fore.CYAN + "│ Bit position                 │ Starts from 0      │")
print(Fore.YELLOW + "└──────────────────────────────┴────────────────────┘")


# --------------------------------------------------
# Building a Bit Mask
# --------------------------------------------------

print(Fore.CYAN + "\nBuild a Bit Mask")

print(
    Fore.YELLOW
    + "\nA mask is created using:  1 << k"
)

print(
    Fore.CYAN
    + "This places exactly one 1 at position k."
)

input(
    Fore.YELLOW
    + "\nBuild the masks for positions 0 to 3. Press Enter "
)


print(Fore.YELLOW + "\n┌──────────────┬──────────────┬────────────────────┐")
print(Fore.YELLOW + "│ Bit Position │ Mask Value   │ Binary             │")
print(Fore.YELLOW + "├──────────────┼──────────────┼────────────────────┤")

for k in range(4):

    mask = 1 << k

    print(
        Fore.CYAN
        + f"│ {k:<12} │ {mask:<12} │ {bin(mask)[2:]:<18} │"
    )

print(Fore.YELLOW + "└──────────────┴──────────────┴────────────────────┘")


# --------------------------------------------------
# Example
# --------------------------------------------------

print(Fore.CYAN + "\nExample")

print(Fore.YELLOW + "\nFor bit position 2:")

print(Fore.CYAN + "  1 << 2")
print(Fore.CYAN + "  = 0100")
print(Fore.CYAN + "  = 4")

print(
    Fore.GREEN
    + "\nSo the mask for bit 2 is 4."
)


# --------------------------------------------------
# Check if Nth Bit is Set
# --------------------------------------------------

print(Fore.CYAN + "\nCheck if the Nth Bit is Set")

n = int(
    input(
        Fore.WHITE
        + "\nEnter a number (try 42 or 13): "
    )
)

guess = input(
    Fore.WHITE
    + "Is bit 2 of "
    + str(n)
    + " ON? (yes/no): "
)


input(
    Fore.YELLOW
    + "\nCheck bit 2 using AND with the mask. Press Enter "
)


# --------------------------------------------------
# Bit Checking
# --------------------------------------------------

mask = 1 << 2

result = n & mask


print(Fore.CYAN + "\nHow the Check Works")

print(Fore.YELLOW + "\n┌──────────────────────────────┬────────────────────┐")
print(Fore.YELLOW + "│ Operation                    │ Purpose            │")
print(Fore.YELLOW + "├──────────────────────────────┼────────────────────┤")

print(Fore.CYAN + "│ 1 << 2                       │ Create bit-2 mask   │")
print(Fore.CYAN + "│ n & mask                     │ Check bit 2         │")
print(Fore.CYAN + "│ result != 0                  │ Bit 2 is ON         │")
print(Fore.CYAN + "│ result == 0                  │ Bit 2 is OFF        │")

print(Fore.YELLOW + "└──────────────────────────────┴────────────────────┘")


# --------------------------------------------------
# Show Calculation
# --------------------------------------------------

print(Fore.CYAN + "\nCalculation")

print(
    Fore.CYAN
    + f"  Number : {n}"
)

print(
    Fore.CYAN
    + f"  Binary : {bin(n)[2:]}"
)

print(
    Fore.CYAN
    + f"  Mask   : {mask}"
)

print(
    Fore.CYAN
    + f"  Mask binary : {bin(mask)[2:]}"
)

print(
    Fore.CYAN
    + f"\n  {n} & {mask} = {result}"
)


# --------------------------------------------------
# Final Result
# --------------------------------------------------

print(Fore.YELLOW + "\n┌──────────────────────────────┬────────────────────┐")
print(Fore.YELLOW + "│ Property                     │ Value              │")
print(Fore.YELLOW + "├──────────────────────────────┼────────────────────┤")

print(
    Fore.CYAN
    + f"│ Number                       │ {n:<18} │"
)

print(
    Fore.CYAN
    + f"│ Binary                       │ {bin(n)[2:]:<18} │"
)

print(
    Fore.CYAN
    + f"│ Bit position checked        │ {2:<18} │"
)

print(
    Fore.CYAN
    + f"│ Mask                         │ {mask:<18} │"
)

print(
    Fore.CYAN
    + f"│ AND result                   │ {result:<18} │"
)

print(Fore.YELLOW + "└──────────────────────────────┴────────────────────┘")


if result:

    print(
        Fore.GREEN
        + f"\n✓ Bit 2 of {n} is ON."
        + f"  |  Your guess: {guess}"
    )

else:

    print(
        Fore.RED
        + f"\n✗ Bit 2 of {n} is OFF."
        + f"  |  Your guess: {guess}"
    )  