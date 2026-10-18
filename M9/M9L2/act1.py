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

def tail_sum(n , acc = 0):
    if n == 0 :
        return acc
    return tail_sum(n - 1 , acc + n)

title("Tail Recursion")

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how Python uses tail recursion with an accumulator, adds each value as n counts down, and shows how the final result is built through repeated recursive calls.....")

print(Fore.LIGHTGREEN_EX + f"\nThe tail recursion of 4 is {tail_sum(4)}, which means 4 + 3 + 2 + 1.")
print(Fore.LIGHTGREEN_EX + f"The tail recursion of 5 is {tail_sum(5)}, which means 5 + 4 + 3 + 2 + 1.")

n = int(input(Fore.LIGHTCYAN_EX + "\nEnter a number you like : "))
guess = input(Fore.LIGHTCYAN_EX + f"What do you think will be te tail recursion of {n} ?: ")

input(Fore.LIGHTYELLOW_EX + "\nTail sum adds the number to accumulator at ecah step, accumulator is the number that builds when the inputed number is counted down. Press Enter to proceed.")
print(Fore.LIGHTCYAN_EX + f"\nThe tail sum of {n} is {tail_sum(n)} , your guess is {guess}.")
