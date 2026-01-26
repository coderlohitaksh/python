import os
import sys
import time
import math
import platform
import datetime
import shutil
from colorama import Fore, Style, init

init(autoreset=True)

def slow_print(text, delay=0.03, color=Fore.WHITE, style=Style.NORMAL):
    for ch in text:
        print(style + color + ch, end="", flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def spinner(duration=1.2):
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end = time.time() + duration
    while time.time() < end:
        for f in frames:
            print(Style.BRIGHT + Fore.MAGENTA + f + " Loading...", end="\r", flush=True)
            time.sleep(0.05)
    print(" " * 40, end="\r")

def show_banner():
    banner = """
 ██████╗ ██╗ ██████╗   ██████╗ ██╗      ███████╗
██╔════╝ ██║ ██╔══██╗ ██╔════╝ ██║      ██╔════╝
██║      ██║ ██████╔╝ ██║      ██║      █████╗  
██║      ██║ ██╔══██╗ ██║      ██║      ██╔══╝  
╚██████╗ ██║ ██║  ██║ ╚██████╗ ███████╗ ███████╗
 ╚═════╝ ╚═╝ ╚═╝  ╚═╝  ╚═════╝ ╚══════╝ ╚══════╝
"""
    width = shutil.get_terminal_size().columns
    for line in banner.splitlines():
        print(Style.BRIGHT + Fore.CYAN + line.center(width))
    slow_print("● CIRCLE INFORMATION SYSTEM ●".center(width), 0.04, Fore.YELLOW, Style.BRIGHT)

class Circle:
    pi = math.pi

    def __init__(self, radius):
        self.radius = radius
        self.created_on = datetime.datetime.now()

    def area(self):
        return Circle.pi * self.radius ** 2

    def perimeter(self):
        return 2 * Circle.pi * self.radius

    def diameter(self):
        return 2 * self.radius

    def display(self):
        slow_print("\nCIRCLE DETAILS", 0.03, Fore.GREEN, Style.BRIGHT)
        print(Style.DIM + "-" * 55)
        print(Fore.CYAN + "Radius        :" + Style.BRIGHT + f" {self.radius}")
        print(Fore.CYAN + "Diameter      :" + Style.BRIGHT + f" {self.diameter():.2f}")
        print(Fore.YELLOW + "Area          :" + Style.BRIGHT + f" {self.area():.2f}")
        print(Fore.YELLOW + "Perimeter     :" + Style.BRIGHT + f" {self.perimeter():.2f}")
        print(Fore.BLUE + "Created On    :" + Style.DIM + f" {self.created_on.strftime('%d-%m-%Y %H:%M:%S')}")
        print(Style.DIM + "-" * 55)

def main():
    clear_screen()
    show_banner()
    slow_print("\nInitializing engine...", 0.04, Fore.CYAN)
    spinner()

    try:
        radius = float(input(Style.BRIGHT + Fore.YELLOW + "\nEnter radius: "))
        if radius <= 0:
            slow_print("Radius must be greater than zero", 0.04, Fore.RED, Style.BRIGHT)
            sys.exit()
        time.sleep(0.4)

        slow_print("\nSYSTEM INFORMATION", 0.04, Fore.CYAN, Style.BRIGHT)
        slow_print(f"Platform        : {platform.system()}", 0.02, Fore.WHITE)
        slow_print(f"Python Version  : {sys.version.split()[0]}", 0.02, Fore.WHITE)
        slow_print("\nCalculation completed successfully", 0.04, Fore.GREEN, Style.BRIGHT)

    except ValueError:
        slow_print("Invalid input. Enter numeric value only.", 0.04, Fore.RED, Style.BRIGHT)

if __name__ == "__main__":
    main()
