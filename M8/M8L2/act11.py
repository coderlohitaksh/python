from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + "\n╔══════════════════════════════════════════════╗")
print(Fore.CYAN + "║" + Fore.GREEN + "              SET & POWER BITS                " + Fore.CYAN + "║")
print(Fore.CYAN + "╚══════════════════════════════════════════════╝")


print(Fore.CYAN + "\nBitwise OR - Set a Bit")  

print(Fore.YELLOW + "\n┌──────────────────────────────┬──────────────┐")
print(Fore.YELLOW + "│ Operation                    │ Result       │")
print(Fore.YELLOW + "├──────────────────────────────┼──────────────┤")

print(Fore.CYAN + f"│ 5                            │ {bin(5)[2:]:<12} │")
print(Fore.CYAN + f"│ 5 | 2                        │ {5 | 2:<12} │")
print(Fore.CYAN + f"│ Binary result                │ {bin(5 | 2)[2:]:<12} │")

print(Fore.YELLOW + "└──────────────────────────────┴──────────────┘")


print(Fore.CYAN + "\nBitwise AND - Zero a Bit")

print(Fore.YELLOW + "\n┌──────────────────────────────┬──────────────┐")
print(Fore.YELLOW + "│ Operation                    │ Result       │")
print(Fore.YELLOW + "├──────────────────────────────┼──────────────┤")

print(Fore.CYAN + f"│ 7                            │ {bin(7)[2:]:<12} │")
print(Fore.CYAN + f"│ 7 & 5                        │ {7 & 5:<12} │")
print(Fore.CYAN + f"│ Binary result                │ {bin(7 & 5)[2:]:<12} │")

print(Fore.YELLOW + "└──────────────────────────────┴──────────────┘")


print(Fore.CYAN + "\nPower of 2 Check")

n = int(input("Enter a number (try 4 or 6): "))
guess = input("Is it a power of 2? (yes/no): ")

is_power = n > 0 and (n & (n - 1)) == 0

print(Fore.YELLOW + "\n┌──────────────────────────────┬────────────────────┐")
print(Fore.YELLOW + "│ Property                     │ Value              │")
print(Fore.YELLOW + "├──────────────────────────────┼────────────────────┤")

print(Fore.CYAN + f"│ Number                       │ {n:<18} │")
print(Fore.CYAN + f"│ Binary                       │ {bin(n)[2:]:<18} │")
print(Fore.CYAN + f"│ Your guess                   │ {guess:<18} │")

if is_power:
    print(Fore.GREEN + f"│ Result                       │ {'POWER OF 2':<18} │")
else:
    print(Fore.RED + f"│ Result                       │ {'NOT POWER OF 2':<18} │")

print(Fore.YELLOW + "└──────────────────────────────┴────────────────────┘")


print(Fore.CYAN + "\nPower of 2 Explanation")

print(Fore.YELLOW + "\n┌──────────────────────────────┬────────────────────┐")
print(Fore.YELLOW + "│ Expression                   │ Value              │")
print(Fore.YELLOW + "├──────────────────────────────┼────────────────────┤")

print(Fore.CYAN + f"│ n                            │ {n:<18} │")
print(Fore.CYAN + f"│ n - 1                        │ {n - 1:<18} │")
print(Fore.CYAN + f"│ n & (n - 1)                  │ {n & (n - 1):<18} │")

if is_power:
    print(Fore.GREEN + "│ Conclusion                   │ Only one bit is ON │")
else:
    print(Fore.RED + "│ Conclusion                   │ More than one bit  │")

print(Fore.YELLOW + "└──────────────────────────────┴────────────────────┘")