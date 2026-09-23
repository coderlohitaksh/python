from colorama import Fore, Style, init

init(autoreset=True)


def bits(n, width=16):
    return format(n & ((1 << width) - 1), f"0{width}b")


def pause(message):
    input(Fore.YELLOW + f"\n{message}")


print(Fore.CYAN + Style.BRIGHT + "\nBINARY EXPONENTIATION")
print("Learn how binary numbers make powers faster!")

pause("Press Enter to learn how exponents are written in binary...")

print(Fore.MAGENTA + "\n1. EXPONENT IN BINARY")

print(Fore.CYAN + f"\n8 in binary : {bits(8)}")
print(Fore.CYAN + f"5 in binary : {bits(5)}")
print(Fore.CYAN + f"3 in binary : {bits(3)}")
print(Fore.CYAN + f"6 in binary : {bits(6)}")

print("\nExamples:")
print("8 = 1000")
print("5 = 0101")
print("3 = 0011")
print("6 = 0110")

pause("Press Enter to see repeated squaring...")

print(Fore.MAGENTA + "\n2. REPEATED SQUARING")

print("\nTo calculate 2^8, we can repeatedly square the base.")

print(Fore.GREEN + "\n2^1 = 2")
print("2^2 = 4")
print("2^4 = 16")
print("2^8 = 256")

print("\nInstead of multiplying 2 eight times,")
print("we keep squaring the previous result.")

pause("Press Enter to see how the bits are used...")

print(Fore.MAGENTA + "\n3. USING THE BITS")

print("\nSuppose exponent = 13")

print(Fore.CYAN + "\n13 in binary = 1101")

print("\n13 = 8 + 4 + 1")

print("\nTherefore:")
print("2^13 = 2^8 × 2^4 × 2^1")
print("     = 256 × 16 × 2")
print("     = 8192")

print(Fore.YELLOW + "\nA bit equal to 1 means:")
print("Multiply the current result by the current base.")

pause("Press Enter to see the algorithm...")

print(Fore.MAGENTA + "\n4. BINARY EXPONENTIATION")

exp = int(input(Fore.GREEN + "\nEnter exponent (try 3, 5 or 6): "))

print(Fore.CYAN + f"\nExponent : {exp}")
print(Fore.CYAN + f"Binary   : {bits(exp)}")

guess = input(
    Fore.GREEN + f"\nWhat is 2^{exp}? "
).strip()

pause("Press Enter to calculate...")

result = 1
base = 2
n = exp
step = 1

while n > 0:

    print(Fore.YELLOW + f"\nStep {step}")
    print(f"Exponent : {n}")
    print(f"Binary   : {bits(n)}")

    if n & 1:
        print(Fore.GREEN + "Rightmost bit = 1")
        print("Multiply result by base.")
        result *= base
    else:
        print(Fore.RED + "Rightmost bit = 0")
        print("Skip multiplication.")

    print(f"Result   : {result}")

    base *= base
    n //= 2

    print(f"New base: {base}")

    step += 1

print(Fore.MAGENTA + "\n5. FINAL ANSWER")

print(Fore.CYAN + f"\n2^{exp} = {result}")
print(f"Your guess = {guess}")

if guess == str(result):
    print(Fore.GREEN + "\nYour guess is correct!")
else:
    print(Fore.RED + "\nYour guess is incorrect.")
    print(Fore.GREEN + f"Correct answer = {result}")

print(Fore.MAGENTA + "\n6. IMPORTANT BITWISE OPERATION")

print(Fore.YELLOW + "\nn & 1")

print("Checks the rightmost bit of n.")

print("\nIf n & 1 == 1 → n is ODD")
print("If n & 1 == 0 → n is EVEN")

print(Fore.MAGENTA + "\n7. WHY IS IT FAST?")

print("\nBinary exponentiation repeatedly:")
print("1. Checks the rightmost bit.")
print("2. Multiplies when the bit is 1.")
print("3. Squares the base.")
print("4. Divides the exponent by 2.")

print(Fore.YELLOW + "\nTime Complexity: O(log n).")

print(Fore.GREEN + "\n=> BINARY EXPONENTIATION")