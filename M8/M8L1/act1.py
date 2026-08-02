from colorama import Fore, Style, init

init(autoreset=True)

a = int(input(Fore.YELLOW + ("\nEnter a first posititve number : ")))
b = int(input(Fore.CYAN + ("Enter a second positive number : ")))

def bits(n, width=8):
    return format(n & ((1 << width) - 1), f"0{width}b")


def title(text):
    print(Fore.CYAN + Style.BRIGHT + "╔" + "═" * 50 + "╗")
    print(Fore.CYAN + Style.BRIGHT + f"║{text.center(50)}║")
    print(Fore.CYAN + Style.BRIGHT + "╚" + "═" * 50 + "╝")


def section(text):
    print("\n" + Fore.YELLOW + Style.BRIGHT + f"▶ {text}")
    print(Fore.YELLOW + "─" * 52)


title("BIT EXPLORER")

section("Bits & Binary")

print(Fore.GREEN + f"a = {a:<3}" + Fore.WHITE + f"  Binary : {bits(a)}")
print(Fore.GREEN + f"b = {b:<3}" + Fore.WHITE + f"  Binary : {bits(b)}")

section("AND (&) and OR (|)")

print(Fore.MAGENTA + f"a & b = {a & b:<3}" +
      Fore.WHITE + f"  Binary : {bits(a & b)}")

print(Fore.BLUE + f"a | b = {a | b:<3}" +
      Fore.WHITE + f"  Binary : {bits(a | b)}")

section("NOT (~) and XOR (^)")

print(Fore.RED + f"~a    = {~a & 0xFF:<3}" +
      Fore.WHITE + f"  Binary : {bits(~a)}")

print(Fore.LIGHTMAGENTA_EX + f"a ^ b = {a ^ b:<3}" +
      Fore.WHITE + f"  Binary : {bits(a ^ b)}")

section("Left Shift (<<) and Right Shift (>>)")

print(Fore.GREEN + f"a << 1 = {a << 1:<3}" +
      Fore.WHITE + "  Multiply by 2")

print(Fore.GREEN + f"a >> 1 = {a >> 1:<3}" +
      Fore.WHITE + "  Divide by 2")

section("Odd or Even")

for n in [7, 10, 15, 4]:
    result = "Even" if n ^ 1 == n + 1 else "Odd"
    color = Fore.GREEN if result == "Even" else Fore.RED
    print(Fore.CYAN + f"{n:<3}" + Fore.WHITE + " → " + color + result)

section("Count Bits")


def count_bits(n):
    count = 0
    while n:
        count += 1
        n >>= 1
    return count


for n in [a, b, 255]:
    c = count_bits(n)
    print(
        Fore.YELLOW + f"{n:<3}" +
        Fore.WHITE + f" → {c} bits " +
        Fore.CYAN + f"({bits(n, c)})"
    )

print("\n" + Fore.GREEN + Style.BRIGHT + "✔ Program Finished Successfully!")