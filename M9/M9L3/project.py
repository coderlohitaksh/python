
from colorama import Fore, Style, init

init(autoreset=True)

def bits(n, width=8):
    return format(n & ((1 << width) - 1), f"0{width}b")

def title(text):
    print(Fore.CYAN + Style.BRIGHT + "╔" + "═" * 50 + "╗")
    print(Fore.CYAN + Style.BRIGHT + f"║{text.center(50)}║")
    print(Fore.CYAN + Style.BRIGHT + "╚" + "═" * 50 + "╝")

def show_shrink(score_list):
    print("Current list:", score_list)
    if len(score_list) <= 1:
        print("Base case reached:", score_list)
        return
    show_shrink(score_list[1:])

def is_sorted(score_list):
    if len(score_list) <= 1:
        return True
    if score_list[0] > score_list[1]:
        return False
    return is_sorted(score_list[1:])

def list_sum(lst):
    if lst == []:
        return 0
    return lst[0] + list_sum(lst[1:])

def list_max(lst):
    if len(lst) == 0:
        raise ValueError("Cannot find maximum of an empty list")
    if len(lst) == 1:
        return lst[0]
    rest = list_max(lst[1:])
    return lst[0] if lst[0] > rest else rest

def section(text):
    print("\n" + Fore.YELLOW + Style.BRIGHT + f"▶ {text}")
    print(Fore.YELLOW + "─" * 52)

while True:
    try:
        score = [int(x) for x in input(Fore.LIGHTCYAN_EX + "\nEnter at least 5 numbers separated by spaces: ").split()]
        if len(score) < 5:
            print(Fore.RED + "Please enter at least 5 numbers.")
            continue
        break
    except ValueError:
        print(Fore.RED + "Invalid input! Enter integers only.")

title("Score List Explorer")

print(Fore.LIGHTCYAN_EX + "\nThe First Part - The Head and Tail Pattern")
input(Fore.LIGHTYELLOW_EX + "\nPress Enter to learn about the head-tail pattern...")
input(Fore.LIGHTYELLOW_EX + "\nThe head is the first element: lst[0]. The tail is the remaining list: lst[1:]. An empty list [] can act as a base case. Press Enter to proceed...")

print(Fore.LIGHTCYAN_EX + f"\nOriginal list: {score}")
print(Fore.LIGHTCYAN_EX + f"Head: {score[0]}")
print(Fore.LIGHTCYAN_EX + f"Tail: {score[1:]}")

print(Fore.LIGHTCYAN_EX + "\nThe Second Part - The Base Case for Lists")
input(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\nPress Enter to understand how recursion stops...")

print(Fore.LIGHTCYAN_EX + f"\nIn the list {score}, recursion keeps removing the head until only one element remains.")
print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "\nWatch how the list shrinks at each recursive call!\n")
show_shrink(score)
print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "\nRecursion reaches its base case!")

print(Fore.LIGHTCYAN_EX + "\nThe Third Part - The Sorted Check with Recursion")
input(Fore.LIGHTYELLOW_EX + "\nPress Enter to learn how recursion checks whether a list is sorted...")
print(Fore.LIGHTCYAN_EX + f"\nIn the list {score}, is_sorted() returns {is_sorted(score)}.")

if is_sorted(score):
    print(Fore.GREEN + "The list is sorted in ascending order.")
else:
    print(Fore.RED + "The list is not sorted in ascending order.")

print(Fore.LIGHTCYAN_EX + "\nThe Fourth Part - The Sum of a List with Recursion")
input(Fore.LIGHTYELLOW_EX + "\nPress Enter to learn how recursion adds all values in a list...")
print(Fore.LIGHTCYAN_EX + f"\nSum of {score} = {list_sum(score)}")

print(Fore.LIGHTCYAN_EX + "\nThe Fifth Part - The Largest Element with Recursion")
input(Fore.LIGHTYELLOW_EX + "\nPress Enter to learn how recursion finds the largest value in a list...")
print(Fore.LIGHTCYAN_EX + f"\nLargest element in {score} = {list_max(score)}")

print(Fore.GREEN + Style.BRIGHT + "\nThank you for exploring Python recursion!")
