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


def pause(message="Press Enter to continue..."):
    input(Fore.LIGHTBLUE_EX + "\n" + message)


def reveal(message):
    pause("Let's reveal the answer. Press Enter...")
    print(Fore.LIGHTGREEN_EX + message)


title("Bitwise Operations")

print(Fore.WHITE + "\nLearning Goals:")
print(Fore.LIGHTGREEN_EX + "1. Swap values without a third variable.")
print(Fore.LIGHTGREEN_EX + "2. Use XOR to swap two numbers.")
print(Fore.LIGHTGREEN_EX + "3. Understand left shift multiplication.")
print(Fore.LIGHTGREEN_EX + "4. Detect different signs using XOR.")
print(Fore.LIGHTGREEN_EX + "5. Divide using repeated subtraction.")
print(Fore.LIGHTGREEN_EX + "6. Learn useful mathematical shortcuts.")

pause("Press Enter to begin learning...")

# 1. SWAP WITHOUT A THIRD VARIABLE
section("1. Swap Without a Third Variable")

a = 5
b = 10

print(Fore.LIGHTGREEN_EX + f"\nBefore swapping: a = {a}, b = {b}")

a, b = b, a

print(Fore.LIGHTGREEN_EX + f"After swapping:  a = {a}, b = {b}")
print(Fore.WHITE + "\nPython allows swapping through tuple assignment.")
print(Fore.WHITE + "No temporary variable is needed.")

pause()

# 2. SWAP USING XOR
section("2. Swap Using XOR (^)")

a = 5
b = 10

print(Fore.LIGHTGREEN_EX + f"\nBefore: a = {a}, b = {b}")
print(Fore.LIGHTGREEN_EX + f"a in binary: {bits(a)}")
print(Fore.LIGHTGREEN_EX + f"b in binary: {bits(b)}")

a = a ^ b
b = a ^ b
a = a ^ b

print(Fore.LIGHTGREEN_EX + f"\nAfter XOR swap: a = {a}, b = {b}")
print(Fore.WHITE + "\nXOR swaps values without a third variable.")
print(Fore.WHITE + "Remember: a ^ a = 0 and a ^ 0 = a.")

pause()

# 3. LEFT SHIFT
section("3. Left Shift (<<)")

n = 5

print(Fore.LIGHTGREEN_EX + f"\nBefore: n = {n}")
print(Fore.LIGHTGREEN_EX + f"Binary: {bits(n)}")

result = n << 1

print(Fore.LIGHTGREEN_EX + f"After n << 1: {result}")
print(Fore.LIGHTGREEN_EX + f"Binary: {bits(result)}")
print(Fore.WHITE + "\nFor positive integers, n << 1 equals n * 2.")
print(Fore.WHITE + "Similarly, n << 2 equals n * 4.")

pause()

# 4. XOR TO DETECT DIFFERENT SIGNS
section("4. Detect Different Signs Using XOR")

a = -5
b = 10

print(Fore.LIGHTGREEN_EX + f"\nFirst number: {a}")
print(Fore.LIGHTGREEN_EX + f"Second number: {b}")

different_signs = (a < 0) != (b < 0)

print(
    Fore.LIGHTGREEN_EX
    + f"Do they have different signs? {different_signs}"
)

print(Fore.WHITE + "\nThe clear Python method compares their signs directly.")
print(Fore.WHITE + "A common bitwise shortcut is (a ^ b) < 0.")
print(Fore.WHITE + "This shortcut assumes conventional signed integers.")

pause()

# 5. DIVISION USING REPEATED SUBTRACTION
section("5. Division Using Repeated Subtraction")

dividend = 17
divisor = 5

print(Fore.LIGHTGREEN_EX + f"\nDividend: {dividend}")
print(Fore.LIGHTGREEN_EX + f"Divisor: {divisor}")

if divisor <= 0 or dividend < 0:
    print(Fore.LIGHTRED_EX + "Use a non-negative dividend and positive divisor.")
else:
    remainder = dividend
    quotient = 0

    while remainder >= divisor:
        remainder -= divisor
        quotient += 1
        print(
            Fore.LIGHTGREEN_EX
            + f"Step {quotient}: remainder = {remainder}"
        )

    print(Fore.LIGHTGREEN_EX + f"\nQuotient: {quotient}")
    print(Fore.LIGHTGREEN_EX + f"Remainder: {remainder}")

    print(Fore.WHITE + "\n17 = (5 * 3) + 2")

pause()

# 6. MATHEMATICAL SHORTCUTS
section("6. Useful Mathematical Shortcuts")

n = 8

print(Fore.LIGHTGREEN_EX + f"\nNumber: {n}")
print(Fore.LIGHTGREEN_EX + f"Double: {n << 1}")
print(Fore.LIGHTGREEN_EX + f"Multiply by 4: {n << 2}")
print(Fore.LIGHTGREEN_EX + f"Divide by 2: {n >> 1}")
print(Fore.LIGHTGREEN_EX + f"Check odd: {n & 1}")

print(Fore.WHITE + "\nFor non-negative integers:")
print(Fore.WHITE + "n << 1  is equivalent to n * 2.")
print(Fore.WHITE + "n >> 1  is equivalent to n // 2.")
print(Fore.WHITE + "n & 1   is 1 if odd, otherwise 0.")

pause()

# 7. INTERACTIVE CHALLENGE
section("7. Your Turn!")

a = int(input(Fore.LIGHTRED_EX + "\nEnter the first integer: "))
b = int(input(Fore.LIGHTRED_EX + "Enter the second integer: "))

guess = input(
    Fore.LIGHTRED_EX
    + f"What is {a} << 1? Enter your guess: "
)

result = a << 1

reveal(f"The correct answer is {result}.")

if guess.strip() == str(result):
    print(Fore.LIGHTGREEN_EX + "Correct! Excellent work!")
else:
    print(Fore.LIGHTRED_EX + f"Not quite. Your answer was {guess}.")

guess = input(
    Fore.LIGHTRED_EX
    + f"\nWhat is {a} ^ {b}? Enter your guess: "
)

result = a ^ b

reveal(f"The correct answer is {result}.")

if guess.strip() == str(result):
    print(Fore.LIGHTGREEN_EX + "Correct! Excellent work!")
else:
    print(Fore.LIGHTRED_EX + f"Not quite. Your answer was {guess}.")

print(
    Fore.CYAN
    + Style.BRIGHT
    + "\nGreat job learning bitwise operations!"
)
