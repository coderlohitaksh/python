from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + "\n╔══════════════════════════════════════════════╗")
print(Fore.CYAN + "║" + Fore.GREEN + "          MY SMART SWITCH BIT MONITOR         " + Fore.CYAN + "║")
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

print(Fore.CYAN + "\nBit mask (1 << i):")

print(Fore.YELLOW + "\n┌──────────┬──────────┬──────────────┐")
print(Fore.YELLOW + "│ i        │ 1 << i   │ Binary       │")
print(Fore.YELLOW + "├──────────┼──────────┼──────────────┤")

for i in range(6):
    mask = 1 << i
    print(Fore.CYAN + f"│ {i:<8} │ {mask:<8} │ {bits(mask):<12} │")

print(Fore.YELLOW + "└──────────┴──────────┴──────────────┘")

print(Fore.CYAN + "\nIndividual Bit Values:")

print(Fore.YELLOW + "\n┌──────────┬──────────────┬──────────────┐")
print(Fore.YELLOW + "│ Bit      │ Mask         │ Status       │")
print(Fore.YELLOW + "├──────────┼──────────────┼──────────────┤")

for bit in range(1, 7):
    mask = 1 << (bit - 1)
    result = "SET" if n & mask else "NOT SET"
    print(Fore.CYAN + f"│ {bit:<8} │ {mask:<12} │ {result:<12} │")

print(Fore.YELLOW + "└──────────┴──────────────┴──────────────┘")

print(Fore.CYAN + "\nSmart Home Switch Status:")

print(Fore.YELLOW + "\n┌────────────┬──────────────┬──────────────┐")
print(Fore.YELLOW + "│ Switch     │ Mask         │ Status       │")
print(Fore.YELLOW + "├────────────┼──────────────┼──────────────┤")

for switch in range(1, 7):
    mask = 1 << (switch - 1)
    status = "ON" if n & mask else "OFF"
    print(Fore.CYAN + f"│ Switch {switch:<4} │ {mask:<12} │ {status:<12} │")

print(Fore.YELLOW + "└────────────┴──────────────┴──────────────┘")

print(Fore.CYAN + "\nBitwise Switch Checks:")

print(Fore.YELLOW + "\n┌──────────┬──────────────┬──────────────┐")
print(Fore.YELLOW + "│ Bit      │ Mask         │ Check Result │")
print(Fore.YELLOW + "├──────────┼──────────────┼──────────────┤")

for bit in range(1, 7):
    mask = 1 << (bit - 1)
    result = n & mask
    print(Fore.CYAN + f"│ {bit:<8} │ {mask:<12} │ {result:<12} │")

print(Fore.YELLOW + "└──────────┴──────────────┴──────────────┘")

print(Fore.CYAN + "\n╔══════════════════════════════════════════════╗")
print(Fore.CYAN + "║" + Fore.GREEN + "              MONITOR COMPLETE                " + Fore.CYAN + "║")
print(Fore.CYAN + "╚══════════════════════════════════════════════╝")

print(Fore.GREEN + f"\nNumber       : {n}")
print(Fore.GREEN + f"Binary       : {bits(n)}")
print(Fore.GREEN + f"Set bits     : {count}")
print(Fore.GREEN + f"Zero bits    : {bits(n).count('0')}")