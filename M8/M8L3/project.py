from colorama import Fore, Style, init

init(autoreset=True)


print(Fore.CYAN + "\n╔════════════════════════════════════════════════════╗")
print(Fore.CYAN + "║" + Fore.GREEN + "           BINARY CLUE INVESTIGATOR              " + Fore.CYAN + "║")
print(Fore.CYAN + "╚════════════════════════════════════════════════════╝")


input(
    Fore.LIGHTGREEN_EX +
    "\nXOR with 0 keeps the number unchanged. Press Enter to proceed."
)

print(Fore.LIGHTGREEN_EX + "\nFor example:")
print(Fore.LIGHTGREEN_EX + "7 ^ 0 =", 7 ^ 0)
print(Fore.LIGHTGREEN_EX + "12 ^ 0 =", 12 ^ 0)


input(
    Fore.LIGHTRED_EX +
    "\nXOR a number with itself gives 0. Press Enter to proceed."
)

print(Fore.LIGHTRED_EX + "\nFor example:")
print(Fore.LIGHTRED_EX + "7 ^ 7 =", 7 ^ 7)
print(Fore.LIGHTRED_EX + "12 ^ 12 =", 12 ^ 12)


input(
    Fore.LIGHTBLUE_EX +
    "\nIf two numbers are equal, their XOR is 0. Press Enter to proceed."
)

a = int(input(Fore.LIGHTBLUE_EX + "\nEnter the first number: "))
b = int(input(Fore.LIGHTBLUE_EX + "Enter the second number: "))

print(Fore.LIGHTBLUE_EX + f"\n{a} ^ {b} =", a ^ b)

if (a ^ b) == 0:
    print(Fore.LIGHTGREEN_EX + "Both numbers are equal.")
else:
    print(Fore.LIGHTRED_EX + "Both numbers are different.")


input(
    Fore.LIGHTYELLOW_EX +
    "\nRepeated numbers cancel each other in XOR. Press Enter to proceed."
)

clues = [3, 5, 3, 5, 9]

print(Fore.LIGHTYELLOW_EX + "\nClues:", clues)

xor_result = 0

for clue in clues:
    xor_result = xor_result ^ clue
    print(
        Fore.LIGHTYELLOW_EX +
        f"After XOR with {clue}, result = {xor_result}"
    )

print(Fore.LIGHTGREEN_EX + "\nFinal XOR result:", xor_result)

print(
    Fore.LIGHTGREEN_EX +
    "The repeated 3 and 5 cancelled each other."
)

print(
    Fore.LIGHTGREEN_EX +
    "So the remaining clue is:",
    xor_result
)


input(
    Fore.LIGHTMAGENTA_EX +
    "\nNow let's find one number that occurs an odd number of times."
    "\nPress Enter to proceed."
)

numbers = [4, 7, 4, 2, 7, 2, 9]

print(Fore.LIGHTMAGENTA_EX + "\nNumbers:", numbers)

odd_number = 0

for number in numbers:
    odd_number = odd_number ^ number

print(
    Fore.LIGHTGREEN_EX +
    "\nAll repeated pairs cancel."
)

print(
    Fore.LIGHTGREEN_EX +
    "The number occurring an odd number of times is:",
    odd_number
)


input(
    Fore.LIGHTCYAN_EX +
    "\nNow there are TWO numbers occurring an odd number of times."
    "\nPress Enter to proceed."
)

pair_numbers = [3, 9, 3, 5, 5, 7]

print(Fore.LIGHTCYAN_EX + "\nNumbers:", pair_numbers)

xor_of_two = 0

for number in pair_numbers:
    xor_of_two = xor_of_two ^ number

print(
    Fore.LIGHTGREEN_EX +
    "\nFinal XOR result:",
    xor_of_two
)

print(
    Fore.LIGHTGREEN_EX +
    "This result is the XOR of the two odd-occurring numbers."
)

print(
    Fore.LIGHTYELLOW_EX +
    "\nBut we still don't know the two numbers separately."
)


input(
    Fore.LIGHTBLUE_EX +
    "\nWe can separate the two numbers using the rightmost set bit."
    "\nPress Enter to proceed."
)

rightmost_set_bit = xor_of_two & -xor_of_two

print(
    Fore.LIGHTBLUE_EX +
    "\nXOR of the two odd numbers =",
    xor_of_two
)

print(
    Fore.LIGHTBLUE_EX +
    "Rightmost set bit =",
    rightmost_set_bit
)

print(
    Fore.LIGHTYELLOW_EX +
    "\nThis bit is different in the two odd-occurring numbers."
)


input(
    Fore.LIGHTBLUE_EX +
    "\nNow we split the numbers into two groups."
    "\nPress Enter to proceed."
)

first_odd = 0
second_odd = 0

for number in pair_numbers:

    if number & rightmost_set_bit:
        first_odd = first_odd ^ number

    else:
        second_odd = second_odd ^ number


print(
    Fore.LIGHTGREEN_EX +
    "\nFirst odd-occurring number:",
    first_odd
)

print(
    Fore.LIGHTGREEN_EX +
    "Second odd-occurring number:",
    second_odd
)


input(
    Fore.CYAN +
    "\nPress Enter to see the complete investigation summary."
)

print(Fore.CYAN + "\n╔════════════════════════════════════════════════════╗")
print(Fore.CYAN + "║" + Fore.GREEN + "        BINARY CLUE INVESTIGATION SUMMARY       " + Fore.CYAN + "║")
print(Fore.CYAN + "╚════════════════════════════════════════════════════╝")

print(Fore.LIGHTGREEN_EX + "\n1. XOR Identity")
print(Fore.WHITE + "   a ^ a = 0")

print(Fore.LIGHTGREEN_EX + "\n2. XOR with Zero")
print(Fore.WHITE + "   a ^ 0 = a")

print(Fore.LIGHTGREEN_EX + "\n3. XOR Cancellation")
print(Fore.WHITE + "   Repeated pairs cancel each other.")

print(Fore.LIGHTGREEN_EX + "\n4. One Odd-Occurring Number")
print(
    Fore.WHITE +
    "   Odd-occurring number =",
    odd_number
)

print(Fore.LIGHTGREEN_EX + "\n5. Two Odd-Occurring Numbers")
print(
    Fore.WHITE +
    "   Odd-occurring numbers =",
    first_odd,
    "and",
    second_odd
)

print(Fore.CYAN + "\n════════════════════════════════════════════════════")
print(Fore.GREEN + "              INVESTIGATION COMPLETE!")
print(Fore.CYAN + "════════════════════════════════════════════════════")
