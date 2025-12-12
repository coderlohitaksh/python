import os
import time
import shutil
import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)
colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

# ---------------------- RAINBOW ASCII TEXT ----------------------
def rainbow_big_text(text):
    ascii_banner = pyfiglet.figlet_format(text, font="standard")
    lines = ascii_banner.split("\n")
    terminal_width = shutil.get_terminal_size().columns
    max_line_length = max(len(line) for line in lines)
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

# ---------------------- SIMPLE LOADING DOTS ----------------------
def loading_animation(text):
    for i in range(3):
        print(Fore.CYAN + f"\n{text}" + "." * (i + 1))
        time.sleep(0.4)
    print()

# ---------------------- SPINNER LOADING ----------------------
def spinner_loading(text="Loading...", duration=3):
    spinner = ["⠁","⠃","⠇","⠧","⠷","⠿","⠟","⠯","⠷","⠾","⠽","⠻"]
    width = shutil.get_terminal_size().columns
    msg = text + " "

    for _ in range(duration * 4):
        for frame in spinner:
            line = msg + frame
            pad = (width - len(line)) // 2
            print(" " * pad + Fore.CYAN + line, end="\r")
            time.sleep(0.09)

    print(" " * width, end="\r")

# ---------------------- SQUARE FINDER FUNCTION ----------------------
def find_squares():
    os.system("cls" if os.name == "nt" else "clear")
    rainbow_big_text("S Q U A R E S")

    # Inputs
    start = int(input(Fore.YELLOW + "\nEnter start number: "))
    end = int(input(Fore.YELLOW + "Enter end number: "))
    print()

    # Loading animation
    spinner_loading("Calculating squares", duration=3)

    # Calculations
    squares = {n: n * n for n in range(start, end + 1)}
    odd_squares = {n: sq for n, sq in squares.items() if sq % 2 != 0}
    even_squares = {n: sq for n, sq in squares.items() if sq % 2 == 0}

    # Output
    print(Fore.GREEN + "\nAll Squares:\n")
    for n, sq in squares.items():
        print(f"{n}² = {sq}")
        time.sleep(0.04)

    print(Fore.MAGENTA + "\nOdd Squares:\n")
    for n, sq in odd_squares.items():
        print(f"{n}² = {sq}")
        time.sleep(0.04)

    print(Fore.BLUE + "\nEven Squares:\n")
    for n, sq in even_squares.items():
        print(f"{n}² = {sq}")
        time.sleep(0.04)

    input(Fore.YELLOW + "\nPress Enter to return to menu...")

# ---------------------- MAIN MENU ----------------------
def main_menu():
    os.system("cls" if os.name == "nt" else "clear")
    rainbow_big_text("P Y T H O N\nS Q U A R E S")

    while True:
        print(Fore.CYAN + """
===========================
        MAIN MENU
===========================
1. Find square values
2. Exit
""")

        choice = input(Fore.YELLOW + "Enter your choice: ")

        if choice == "1":
            find_squares()
            os.system("cls" if os.name == "nt" else "clear")
            rainbow_big_text("P Y T H O N\nS Q U A R E S")

        elif choice == "2":
            print(Fore.CYAN + "\nThank you! Exiting...\nExited!\n")
            break

        else:
            print(Fore.RED + "\nInvalid choice! Try again.\n")

# ---------------------- RUN PROGRAM ----------------------
main_menu()
