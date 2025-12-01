import calendar
import time
import pyfiglet
import shutil
from colorama import Fore, Style, init

init(autoreset=True)
colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def rainbow_big_text(text):
    """Prints big colorful ASCII text centered in the terminal."""
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


def list_calendar_module_names():
    print(Fore.YELLOW + "\n=== Names in calendar module ===\n")
    for name in dir(calendar):
        print(Fore.GREEN + name)

def show_days_of_week():
    print(Fore.YELLOW + "\n=== Days of the Week ===\n")
    for day in calendar.day_name:
        print(Fore.CYAN + day)

def show_year_calendar():
    year = int(input(Fore.YELLOW + "\nEnter a year: "))
    print(Fore.GREEN + f"\n=== Calendar for {year} ===\n")
    print(calendar.calendar(year))

def show_current_time():
    print(Fore.YELLOW + "\nCurrent Time: ")
    print(Fore.GREEN + time.ctime())

def main_menu():
    rainbow_big_text("P Y T H O N \n C A L E N D E R")

    while True:
        print(Fore.CYAN + """
===========================
        MAIN MENU
===========================
1. Show all days of the week
2. Display calendar of a year
3. Show current time
4. Exit
""")

        choice = input(Fore.YELLOW + "Enter your choice: ")
        if choice == "1":
            show_days_of_week()
        elif choice == "2":
            show_year_calendar()
        elif choice == "3":
            show_current_time()
        elif choice == "4":
            print(Fore.CYAN + "\nThank you! Exiting...\nExited !\n")
            
            break
        else:
            print(Fore.RED + "\nInvalid choice! Try again.\n") 

main_menu()
