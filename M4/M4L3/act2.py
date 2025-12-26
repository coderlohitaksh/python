import time
import shutil
import pyfiglet
import random
from colorama import Fore, init

init(autoreset=True)

colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

print(Fore.RED + "\nWARNING ! WARNING ! This game is in omega mode . ENJOY !!")

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

def flicker_menu(text):
    w = shutil.get_terminal_size().columns
    for _ in range(2):
        pad = (w - len(text)) // 2
        print(" " * pad + Fore.MAGENTA + text, end="\r")
        time.sleep(0.1)
        print(" " * pad + Fore.WHITE + text, end="\r")
        time.sleep(0.1)
    print(" " * pad + Fore.CYAN + text)

def type_out(msg, color=Fore.GREEN, delay=0.015, rainbow=False):
    if rainbow:
        for ch in msg:
            ch_color = random.choice(colors) if ch != " " else color
            print(ch_color + ch, end="", flush=True)
            time.sleep(delay)
    else:
        for ch in msg:
            print(color + ch, end="", flush=True)
            time.sleep(delay)
    print()

def omega_loader(text="Loading", duration=3):
    spinner = ["⠁","⠃","⠇","⠧","⠷","⠿","⠟","⠯","⠷","⠾","⠽","⠻"] 
    width = shutil.get_terminal_size().columns
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        dots = "." * ((i % 3) + 1)
        frame = spinner[i % len(spinner)]
        line = f"{text}{dots} {frame}"
        pad = (width - len(line)) // 2
        print(" " * pad + Fore.CYAN + line, end="\r", flush=True)
        time.sleep(0.15)
        i += 1
    print(" " * width, end="\r")

def omega_menu():
    test_dict = {'Viswanathan Anand': 2, 'is': 2, 'known as': 2, 'the lightning': 2, 'kid .': 2}
    K = 5
    while True:
        print("\n")
        rainbow_big_text("Viswanathan Anand Statics")
        flicker_menu("1. SHOW DICTIONARY")
        flicker_menu("2. EXIT")
        print()
        choice = input(Fore.YELLOW + "Enter your choice: ")

        if choice == "1":
            print()
            type_out("The original dictionary was:", Fore.CYAN)
            omega_loader("Fetching Dictionary", 2)
            for key, value in test_dict.items():
                type_out(f"{key}: {value}", delay=0.02, rainbow=True)
            print("\n")
            final_msg = f"Frequency of Viswanathan Anand being world chess champion is {K} (2000 , 2007 , 2008 , 2010 , 2012)."
            type_out(final_msg, Fore.MAGENTA, 0.01)
            input(Fore.YELLOW + "\nPress Enter to return to menu...")
            print("\n")
        elif choice == "2":
            omega_loader("Exiting", 2)
            type_out("Goodbye!", Fore.MAGENTA, 0.02)
            break
        else:
            type_out("Invalid option! Only 1 and 2 allowed.", Fore.RED, 0.02)

omega_menu()
