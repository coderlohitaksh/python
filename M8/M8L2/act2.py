from colorama import Fore, Style, init

init(autoreset=True)


print(Fore.CYAN + "\n╔══════════════════════════════════════════════╗")
print(Fore.CYAN + "║" + Fore.GREEN + "              FIRST SET BIT                  " + Fore.CYAN + "║")
print(Fore.CYAN + "╚══════════════════════════════════════════════╝")


print(Fore.CYAN + "\nWhat is a Set Bit?")

print(Fore.YELLOW + "\n┌──────────────────────────────┬────────────────────┐")
print(Fore.YELLOW + "│ Term                         │ Meaning            │")
print(Fore.YELLOW + "├──────────────────────────────┼────────────────────┤")
print(Fore.CYAN + "│ Set bit                      │ A bit with value 1 │")
print(Fore.CYAN + "│ First set bit                │ Rightmost 1        │")
print(Fore.CYAN + "│ Position counting            │ Starts from 0      │")
print(Fore.YELLOW + "└──────────────────────────────┴────────────────────┘")


print(Fore.CYAN + "\nExamples")

print(Fore.YELLOW + "\n┌──────────────────────────────┬────────────────────┐")
print(Fore.YELLOW + "│ Number                       │ Binary / Position  │")
print(Fore.YELLOW + "├──────────────────────────────┼────────────────────┤")

print(Fore.CYAN + f"│ 5                            │ {bin(5)[2:]:<18} │")
print(Fore.CYAN + "│ First 1                      │ Position 0         │")

print(Fore.CYAN + f"│ 8                            │ {bin(8)[2:]:<18} │")
print(Fore.CYAN + "│ First 1                      │ Position 3         │")

print(Fore.YELLOW + "└──────────────────────────────┴────────────────────┘")


print(Fore.CYAN + "\nFind the First Set Bit")

n = int(input("Enter a number (try 8 or 14): "))

input(
    Fore.YELLOW
    + "Watch bits drop until the first 1 appears. Press Enter "
)

temp = n
pos = 0

while temp > 0:

    last_bit = temp & 1

    print(
        Fore.CYAN
        + f"  Binary: {bin(temp)[2:]:<10}  Last bit: {last_bit}"
    )

    if last_bit:
        break

    pos += 1
    temp >>= 1


print(Fore.YELLOW + "\n┌──────────────────────────────┬────────────────────┐")
print(Fore.YELLOW + "│ Property                     │ Value              │")
print(Fore.YELLOW + "├──────────────────────────────┼────────────────────┤")

print(Fore.CYAN + f"│ Number                       │ {n:<18} │")
print(Fore.CYAN + f"│ Binary                       │ {bin(n)[2:]:<18} │")
print(Fore.CYAN + f"│ First set bit position       │ {pos:<18} │")

print(Fore.YELLOW + "└──────────────────────────────┴────────────────────┘")


print(Fore.CYAN + "\nHow It Works")

print(Fore.YELLOW + "\n┌──────────────────────────────┬────────────────────┐")
print(Fore.YELLOW + "│ Operation                    │ Purpose            │")
print(Fore.YELLOW + "├──────────────────────────────┼────────────────────┤")

print(Fore.CYAN + "│ temp & 1                     │ Check last bit     │")
print(Fore.CYAN + "│ temp >> 1                    │ Drop last bit      │")
print(Fore.CYAN + "│ pos += 1                     │ Move position      │")

print(Fore.YELLOW + "└──────────────────────────────┴────────────────────┘")


if n > 0:

    print(
        Fore.GREEN
        + f"\n✓ First set bit in {n} is at position {pos}"
    )

else:  

    print(
        Fore.RED
        + "\n✗ No set bit exists because the number is 0."
    )