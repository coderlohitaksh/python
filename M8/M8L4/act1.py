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


input(Fore.LIGHTYELLOW_EX + "N & (n-1) clears the rightmost set bit like in 10 or 1010 in binary , it clears the the rightmost 1 in 1010 so it becomes  1000 or 8 in Hindu-Arabic numeration. Press Enter to proceed . ")
print(Fore.LIGHTYELLOW_EX + "12 & 11 = ",12 & 11,"and the binary is ",bin(12 & 11)[2:])
print(Fore.LIGHTYELLOW_EX + "8 & 7 = ",8 & 7)

n = int(input((Fore.LIGHTGREEN_EX + "Enter a number (try 4 or 6) :")))
guess = input(Fore.LIGHTGREEN_EX + 
              (f"Is the number (str{n}) a power of 2 (Yes / No): ")
              )
input("Power of 2 (n & (n-1)) == 0 which means only one set bit which is 1 in binary is on . Press Enter to Proceed.")

if n > 0 and (n & (n-1)) == 0 :
    print(f"{n}'s binary number is {bin(n)[2:]} power of 2 is yes , you guess is {guess}")
else:
    print(f"{n}'s binary number is {bin(n)[2:]} power of 2 is no , you guess is {guess}")