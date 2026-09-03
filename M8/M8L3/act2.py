from colorama import Fore, Style, init

init(autoreset=True)


print(Fore.CYAN + "\n╔══════════════════════════════════════════════╗")

print(Fore.CYAN + "║" + Fore.GREEN + "           ONE ODD-OCCURRING NUMBER           " + Fore.CYAN + "║")

print(Fore.CYAN + "╚══════════════════════════════════════════════╝")


input(
    Fore.LIGHTGREEN_EX
    + "\nXOR cancels numbers that occur in pairs. "
      "Press Enter to proceed."
)

print(
    Fore.LIGHTGREEN_EX
    + "For example: 2 ^ 3 ^ 4 ^ 3 ^ 2 = ",
    2 ^ 3 ^ 4 ^ 3 ^ 2
)

input(
    Fore.LIGHTRED_EX
    + "\nThe 2s cancel each other and the 3s cancel each other. "
      "The number occurring once survives. Press Enter to proceed."
)

print(
    Fore.LIGHTRED_EX
    + "2 ^ 3 ^ 4 ^ 3 ^ 2 = ",
    2 ^ 3 ^ 4 ^ 3 ^ 2
)


n = int(input(Fore.LIGHTBLUE_EX + "\nEnter a number (Try 7 or 11): "))

nums = [3, n, 5, 3, 5]

guess = input(
    Fore.LIGHTBLUE_EX
    + f"Which number in {nums} appears only once? "
)


result = 0

for x in nums:
    result ^= x


input(
    Fore.LIGHTBLUE_EX
    + "\nXOR cancels the repeated pairs, "
      "so the odd-occurring number survives. "
      "Press Enter to proceed."
)


print(
    Fore.LIGHTBLUE_EX
    + f"\n{nums} → odd-occurring number = ",
    result,
    " your guess is ",
    guess
)