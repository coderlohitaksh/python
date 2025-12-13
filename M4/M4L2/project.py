import os
import time
import shutil
import pyfiglet
from colorama import Fore, init

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

# ---------------------- LOADING DOTS ----------------------
def loading_dots(text):
    for i in range(3):
        print(Fore.CYAN + f"\n{text}" + "." * (i + 1))
        time.sleep(0.4)

# ---------------------- SPINNER ----------------------
def spinner_loading(text="Calculating...", duration=3):
    spinner = ["⠁","⠃","⠇","⠧","⠷","⠿","⠟","⠯","⠷","⠾","⠽","⠻"]
    width = shutil.get_terminal_size().columns
    msg = text + " "

    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        frame = spinner[i % len(spinner)]
        line = msg + frame
        pad = (width - len(line)) // 2
        print(" " * pad + Fore.CYAN + line, end="\r")
        time.sleep(0.09)
        i += 1

    print(" " * width, end="\r")

# ---------------------- TUPLE PRODUCT FUNCTION ----------------------
def tuple_product(t):
    product = 1
    for num in t:
        product *= num
    return product

def game_intro():
    os.system("cls" if os.name == "nt" else "clear")
    rainbow_big_text("W E L C O M E")
    time.sleep(1)

    name = input(Fore.YELLOW + "\nEnter your name: ")
    age = int(input(Fore.YELLOW + "Enter your age: "))

    loading_dots("Initializing experience")
    spinner_loading("Loading cinematic", duration=3)

    os.system("cls" if os.name == "nt" else "clear")
    rainbow_big_text("P Y T H O N\nE X P E R I E N C E")

    if age < 13:
        age_msg = "You are a young explorer! Curiosity is your power 🚀"
    elif age < 18:
        age_msg = "You are a rising coder! Skill is forming 🔥"
    else:
        age_msg = "You are a Python adventurer! Logic leads the way 🧠"

    print(Fore.CYAN + f"""
Hello {name},

{age_msg}

This program is a cinematic Python experience.
You will explore tuple calculations,
see execution speed,
and enjoy colorful animations.

Sit back and enjoy the journey.
""")

    input(Fore.GREEN + "\nPress Enter to enter the menu...")

# ---------------------- TUPLE PRODUCT OPTION ----------------------
def tuple_product_option():
    os.system("cls" if os.name == "nt" else "clear")
    rainbow_big_text("T U P L E\nP R O D U C T")

    tuple1 = (4, 3, 2, 2, -1, 18)
    tuple2 = (2, 4, 8, 8, 3, 2, 8)

    print(Fore.YELLOW + "\nTuple 1:", tuple1)
    print(Fore.YELLOW + "Tuple 2:", tuple2)

    loading_dots("Starting calculation")
    spinner_loading("Calculating product", duration=3)

    start_time = time.time()
    product1 = tuple_product(tuple1)
    product2 = tuple_product(tuple2)
    end_time = time.time()

    print(Fore.GREEN + "\nProduct of Tuple 1:", product1)
    print(Fore.GREEN + "Product of Tuple 2:", product2)

    print(Fore.MAGENTA + f"\nExecution Time: {end_time - start_time:.6f} seconds")
    input(Fore.CYAN + "\nPress Enter to return to menu...")

# ---------------------- MAIN MENU ----------------------
def main_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        rainbow_big_text("P Y T H O N\nM E N U")

        print(Fore.CYAN + """
============================
        MAIN MENU
==========================
1. Find product of tuples
2. Exit
""")

        choice = input(Fore.YELLOW + "Select an option: ")

        if choice == "1":
            tuple_product_option()
        elif choice == "2":
            print(Fore.GREEN + "\nThank you for playing!\n")
            time.sleep(1)
            break
        else:
            print(Fore.RED + "\nInvalid choice! Try again.")
            time.sleep(1)

# ---------------------- RUN PROGRAM ----------------------
game_intro()
main_menu()
