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


title("Bit difference")

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how XOR calculates the difference of two numbers using 2's compliment...." ) 

def reveal(text):
    print(Fore.LIGHTYELLOW_EX + text)

print(Fore.LIGHTGREEN_EX + f"\n9 ^ 3 = {9^3} and {9^3}'s binary is {bin(9^3)[2:]} and the bit's different are {bin(9^3).count('1')} bits.")
print(Fore.LIGHTGREEN_EX + f"5 ^ 3 = {5^3} and {5^3}'s binary is {bin(5^3)[2:]} and the bit's different are {bin(5^3).count('1')} bits.")

n = int(input(Fore.LIGHTCYAN_EX + "Enter a number (try 4 or 6): "))
guess = input(Fore.LIGHTCYAN_EX + f"How many bits differ between {n} and 7? ")
input(Fore.LIGHTCYAN_EX + "XOR marks the differing bits - count the 1s.  Press Enter ")
difference = bin(n ^ 7).count('1')
print(Fore.LIGHTCYAN_EX + f"\n{n} ^ 7 gives the binary number {bin(n^7)[2:]} and the bit's different are {difference}.  ")

reveal(Fore.LIGHTCYAN_EX + f"The correct answer is {difference}.")

if guess.strip() == str(difference):
    print(Fore.LIGHTGREEN_EX + "Correct! Excellent work!")
else:
    print(
        Fore.LIGHTRED_EX
        + f"Not quite. The correct count is {difference}."
    )