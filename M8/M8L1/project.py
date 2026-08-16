from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + "\n╔══════════════════════════════════════╗")
print(Fore.CYAN + "║" + Fore.GREEN + "      MY SECRET CODE BIT SCANNER      " + Fore.CYAN + "║")
print(Fore.CYAN + "╚══════════════════════════════════════╝")

print(Fore.YELLOW + "\n🔐 Enter your secret information")

secret = int(input(Fore.WHITE + "Secret Code : "))
key = int(input(Fore.WHITE + "Access Key  : "))

print(Fore.CYAN + "\n🔎 SCANNING YOUR CODE...")
print(Fore.CYAN + "──────────────────────────────────────")

print(Fore.GREEN + "Secret Code  : " + Fore.WHITE + format(secret, "08b"))
print(Fore.GREEN + "Access Key   : " + Fore.WHITE + format(key, "08b"))

print(Fore.CYAN + "\n⚡ BIT OPERATIONS")
print(Fore.CYAN + "──────────────────────────────────────")

print(Fore.WHITE + "AND  → " + Fore.YELLOW + format(secret & key, "08b"))
print(Fore.WHITE + "OR   → " + Fore.YELLOW + format(secret | key, "08b"))
print(Fore.WHITE + "XOR  → " + Fore.YELLOW + format(secret ^ key, "08b"))

print(Fore.CYAN + "\n🔄 BIT FLIP")
print(Fore.CYAN + "──────────────────────────────────────")

flipped = ~secret
print(Fore.WHITE + "Flipped Code → " + Fore.YELLOW + str(flipped))

print(Fore.CYAN + "\n↔ BIT SHIFT")
print(Fore.CYAN + "──────────────────────────────────────")

print(Fore.WHITE + "Left Shift  → " + Fore.YELLOW + str(secret << 1))
print(Fore.WHITE + "Right Shift → " + Fore.YELLOW + str(secret >> 1))

print(Fore.CYAN + "\n🔢 BIT COUNTER")
print(Fore.CYAN + "──────────────────────────────────────")

print(Fore.WHITE + "Number of 1-bits → " + Fore.YELLOW + str(secret.bit_count()))

print(Fore.CYAN + "\n🔐 ACCESS CHECK")
print(Fore.CYAN + "──────────────────────────────────────")

if secret == key:
    print(Fore.GREEN + "✓ ACCESS GRANTED!")
    print(Fore.GREEN + "✓ Secret code matches the access key.")
else:
    print(Fore.RED + "✗ ACCESS DENIED!")
    print(Fore.RED + "✗ Secret code does not match the access key.")

print(Fore.CYAN + "\n╔══════════════════════════════════════╗")
print(Fore.CYAN + "║" + Fore.GREEN + "          SCAN COMPLETE ✓             " + Fore.CYAN + "║")
print(Fore.CYAN + "╚══════════════════════════════════════╝")