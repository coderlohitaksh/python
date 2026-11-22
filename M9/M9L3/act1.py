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

title("The Head and Tail pattern")

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how Python introduces the head-tail pattern in lists, showing how the first    element becomes the head, the remaining elements become the tail, and an empty list acts as the base case......")

input(Fore.LIGHTYELLOW_EX + "\nThe head of a list is the starting thing in the list , in code we write lst[0] . Similary the rest part of the list is tail , we write     lst[1:] and the base case in code we write [].Press Enter to proceed")
print(Fore.LIGHTCYAN_EX + f"\nIn the list [1 , 4 , 9 , 16], the head is {[1 , 4 , 9 , 16][:0]} and the tail is {[1 , 4 , 9 , 16][1:]}.")
print(Fore.LIGHTCYAN_EX + f"In the list [1 , 8 , 27 , 64], the head is {[1 , 8 , 27 , 64][:0]} and the tail is {[1 , 8 , 27 , 64][1:]}.")

lst = [int(x) for x in input(Fore.LIGHTGREEN_EX + ("\nEnter numbers in any order you like (put atleast 2 numbers) : ")).split()]
guess = int(input(Fore.LIGHTGREEN_EX + f"What do you think will be the head of the list{lst}?: "))
print(Fore.LIGHTGREEN_EX + f"\nThe head of the list is {[lst[0]]} , your answer is {guess}.")
