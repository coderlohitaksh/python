import shutil
import time
import os
from colorama import Fore, init , Style
import pyfiglet
import re
import math
import sys
colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

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

rainbow_big_text("TRIGONOMETRY")

os.system('cls' if os.name == 'nt' else 'clear')

welcome_text = "Let's learn about Trigonometric Functions!"
print(Fore.YELLOW + Style.BRIGHT + welcome_text.center(80))
time.sleep(1)

try:
    angle_deg = float(input(Fore.GREEN + "\nEnter an angle in degrees: "))

    angle_rad = math.radians(angle_deg)

    sin_val = math.sin(angle_rad)
    cos_val = math.cos(angle_rad)
    tan_val = math.tan(angle_rad)

    print(Fore.MAGENTA + "\n--- Trigonometric Values ---")
    print(Fore.CYAN + f"Sine (sin {angle_deg}°) = {sin_val:.4f}")
    print(Fore.CYAN + f"Cosine (cos {angle_deg}°) = {cos_val:.4f}")
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
