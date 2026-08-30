from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + "\n╔══════════════════════════════════════════════╗")
print(Fore.CYAN + "║" + Fore.GREEN + "                  BIT PLAY                    " + Fore.CYAN + "║")
print(Fore.CYAN + "╚══════════════════════════════════════════════╝")

n = 52

def bits(n):
    return bin(n)[2:]

print(Fore.YELLOW + "\n┌────────────────────┬────────────────────┐")
print(Fore.YELLOW + "│ Property           │ Value              │")
print(Fore.YELLOW + "├────────────────────┼────────────────────┤")
print(Fore.CYAN + f"│ Number             │ {n:<18} │")
print(Fore.CYAN + f"│ Binary             │ {bits(n):<18} │")
print(Fore.CYAN + f"│ Set bits           │ {bits(n).count('1'):<18} │")
print(Fore.CYAN + f"│ Zero bits          │ {bits(n).count('0'):<18} │")
print(Fore.YELLOW + "└────────────────────┴────────────────────┘")

#

count, temp = 0, n

while temp:
    if temp & 1:
        count += 1
    temp >>= 1

print(Fore.YELLOW + "\n┌──────────────────────────────┬──────────────┐")
print(Fore.YELLOW + "│ Operation                    │ Result       │")
print(Fore.YELLOW + "├──────────────────────────────┼──────────────┤")
print(Fore.CYAN + f"│ Set bits using loop          │ {count:<12} │")
print(Fore.YELLOW + "└──────────────────────────────┴──────────────┘")

#

pos, temp = 1, n

while temp:
    if temp & 1:
        break
    pos += 1
    temp >>= 1

print(Fore.YELLOW + "\n┌──────────────────────────────┬──────────────┐")
print(Fore.YELLOW + "│ Operation                    │ Result       │")
print(Fore.YELLOW + "├──────────────────────────────┼──────────────┤")
print(Fore.CYAN + f"│ First set bit position       │ {pos:<12} │")
print(Fore.YELLOW + "└──────────────────────────────┴──────────────┘")

#

print(Fore.CYAN + "\nBit mask (1 << i):")

print(Fore.YELLOW + "\n┌──────────┬──────────┬──────────────┐")
print(Fore.YELLOW + "│ i        │ 1 << i   │ Binary       │")
print(Fore.YELLOW + "├──────────┼──────────┼──────────────┤")

for i in range(6):
    mask = 1 << i
    print(Fore.CYAN + f"│ {i:<8} │ {mask:<8} │ {bits(mask):<12} │")

print(Fore.YELLOW + "└──────────┴──────────┴──────────────┘")

# 

print(Fore.CYAN + "\nIndividual Bit Values:")

print(Fore.YELLOW + "\n┌──────────┬──────────────┬──────────────┐")
print(Fore.YELLOW + "│ Bit      │ Mask         │ Status       │")
print(Fore.YELLOW + "├──────────┼──────────────┼──────────────┤")

for bit in range(1, 7):
    mask = 1 << (bit - 1)
    result = "SET" if n & mask else "NOT SET"
    print(Fore.CYAN + f"│ {bit:<8} │ {mask:<12} │ {result:<12} │")

print(Fore.YELLOW + "└──────────┴──────────────┴──────────────┘")

from colorama import Fore, Style, init

init(autoreset=True)


print(Fore.CYAN + "\n╔══════════════════════════════════════════════╗")
print(Fore.CYAN + "║" + Fore.GREEN + "              BIT OPERATIONS                  " + Fore.CYAN + "║")
print(Fore.CYAN + "╚══════════════════════════════════════════════╝")


def bits(n):
    return bin(n)[2:]


print(Fore.CYAN + "\nSET A BIT — OR (|) turns a bit ON")

a = 5
b = 2
result = a | b

print(Fore.YELLOW + "\n┌────────────────────┬────────────────────┐")
print(Fore.YELLOW + "│ Property           │ Value              │")
print(Fore.YELLOW + "├────────────────────┼────────────────────┤")
print(Fore.CYAN + f"│ First number       │ {a:<18} │")
print(Fore.CYAN + f"│ Binary             │ {bits(a):<18} │")
print(Fore.CYAN + f"│ OR mask            │ {b:<18} │")
print(Fore.CYAN + f"│ Mask binary        │ {bits(b):<18} │")
print(Fore.CYAN + f"│ Result             │ {result:<18} │")
print(Fore.CYAN + f"│ Result binary      │ {bits(result):<18} │")
print(Fore.YELLOW + "└────────────────────┴────────────────────┘")

print(Fore.CYAN + "\nZERO A BIT — AND (&) turns a bit OFF")

a = 7
b = 5
result = a & b

print(Fore.YELLOW + "\n┌────────────────────┬────────────────────┐")
print(Fore.YELLOW + "│ Property           │ Value              │")
print(Fore.YELLOW + "├────────────────────┼────────────────────┤")
print(Fore.CYAN + f"│ First number       │ {a:<18} │")
print(Fore.CYAN + f"│ Binary             │ {bits(a):<18} │")
print(Fore.CYAN + f"│ AND mask           │ {b:<18} │")
print(Fore.CYAN + f"│ Mask binary        │ {bits(b):<18} │")
print(Fore.CYAN + f"│ Result             │ {result:<18} │")
print(Fore.CYAN + f"│ Result binary      │ {bits(result):<18} │")
print(Fore.YELLOW + "└────────────────────┴────────────────────┘")

print(Fore.CYAN + "\nPOWER OF 2 CHECK")

n = int(input(Fore.WHITE + "\nEnter a number (try 4 or 6): "))

guess = input("Is it a power of 2? (yes/no): ")

is_power = n > 0 and (n & (n - 1)) == 0


print(Fore.YELLOW + "\n┌──────────────────────────────┬────────────────┐")
print(Fore.YELLOW + "│ Property                     │ Value          │")
print(Fore.YELLOW + "├──────────────────────────────┼────────────────┤")
print(Fore.CYAN + f"│ Number                       │ {n:<14} │")
print(Fore.CYAN + f"│ Binary                       │ {bits(n):<14} │")
print(Fore.CYAN + f"│ n - 1                        │ {n - 1:<14} │")
print(Fore.CYAN + f"│ n & (n - 1)                  │ {(n & (n - 1)):<14} │")
print(Fore.CYAN + f"│ Your guess                   │ {guess:<14} │")
print(Fore.CYAN + f"│ Power of 2?                  │ {str(is_power):<14} │")
print(Fore.YELLOW + "└──────────────────────────────┴────────────────┘")

print(Fore.CYAN + "\nWHY DOES THIS WORK?")

print(Fore.YELLOW + "\n┌──────────────────────────────────────────────┐")
print(Fore.YELLOW + "│ A power of 2 has exactly ONE set bit.        │")
print(Fore.YELLOW + "│                                              │")
print(Fore.CYAN + "│ Example:                                     │")
print(Fore.CYAN + "│   4  = 100                                  │")
print(Fore.CYAN + "│   3  = 011                                  │")
print(Fore.CYAN + "│   4 & 3 = 000                               │")
print(Fore.YELLOW + "│                                              │")
print(Fore.YELLOW + "│ Therefore: n & (n - 1) == 0                  │")
print(Fore.YELLOW + "│ means n is a power of 2.                    │")
print(Fore.YELLOW + "└──────────────────────────────────────────────┘")

print(Fore.CYAN + "\nPOWER OF 2 EXAMPLES:")

print(Fore.YELLOW + "\n┌──────────┬──────────────┬──────────────┬──────────────┐")
print(Fore.YELLOW + "│ Number   │ Binary       │ n & (n-1)    │ Power of 2   │")
print(Fore.YELLOW + "├──────────┼──────────────┼──────────────┼──────────────┤")

for x in range(1, 11):
    check = x > 0 and (x & (x - 1)) == 0
    value = x & (x - 1)

    status = "YES" if check else "NO"

    print(
        Fore.CYAN +
        f"│ {x:<8} │ {bits(x):<12} │ {value:<12} │ {status:<12} │"
    )

print(Fore.YELLOW + "└──────────┴──────────────┴──────────────┴──────────────┘")
print(Fore.GREEN + "\n╔══════════════════════════════════════════════╗")
print(Fore.GREEN + "║" + Fore.WHITE + "              QUICK SUMMARY                   " + Fore.GREEN + "║")
print(Fore.GREEN + "╠══════════════════════════════════════════════╣")
print(Fore.CYAN + "║  OR (|)  → turns selected bits ON            ║")
print(Fore.CYAN + "║  AND (&) → turns selected bits OFF           ║")
print(Fore.CYAN + "║  Power of 2 → exactly one bit is ON          ║")
print(Fore.CYAN + "║  n & (n-1) == 0 → Power of 2                 ║")
print(Fore.GREEN + "╚══════════════════════════════════════════════╝")