import pyfiglet
from colorama import Fore, init
import random
import time
import statistics
import itertools
import threading
import sys
import shutil

init(autoreset=True)
spinner_running = False

def spinner(duration=None):
    frames = ["⠁","⠃","⠇","⠧","⠷","⠿","⠟","⠯","⠷","⠾","⠽","⠻"]
    neon = [Fore.MAGENTA, Fore.CYAN, Fore.BLUE, Fore.YELLOW, Fore.GREEN]
    if duration is None:
        duration = random.randint(10, 20)
    start_time = time.time()
    color_index = 0
    while time.time() - start_time < duration and spinner_running:
        for frame in frames:
            if not spinner_running:
                break
            term_width = shutil.get_terminal_size().columns
            color = neon[color_index % len(neon)]
            text = f"{color}Processing {frame}"
            centered = text.center(term_width)
            sys.stdout.write("\r" + centered)
            sys.stdout.flush()
            color_index += 1
            time.sleep(0.08)
    term_width = shutil.get_terminal_size().columns
    done_msg = Fore.LIGHTGREEN_EX + "Done!"
    sys.stdout.write("\r" + done_msg.center(term_width) + "\n")
    sys.stdout.flush()

def start_spinner(duration=None):
    global spinner_running
    spinner_running = True
    t = threading.Thread(target=spinner, args=(duration,))
    t.start()
    return t

def stop_spinner(thread):
    global spinner_running
    spinner_running = False
    thread.join()

def rainbow(text):
    banner = pyfiglet.figlet_format(text, font="slant")
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    for i, line in enumerate(banner.splitlines()):
        print(colors[i % len(colors)] + line)

def rainbow_animate(text):
    banner = pyfiglet.figlet_format(text, font="slant")
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    for line in banner.splitlines():
        for i, char in enumerate(line):
            color = colors[i % len(colors)]
            print(color + char, end='', flush=True)
            time.sleep(0.005)
        print()

def pause(sec=1):
    time.sleep(sec)

def say_hello():
    name = input(Fore.CYAN + "What's your name? ")
    rainbow_animate(f"Hello, {name}!")
    print(Fore.MAGENTA + "Welcome to Array Adventure! ✨\n")
    time.sleep(1)

def show_array(arr):
    t = start_spinner()
    stop_spinner(t)
    print(Fore.MAGENTA + "\nCurrent Array:")
    print(Fore.CYAN + str(arr))

def count_occurrence(arr):
    print(Fore.YELLOW + "\nEnter number to count:")
    try:
        num = int(input("> "))
        t = start_spinner()
        stop_spinner(t)
        c = arr.count(num)
        print(Fore.GREEN + f"{num} appears {c} time(s).")
    except ValueError:
        print(Fore.RED + "Enter a valid integer!")

def reverse_array(arr):
    t = start_spinner()
    arr.reverse()
    stop_spinner(t)
    print(Fore.CYAN + "\nReversed Array:")
    print(arr)

def add_number(arr):
    print(Fore.YELLOW + "\nEnter a number to add:")
    try:
        num = int(input("> "))
        t = start_spinner()
        arr.append(num)
        stop_spinner(t)
        print(Fore.GREEN + f"{num} added!")
    except ValueError:
        print(Fore.RED + "Invalid number!")

def remove_number(arr):
    print(Fore.YELLOW + "\nEnter number to remove:")
    try:
        num = int(input("> "))
        if num in arr:
            t = start_spinner()
            arr.remove(num)
            stop_spinner(t)
            print(Fore.GREEN + f"{num} removed!")
        else:
            print(Fore.RED + "Number not found!")
    except ValueError:
        print(Fore.RED + "Enter a valid integer!")

def array_stats(arr):
    t = start_spinner()
    stop_spinner(t)
    print(Fore.MAGENTA + "\nArray Statistics:")
    print(Fore.CYAN + f"Sum = {sum(arr)}")
    print(Fore.CYAN + f"Mean = {statistics.mean(arr)}")
    print(Fore.CYAN + f"Min = {min(arr)}")
    print(Fore.CYAN + f"Max = {max(arr)}")

def print_menu_box():
    term_width = shutil.get_terminal_size().columns
    menu_width = 40
    print(Fore.CYAN + ("╔" + "═" * menu_width + "╗").center(term_width))
    print(Fore.CYAN + ("║" + "MAIN MENU".center(menu_width) + "║").center(term_width))
    print(Fore.CYAN + ("╠" + "═" * menu_width + "╣").center(term_width))
    print(Fore.YELLOW + ("║" + "1. Show Array".ljust(menu_width) + "║").center(term_width))
    print(Fore.YELLOW + ("║" + "2. Count Occurrence".ljust(menu_width) + "║").center(term_width))
    print(Fore.YELLOW + ("║" + "3. Reverse Array".ljust(menu_width) + "║").center(term_width))
    print(Fore.YELLOW + ("║" + "4. Add a Number".ljust(menu_width) + "║").center(term_width))
    print(Fore.YELLOW + ("║" + "5. Remove a Number".ljust(menu_width) + "║").center(term_width))
    print(Fore.YELLOW + ("║" + "6. Array Statistics".ljust(menu_width) + "║").center(term_width))
    print(Fore.YELLOW + ("║" + "7. Exit".ljust(menu_width) + "║").center(term_width))
    print(Fore.CYAN + ("╚" + "═" * menu_width + "╝").center(term_width))

def menu():
    say_hello()
    arr = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10]
    rainbow("Array Adventure")
    print(Fore.YELLOW + "Loading Adventure...")
    t = start_spinner()
    stop_spinner(t)
    while True:
        print_menu_box()
        choice = input(Fore.CYAN + "\nChoose an option (1 - 7): ")
        if choice == "1":
            show_array(arr)
        elif choice == "2":
            count_occurrence(arr)
        elif choice == "3":
            reverse_array(arr)
        elif choice == "4":
            add_number(arr)
        elif choice == "5":
            remove_number(arr)
        elif choice == "6":
            array_stats(arr)
        elif choice == "7":
            rainbow("Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice, try again.")

menu()
