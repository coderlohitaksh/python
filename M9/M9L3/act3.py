from colorama import Fore, Style, init

init(autoreset=True)

def bits(n, width=8):
    return format(n & ((1 << width) - 1), f"0{width}b")


def title(text):
    print(Fore.CYAN + Style.BRIGHT + "╔" + "═" * 50 + "╗")
    print(Fore.CYAN + Style.BRIGHT + f"║{text.center(50)}║")
    print(Fore.CYAN + Style.BRIGHT + "╚" + "═" * 50 + "╝")

def list_max(lst):
    if len(lst) == 1:
        return lst[0]
    rest = list_max(lst[1:])
    return lst[0] if lst[0] > rest else rest

def section(text):
    print("\n" + Fore.YELLOW + Style.BRIGHT + f"▶ {text}")
    print(Fore.YELLOW + "─" * 52)

title("List Max")

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how Python finds the largest value in a list using recursion by comparing the head with the maximum value found in the tail......")

print(Fore.LIGHTCYAN_EX + f"\nIn the list [9 , 1 , 4 , 16 , 36 , 25] , if we apply list max , it becomes the number {list_max([9 , 1 , 4 , 16 , 36 , 25])}.")
print(Fore.LIGHTCYAN_EX + f"In the list [1 , 27 , 8 , 125 , 216 , 64] , if we apply list max , it becomes the number {list_max([1 , 27 , 8 , 125 , 216 , 64])}.")

n = int(input(Fore.LIGHTGREEN_EX + "\nEnter any number you want: "))
lst = [n , 27 , 64 , 125 , 216 , 343]
guess = int(input(Fore.LIGHTGREEN_EX + f"What do you think will be the greatest number in {lst}?: "))
print(Fore.LIGHTCYAN_EX + f"\nThe Largest number is {list_max(lst)}. Your guess is {guess}.")
