import shutil
import time
import os
from colorama import Fore, init, Style
import pyfiglet
import math
import sys

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

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
rainbow_big_text("TRIGONOMETRY")
print(Fore.YELLOW + Style.BRIGHT + "\nLet's learn about Sin, Cos, and Tan!".center(80))
print(Fore.CYAN + "\nType an angle in degrees to calculate sin, cos, and tan.")
print(Fore.CYAN + "Type 'q' to quit.\n")

while True:
    user_input = input(Fore.GREEN + "\nEnter an angle in degrees (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    try:
        angle_deg = float(user_input)
        angle_rad = math.radians(angle_deg)
        sin_val = math.sin(angle_rad)
        cos_val = math.cos(angle_rad)

        print(Fore.MAGENTA + "\n--- Trigonometric Values ---")
        print(Fore.CYAN + f"Angle (radians) = {angle_rad:.4f}")
        print(Fore.CYAN + f"Sine (sin {angle_deg}°)   = {sin_val:.4f}")
        print(Fore.CYAN + f"Cosine (cos {angle_deg}°) = {cos_val:.4f}")

        if abs(cos_val) < 1e-10:
            print(Fore.CYAN + f"Tangent (tan {angle_deg}°) = Undefined (cos=0)")
        else:
            tan_val = math.tan(angle_rad)
            print(Fore.CYAN + f"Tangent (tan {angle_deg}°) = {tan_val:.4f}")

    except ValueError:
        print(Fore.RED + "Error: Please enter a valid number.")
    except Exception as e:
        print(Fore.RED + f"Unexpected error: {e}")

print(Fore.YELLOW + "\nExiting", end="")
for i in range(3):
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(0.5)
print(Fore.GREEN + "\nThank you for using the Trigonometric Calculator! ✨")
