import os

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def bits(n, width=8):
    return format(n & ((1 << width) - 1), f"0{width}b")

def pause(msg="Press ENTER to continue..."):
    input(f"\n{YELLOW}⏎ {msg}{RESET}")

def title(text):
    print(f"\n{CYAN}{BOLD}{'═' * 60}{RESET}")
    print(f"{MAGENTA}{BOLD}        🌟 {text} 🌟{RESET}")
    print(f"{CYAN}{BOLD}{'═' * 60}{RESET}")

def box(text, color=BLUE):
    print(f"\n{color}{BOLD}┌{'─' * 58}┐")
    for line in text.split("\n"):
        print(f"│ {line:<56} │")
    print(f"└{'─' * 58}┘{RESET}")

def show_bits(label, n):
    print(f"{YELLOW}{label:<12}:{RESET} {GREEN}{bits(n)}{RESET}")

def is_power_of_2(num):
    return num > 0 and (num & (num - 1)) == 0

def power_position(num):
    position = 0
    while num > 1:
        num >>= 1
        position += 1
    return position

def is_power_of_4(num):
    return is_power_of_2(num) and power_position(num) % 2 == 0

def is_power_of_8(num):
    return is_power_of_2(num) and power_position(num) % 3 == 0


clear()
title("POWER OF TWO SCANNER")

box(
    "🔢 Learn how binary bits identify powers of 2, 4 and 8.\n"
    "⚡ Explore the n & (n-1) trick.\n"
    "🚀 Understand binary exponentiation.",
    MAGENTA
)

pause("Press ENTER to start the bitwise adventure...")

title("1. THE n & (n-1) TRICK")

n = 16

print(f"\n{WHITE}Number n:{RESET} {GREEN}{n}{RESET}")
show_bits("Binary", n)

print(f"\n{WHITE}Number n-1:{RESET} {GREEN}{n-1}{RESET}")
show_bits("Binary", n - 1)

result = n & (n - 1)

print(f"\n{CYAN}{BOLD}BITWISE AND:{RESET}")
print(f"{GREEN}{bits(n)}{RESET}")
print(f"{GREEN}{bits(n-1)}{RESET}")
print(f"{CYAN}{'─' * 8}{RESET}")
print(f"{YELLOW}{bits(result)}{RESET}")

box(
    "💡 n & (n-1) removes the RIGHTMOST SET BIT!\n\n"
    "16 = 10000\n"
    "15 = 01111\n"
    "16 & 15 = 00000",
    GREEN
)

pause()

title("2. POWER OF 2")

box(
    "A positive power of 2 contains EXACTLY ONE set bit.\n\n"
    "1  → 00000001\n"
    "2  → 00000010\n"
    "4  → 00000100\n"
    "8  → 00001000\n"
    "16 → 00010000\n"
    "32 → 00100000",
    CYAN
)

print(f"\n{YELLOW}Magic condition:{RESET}")
print(f"{GREEN}n > 0 and (n & (n-1)) == 0{RESET}")

pause("Press ENTER to test a number...")

num = int(input(f"\n{CYAN}🔢 Enter a number: {RESET}"))
show_bits("Number", num)

if is_power_of_2(num):
    print(f"\n{GREEN}{BOLD}✅ YES! {num} is a POWER OF 2!{RESET}")
else:
    print(f"\n{RED}{BOLD}❌ NO! {num} is NOT a power of 2.{RESET}")

pause()

title("3. POWER OF 4")

box(
    "4⁰ = 1       → position 0\n"
    "4¹ = 4       → position 2\n"
    "4² = 16      → position 4\n"
    "4³ = 64      → position 6\n"
    "4⁴ = 256     → position 8\n\n"
    "✨ The set-bit position is ALWAYS EVEN!",
    MAGENTA
)

pause("Press ENTER to test a power of 4...")

num4 = int(input(f"\n{CYAN}🔢 Enter a number: {RESET}"))
show_bits("Binary", num4)

if is_power_of_4(num4):
    print(f"\n{GREEN}{BOLD}✅ {num4} IS A POWER OF 4!{RESET}")
else:
    print(f"\n{RED}{BOLD}❌ {num4} is NOT a power of 4.{RESET}")

pause()

title("4. POWER OF 8")

box(
    "8⁰ = 1       → position 0\n"
    "8¹ = 8       → position 3\n"
    "8² = 64      → position 6\n"
    "8³ = 512     → position 9\n"
    "8⁴ = 4096    → position 12\n\n"
    "✨ Positions: 0, 3, 6, 9, 12...\n"
    "✨ Therefore position % 3 == 0",
    BLUE
)

pause("Press ENTER to test a power of 8...")

num8 = int(input(f"\n{CYAN}🔢 Enter a number: {RESET}"))
show_bits("Binary", num8)

if is_power_of_8(num8):
    print(f"\n{GREEN}{BOLD}✅ {num8} IS A POWER OF 8!{RESET}")
else:
    print(f"\n{RED}{BOLD}❌ {num8} is NOT a power of 8.{RESET}")

pause()

title("5. FIND THE SET-BIT POSITION")

num = int(input(f"\n{CYAN}🔢 Enter a positive power of 2: {RESET}"))

if is_power_of_2(num):
    temp = num
    position = 0

    show_bits("Binary", num)

    while temp > 1:
        print(
            f"{YELLOW}{temp:>5} >> 1 = "
            f"{GREEN}{temp >> 1}{RESET}"
        )
        temp >>= 1
        position += 1

    print(f"\n{MAGENTA}{BOLD}📍 Set-bit position = {position}{RESET}")

    if position % 2 == 0:
        print(f"{GREEN}✔ Even position → POWER OF 4{RESET}")
    else:
        print(f"{RED}✘ Odd position → NOT power of 4{RESET}")

    if position % 3 == 0:
        print(f"{GREEN}✔ Divisible by 3 → POWER OF 8{RESET}")
    else:
        print(f"{RED}✘ Not divisible by 3 → NOT power of 8{RESET}")
else:
    print(f"{RED}❌ Please enter a POWER OF 2.{RESET}")

pause()

title("6. BINARY EXPONENTIATION")

box(
    "Binary exponentiation uses the BITS of the exponent.\n\n"
    "Example: 2¹³\n"
    "13 = 1101₂\n"
    "13 = 8 + 4 + 1\n\n"
    "2¹³ = 2⁸ × 2⁴ × 2¹\n"
    "     = 256 × 16 × 2\n"
    "     = 8192",
    YELLOW
)

pause("Press ENTER to perform binary exponentiation...")

base = int(input(f"\n{CYAN}🔢 Enter base: {RESET}"))
exponent = int(input(f"{CYAN}🔢 Enter exponent: {RESET}"))

print(f"\n{WHITE}Base     : {GREEN}{base}{RESET}")
print(f"{WHITE}Exponent : {GREEN}{exponent}{RESET}")
show_bits("Binary", exponent)

guess = input(
    f"\n{YELLOW}🤔 What is {base}^{exponent}? {RESET}"
).strip()

pause("Press ENTER to calculate step by step...")

answer = 1
current_base = base
n = exponent
step = 1

while n > 0:
    print(f"\n{MAGENTA}{BOLD}━━ STEP {step} ━━{RESET}")
    print(f"Exponent = {GREEN}{n}{RESET}")
    print(f"Binary   = {GREEN}{bits(n)}{RESET}")

    if n & 1:
        print(f"{GREEN}🟢 Rightmost bit = 1 → MULTIPLY{RESET}")
        answer *= current_base
    else:
        print(f"{YELLOW}🟡 Rightmost bit = 0 → SKIP{RESET}")

    print(f"Answer = {CYAN}{answer}{RESET}")

    current_base *= current_base
    print(f"Base²  = {BLUE}{current_base}{RESET}")

    n >>= 1
    print(f"Exp >> 1 = {BLUE}{n}{RESET}")

    step += 1

title("7. FINAL ANSWER")

print(
    f"\n{CYAN}{BOLD}{base}^{exponent} = "
    f"{GREEN}{answer}{RESET}"
)

print(f"{WHITE}Your guess : {guess}{RESET}")

if guess == str(answer):
    print(f"\n{GREEN}{BOLD}🎉 CORRECT! Excellent work! 🎉{RESET}")
else:
    print(
        f"\n{RED}{BOLD}❌ INCORRECT{RESET}"
        f"\n{YELLOW}Correct answer = {answer}{RESET}"
    )

pause()

title("8. IMPORTANT BITWISE OPERATIONS")

box(
    "n & 1\n"
    "→ Checks the RIGHTMOST bit.\n"
    "→ 1 = ODD\n"
    "→ 0 = EVEN\n\n"
    "n & (n-1)\n"
    "→ Removes the RIGHTMOST SET BIT.\n\n"
    "n > 0 AND n & (n-1) == 0\n"
    "→ POWER OF 2",
    CYAN
)

title("🌟 FINAL SUMMARY 🌟")

print(f"""
{GREEN}{BOLD}POWER OF 2{RESET}
  • Exactly ONE bit is set.
  • n & (n-1) == 0

{MAGENTA}{BOLD}POWER OF 4{RESET}
  • Exactly ONE bit is set.
  • Set-bit position is EVEN.

{BLUE}{BOLD}POWER OF 8{RESET}
  • Exactly ONE bit is set.
  • Set-bit position is divisible by 3.

{YELLOW}{BOLD}BINARY EXPONENTIATION{RESET}
  • Uses the bits of the exponent.
  • Squares the base repeatedly.
  • Divides the exponent by 2 repeatedly.
  • Time Complexity: O(log n)
""")

box(
    "🧠 ONE BIT → POWER OF 2\n"
    "✨ EVEN POSITION → POWER OF 4\n"
    "🚀 POSITION % 3 == 0 → POWER OF 8\n\n"
    "Keep experimenting with binary!",
    GREEN
)

print(f"\n{CYAN}{BOLD}{'═' * 60}{RESET}")
print(f"{MAGENTA}{BOLD}       🌈 POWER OF TWO SCANNER 🌈{RESET}")
print(f"{CYAN}{BOLD}              END OF PROGRAM{RESET}")
print(f"{CYAN}{BOLD}{'═' * 60}{RESET}\n")