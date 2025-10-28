import math
import os
import sys
import time
from colorama import Fore, Style, init
import pyfiglet
import shutil

init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')
colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def rainbow_big_text_per_word(text_lines):
    terminal_width = shutil.get_terminal_size().columns if os.isatty(sys.stdout.fileno()) else 80
    if isinstance(text_lines, str):
        words = text_lines.splitlines()
    else:
        words = list(text_lines)
    for word in words:
        if not word.strip():
            print()
            continue
        ascii_banner = pyfiglet.figlet_format(word, font="standard")
        lines = ascii_banner.splitlines()
        max_line_length = max((len(l) for l in lines), default=0)
        left_padding = max((terminal_width - max_line_length) // 2, 0)
        color_index = 0
        for line in lines:
            colored_line = ""
            for char in line:
                if char != " ":
                    colored_line += colors[color_index % len(colors)] + char
                    color_index += 1
                else:
                    colored_line += " "
            print(" " * left_padding + colored_line)
        print()

def typewrite(text, color=Fore.WHITE, delay=0.02, end="\n"):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    if end:
        sys.stdout.write(end)

def floor_and_ceiling():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner_lines = ["F L O O R", "V A L U E S", "A N D", "C E I L I N G", "V A L U E S"]
    rainbow_big_text_per_word(banner_lines)
    term_width = shutil.get_terminal_size().columns if os.isatty(sys.stdout.fileno()) else 80
    title = "🧮 Floor & Ceiling Calculator 🧮"
    print(Fore.CYAN + Style.BRIGHT + title.center(term_width))
    print(Fore.CYAN + "=" * term_width)
    typewrite("Enter a number: ", Fore.YELLOW)
    try:
        num = float(input())
    except ValueError:
        print(Fore.RED + "\n❌ Invalid input! Please enter a numeric value.")
        time.sleep(2)
        main_menu()
        return
    print(Fore.BLUE + "\nCalculating floor and ceiling values...")
    time.sleep(1)
    floor_val = math.floor(num)
    ceil_val = math.ceil(num)
    print()
    typewrite(f"   Floor value of {num} → {floor_val}", Fore.GREEN)
    time.sleep(0.4)
    typewrite(f"   Ceiling value of {num} → {ceil_val}", Fore.MAGENTA)
    time.sleep(0.7)
    print(Fore.CYAN + "=" * term_width)
    typewrite("Calculation Complete ✅".center(term_width), Fore.LIGHTYELLOW_EX)
    print(Fore.BLUE + "Returning to main menu...".center(term_width))
    time.sleep(2)
    main_menu()

#

def copy_sign_calc():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner_lines = ["C O P Y", "S I G N", "C A L C U L A T O R"]
    rainbow_big_text_per_word(banner_lines)
    term_width = shutil.get_terminal_size().columns if os.isatty(sys.stdout.fileno()) else 80
    title = "⚡ Copy Sign Demonstrator ⚡"
    print(Fore.CYAN + Style.BRIGHT + title.center(term_width))
    print(Fore.CYAN + "=" * term_width)
    typewrite("Enter your first number (x): ", Fore.YELLOW)
    try:
        x = float(input())
    except ValueError:
        typewrite("\n❌ Invalid input! Please enter a numeric value.\n", Fore.RED)
        time.sleep(2)
        main_menu()
        return
    typewrite("Enter your second number (y): ", Fore.YELLOW)
    try:
        y = float(input())
    except ValueError:
        typewrite("\n❌ Invalid input! Please enter a numeric value.\n", Fore.RED)
        time.sleep(2)
        main_menu()
        return
    typewrite("\nProcessing sign copy operation...\n", Fore.BLUE, 0.03)
    time.sleep(1)
    result = math.copysign(x, y)
    time.sleep(0.3)
    typewrite(f"\n   ➤ Original x value: {x}", Fore.GREEN)
    time.sleep(0.4)
    typewrite(f"\n   ➤ Sign source (y): {y}", Fore.MAGENTA)
    time.sleep(0.4)
    typewrite(f"\n   ➤ Result after copying sign: {result}", Fore.CYAN)
    time.sleep(0.7)
    print(Fore.CYAN + "\n" + "=" * term_width)
    typewrite("Operation Complete ✅".center(term_width) + "\n", Fore.LIGHTYELLOW_EX, 0.01)
    typewrite("Thanks for using the Copy Sign Calculator!".center(term_width) + "\n", Fore.BLUE, 0.01)
    print(Fore.BLUE + "Returning to main menu...".center(term_width))
    time.sleep(2)
    main_menu()

#

def absolute_value_calc():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner_lines = ["A B S O L U T E", "V A L U E S"]
    rainbow_big_text_per_word(banner_lines)
    term_width = shutil.get_terminal_size().columns if os.isatty(sys.stdout.fileno()) else 80
    title = "📏 Absolute Value Calculator 📏"
    print(Fore.CYAN + Style.BRIGHT + title.center(term_width))
    print(Fore.CYAN + "=" * term_width)
    typewrite("Enter your first number (x): ", Fore.YELLOW)
    try:
        x = float(input())
    except ValueError:
        typewrite("\n❌ Invalid input! Please enter a numeric value.\n", Fore.RED)
        time.sleep(2)
        main_menu()
        return
    typewrite("Enter your second number (y): ", Fore.YELLOW)
    try:
        y = float(input())
    except ValueError:
        typewrite("\n❌ Invalid input! Please enter a numeric value.\n", Fore.RED)
        time.sleep(2)
        main_menu()
        return
    typewrite("\nCalculating absolute values...\n", Fore.BLUE, 0.03)
    time.sleep(1)
    abs_x = math.fabs(x)
    abs_y = math.fabs(y)
    typewrite(f"\n   |{x}| = {abs_x}", Fore.GREEN)
    time.sleep(0.4)
    typewrite(f"\n   |{y}| = {abs_y}", Fore.MAGENTA)
    time.sleep(0.7)
    print(Fore.CYAN + "\n" + "=" * term_width)
    typewrite("Calculation Complete ✅".center(term_width) + "\n", Fore.LIGHTYELLOW_EX, 0.01)
    typewrite("Thanks for using the Absolute Value Calculator!".center(term_width) + "\n", Fore.BLUE, 0.01)
    print(Fore.BLUE + "Returning to main menu...".center(term_width))
    time.sleep(2)
    main_menu()

#

def gcd_calc():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner_lines = ["G C D", "C A L C U L A T O R"]
    rainbow_big_text_per_word(banner_lines)
    term_width = shutil.get_terminal_size().columns if os.isatty(sys.stdout.fileno()) else 80
    title = "📘 Greatest Common Divisor Calculator 📘"
    print(Fore.CYAN + Style.BRIGHT + title.center(term_width))
    print(Fore.CYAN + "=" * term_width)
    try:
        typewrite("Enter your first number: ", Fore.YELLOW)
        x = int(float(input()))
        typewrite("Enter your second number: ", Fore.YELLOW)
        y = int(float(input()))
    except ValueError:
        typewrite("\n❌ Invalid input! Please enter numeric values.\n", Fore.RED)
        time.sleep(2)
        main_menu()
        return
    typewrite("\nCalculating GCD...\n", Fore.BLUE, 0.03)
    time.sleep(1)
    gcd_val = math.gcd(x, y)
    typewrite(f"\n   The GCD of {x} and {y} is: {gcd_val}\n", Fore.GREEN)
    print(Fore.CYAN + "=" * term_width)
    typewrite("Calculation Complete ✅\n", Fore.LIGHTYELLOW_EX)
    print(Fore.BLUE + "Returning to main menu...".center(term_width))
    time.sleep(2)
    main_menu()

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner_lines = ["M A T H", "T O O L S"]
    rainbow_big_text_per_word(banner_lines)
    term_width = shutil.get_terminal_size().columns if os.isatty(sys.stdout.fileno()) else 80
    title = "✨ Welcome to the Math Tools Hub ✨"
    print(Fore.CYAN + Style.BRIGHT + title.center(term_width))
    print(Fore.CYAN + "=" * term_width)
    print()
    typewrite("Choose an option:\n", Fore.YELLOW)
    typewrite("  1️⃣  Floor & Ceiling Calculator\n", Fore.GREEN)
    typewrite("  2️⃣  Copy Sign Calculator\n", Fore.MAGENTA)
    typewrite("  3️⃣  Absolute Value Calculator\n", Fore.BLUE)
    typewrite("  4️⃣  GCD Calculator\n", Fore.LIGHTGREEN_EX)
    typewrite("  5️⃣  Exit\n\n", Fore.RED)
    typewrite("Enter your choice: ", Fore.CYAN)
    choice = input().strip()
    if choice == "1":
        floor_and_ceiling()
    elif choice == "2":
        copy_sign_calc()
    elif choice == "3":
        absolute_value_calc()
    elif choice == "4":
        gcd_calc()
    elif choice == "5":
        os.system('cls' if os.name == 'nt' else 'clear')
        typewrite("Goodbye! 👋\n", Fore.LIGHTYELLOW_EX)
        sys.exit(0)
    else:
        typewrite("\n❌ Invalid choice! Try again...\n", Fore.RED)
        time.sleep(1.5)
        main_menu()

if __name__ == "__main__":
    main_menu()
