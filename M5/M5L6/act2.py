from colorama import Fore, Style, init
import time
import os
import sys

init(autoreset=True)

# ---------- Utils ----------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def type_text(text, speed=0.03):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# ---------- Title ----------
def cinematic_title():
    clear()

    title = [
" ██████╗ ██████╗ ███╗   ███╗██████╗ ",
"██╔════╝██╔═══██╗████╗ ████║██╔══██╗",
"██║     ██║   ██║██╔████╔██║██████╔╝",
"██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ",
"╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ",
" ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     "
    ]

    print(Fore.BLUE)
    for line in title:
        print(line)
        time.sleep(0.15)

    print(Fore.CYAN)
    type_text("\n        OBJECT COMPARISON TERMINAL\n", 0.04)

# ---------- Loading ----------
def loading():
    print(Fore.YELLOW)
    type_text("Initializing system...\n", 0.03)

    for _ in range(25):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(0.03)

    print("\n")

# ---------- Class ----------
class A:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

# ---------- Compare ----------
def compare(a1, a2):
    ob1 = A(a1)
    ob2 = A(a2)

    print(Fore.CYAN + "\nComparing objects...\n")
    time.sleep(0.5)

    print(Fore.WHITE + f"Object 1: {a1}")
    print(Fore.WHITE + f"Object 2: {a2}\n")

    time.sleep(0.5)

    if ob1 < ob2:
        type_text(Fore.GREEN + "Result: Object 1 < Object 2")
    elif ob1 == ob2:
        type_text(Fore.YELLOW + "Result: Object 1 == Object 2")
    else:
        type_text(Fore.RED + "Result: Object 1 > Object 2")

# ---------- Menu ----------
def menu():
    print(Fore.GREEN)
    print("\n====== MENU ======")
    print("1  Compare Objects")
    print("2  Exit")
    print("==================")

# ---------- Main ----------
def main():
    cinematic_title()
    loading()

    while True:
        menu()
        choice = input(Fore.YELLOW + "Choose option: ")

        if choice == "1":
            try:
                a1 = int(input(Fore.CYAN + "Enter value for Object 1: "))
                a2 = int(input(Fore.CYAN + "Enter value for Object 2: "))
            except ValueError:
                type_text(Fore.RED + "Invalid input!")
                continue

            clear()
            cinematic_title()
            compare(a1, a2)

            input(Fore.YELLOW + "\nPress Enter to continue...")

        elif choice == "2":
            type_text(Fore.RED + "Closing program...", 0.04)
            break

        else:
            type_text(Fore.RED + "Invalid option!")

# ---------- Run ----------
if __name__ == "__main__":
    main()
