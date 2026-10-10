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


title("Shift Operations")

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how left shift multiplies a number "
      "and right shift divides a number by 2..."
)

# LEFT SHIFT
section("Left Shift (<<)")

n = 5
print(Fore.LIGHTGREEN_EX + f"\nBefore: n = {n}")
print(Fore.LIGHTGREEN_EX + f"Binary: {bits(n)}")

result = n << 1

print(Fore.LIGHTGREEN_EX + f"After n << 1: {result}")
print(Fore.LIGHTGREEN_EX + f"Binary: {bits(result)}")

input(
    Fore.LIGHTBLUE_EX
    + "\nLeft shift by 1 multiplies a positive integer by 2. Press Enter..."
)

# RIGHT SHIFT
section("Right Shift (>>)")

n = 10
print(Fore.LIGHTGREEN_EX + f"\nBefore: n = {n}")
print(Fore.LIGHTGREEN_EX + f"Binary: {bits(n)}")

result = n >> 1

print(Fore.LIGHTGREEN_EX + f"After n >> 1: {result}")
print(Fore.LIGHTGREEN_EX + f"Binary: {bits(result)}")

input(
    Fore.LIGHTBLUE_EX
    + "\nRight shift by 1 divides an integer by 2, rounding down "
      "for non-negative integers. Press Enter..."
)

# INTERACTIVE CHALLENGE
section("Your Turn!")

n = int(
    input(
        Fore.LIGHTRED_EX
        + "\nEnter a number (try 3 or 7): "
    )
)

guess = input(
    Fore.LIGHTRED_EX
    + f"What will {n} << 1 become? Enter your guess: "
)

result = n << 1

input(
    Fore.LIGHTBLUE_EX
    + "\nLet's reveal the answer. Press Enter..."
)

if guess.strip() == str(result):
    print(Fore.LIGHTGREEN_EX + "Correct! Excellent work!")
else:
    print(Fore.LIGHTRED_EX + "Not quite. Keep practising!")

print(
    Fore.LIGHTGREEN_EX
    + f"\nThe answer is {result}. "
    + f"Your guess was {guess}."
)

# RIGHT SHIFT CHALLENGE
n = int(
    input(
        Fore.LIGHTRED_EX
        + "\nEnter another number (try 8 or 15): "
    )
)

guess = input(
    Fore.LIGHTRED_EX
    + f"What will {n} >> 1 become? Enter your guess: "
)

result = n >> 1

input(
    Fore.LIGHTBLUE_EX
    + "\nLet's reveal the answer. Press Enter..."
)

if guess.strip() == str(result):
    print(Fore.LIGHTGREEN_EX + "Correct! Excellent work!")
else:
    print(Fore.LIGHTRED_EX + "Not quite. Keep practising!")

print(
    Fore.LIGHTGREEN_EX
    + f"\nThe answer is {result}. "
    + f"Your guess was {guess}."
)

print(Fore.CYAN + Style.BRIGHT + "\nGreat job learning shift operations!")
