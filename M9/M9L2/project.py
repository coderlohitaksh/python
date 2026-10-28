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

title("Stack Frame Visualizer")

print(Fore.LIGHTCYAN_EX + "\nThe first part - Tail recursion ")

def tail_sum(n , acc = 0):
    if n == 0 :
        return acc
    return tail_sum(n - 1 , acc + n)

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how Python uses tail recursion with an accumulator, adds each value as n counts down, and shows how the final result is built through repeated recursive calls.....")

print(Fore.LIGHTGREEN_EX + f"\nThe tail recursion of 4 is {tail_sum(4)}, which means 4 + 3 + 2 + 1.")
print(Fore.LIGHTGREEN_EX + f"The tail recursion of 5 is {tail_sum(5)}, which means 5 + 4 + 3 + 2 + 1.")

print(Fore.LIGHTCYAN_EX + "\nThe second part - Linear recursion")

def linear_sum(n , y = 0):
    if n == 0 :
        return y
    return linear_sum(n - 1)

input(
    Fore.LIGHTYELLOW_EX
     + "Press Enter to learn how Python uses linear recursion is the simplest shape: each call makes exactly one recursive call. The call chain is a straight line from the original call down to the base case, and then back up.....")


print(Fore.LIGHTGREEN_EX + f"\nThe linear recursion of 4 is {linear_sum(4)}, which means its going down to the base case 0.")
print(Fore.LIGHTGREEN_EX + f"The linear recursion of 5 is {linear_sum(5)}, which means its going down to the base case 0.")

print(Fore.LIGHTCYAN_EX + "The third part - Head recursion")

def head_sum(n , x = 0):
    
