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
    + "\nPress Enter to learn how Python uses tail recursion with an accumulator, adds each value as n counts down, and shows how the final result is built through repeated recursive calls.....")

print(Fore.LIGHTGREEN_EX + f"\nThe tail recursion of 4 is {tail_sum(4)}, which means 4 + 3 + 2 + 1.")
print(Fore.LIGHTGREEN_EX + f"The tail recursion of 5 is {tail_sum(5)}, which means 5 + 4 + 3 + 2 + 1.")

print(Fore.LIGHTCYAN_EX + "\nThe second part - Linear recursion")

def linear_sum(n , y = 0):
    if n == 0 :
        return y
    return linear_sum(n - 1)

input(
    Fore.LIGHTYELLOW_EX
     + "\nPress Enter to learn how Python uses linear recursion is the simplest shape: each call makes exactly one recursive call. The call chain is a straight line from the original call down to the base case, and then back up.....")


print(Fore.LIGHTGREEN_EX + f"\nThe linear recursion of 4 is {linear_sum(4)}, which means its going down to the base case 0 from 4 .")
print(Fore.LIGHTGREEN_EX + f"The linear recursion of 5 is {linear_sum(5)}, which means its going down to the base case 0 from 5 .")

print(Fore.LIGHTCYAN_EX + "\nThe third part - Head recursion")

def head_sum(n , x = 0):
    if n == 0 :
        return x
    return head_sum(n - 1)
    
input(
    Fore.LIGHTYELLOW_EX
     + "\nPress Enter to learn how Python uses A function is head recursive when the very first thing it does is the recursive call - before doing any other work on the    current value......")

print(Fore.LIGHTGREEN_EX + f"\nThe head recursion of 4 is {head_sum(4)}, which means it is going to the reverse order from 4 like 4 , 3 , 2 , 1 , 0.")
print(Fore.LIGHTGREEN_EX + f"\nThe head recursion of 5 is {head_sum(5)}, which means it is going to the reverse order from 5 like 5 , 4 , 3 , 2 , 1 , 0.")

print(Fore.LIGHTCYAN_EX + "\nThe fourth part - Increasing and Decreasing recursion")

def mirror(n):
    if n == 0:
        return 0
    rest = mirror(n-1)
    return rest + 2*n

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how Python uses head recursion by making the recursive call first and then adding values while the function unwinds back up.....")

print(Fore.LIGHTGREEN_EX + f"\nThe mirror of 3 is {mirror(3)} , which is 3 + 2 + 1 + 0 + 1 + 2 + 3.")
print(Fore.LIGHTGREEN_EX + f"The mirror of 4 is {mirror(4)} , which is 4 + 3 + 2 + 1 + 0 + 1 + 2 + 3 + 4.")

print(Fore.LIGHTCYAN_EX + "\nThe fourth part - Tree recursion")

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

input(
    Fore.LIGHTYELLOW_EX
    + "Press Enter to learn how Python uses Fibonacci to demonstrate tree recursion, where each function call creates two more recursive calls until the base cases are reached.....")

print(Fore.LIGHTGREEN_EX + f"\nThe fibonacci number of 5th indexing is {fib(5)} , the sequence is 0, 1, 1, 2, 3, 5.")
print(Fore.LIGHTGREEN_EX + f"The fibonacci number of 6th indexing is {fib(6)} , the sequence is 0, 1, 1, 2, 3, 5, 8.") 