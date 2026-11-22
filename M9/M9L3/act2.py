from colorama import Fore, Style, init

init(autoreset=True)

def bits(n, width=8):
    return format(n & ((1 << width) - 1), f"0{width}b")


def title(text):
    print(Fore.CYAN + Style.BRIGHT + "╔" + "═" * 50 + "╗")
    print(Fore.CYAN + Style.BRIGHT + f"║{text.center(50)}║")
    print(Fore.CYAN + Style.BRIGHT + "╚" + "═" * 50 + "╝")

def list_sum(lst) :
    if lst == []:
        return 0
    return lst[0] + list_sum(lst[1:])

def section(text):
    print("\n" + Fore.YELLOW + Style.BRIGHT + f"▶ {text}")
    print(Fore.YELLOW + "─" * 52)

title("List Sum")

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how Python adds all values in a list using recursion by adding the head to the sum of the tail until the list becomes empty......")

print(Fore.LIGHTCYAN_EX + f"\nIn the list [1 , 4 , 9] , if we apply list sum , it becomes {list_sum([1 , 4 , 9])}.")
print(Fore.LIGHTCYAN_EX + f"In the list [1 , 8 , 27] , if we apply list sum , it becomes {list_sum([1 , 8 , 27])}.")

lst = [int(x) for x in input(Fore.LIGHTGREEN_EX + ("\nEnter numbers in any order you like (put atleast 2 numbers) : ")).split()]
guess = int(input(Fore.LIGHTCYAN_EX + f"What is the sum of {lst}?: "))
input("\nThe function list_sum adds the head of the list to list_sum(tail) meaning the tail of the list until the list is empty.Press Enter to Proceed.")
print(Fore.LIGHTCYAN_EX + f"\nThe sum of all the numbers in the list is {list_sum(lst)} . Your guess is {guess}.")