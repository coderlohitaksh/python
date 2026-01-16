import random
import string
import secrets
import os
import sys
import time
import platform
import getpass
import math
import shutil
from colorama import Fore, init

init(autoreset=True)

def slow_print(text, delay=0.03, color=Fore.WHITE):
    for ch in text:
        print(color + ch, end="", flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_banner():
    banner = """
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝
"""
    width = shutil.get_terminal_size().columns
    for line in banner.splitlines():
        print(Fore.CYAN + line.center(width))
    slow_print("🔐 PASSWORD GENERATOR 🔐".center(width), 0.04, Fore.YELLOW)

def generate_password(length, char_sets):
    password = [secrets.choice(cs) for cs in char_sets]
    all_chars = ''.join(char_sets)
    for _ in range(length - len(password)):
        password.append(secrets.choice(all_chars))
    random.shuffle(password)
    return "".join(password)

def calculate_strength(pwd):
    categories = [string.ascii_lowercase, string.ascii_uppercase, string.digits, "!@#$%^&*()-_=+[]{};:,.<>/?"]
    used_sets = sum(1 for cat in categories if any(c in cat for c in pwd))
    pool_size = sum(len(cat) for cat in categories if any(c in cat for c in pwd))
    pool_size = pool_size if pool_size > 0 else 1
    entropy = len(pwd) * math.log2(pool_size)
    if entropy < 40 or used_sets == 1:
        return Fore.RED + "Weak 😬"
    elif entropy < 70 or used_sets == 2:
        return Fore.YELLOW + "Moderate 🙂"
    else:
        return Fore.GREEN + "Strong 💪"

def fancy_spinner(duration=2):
    spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    while time.time() < end_time:
        for s in spinner:
            print(Fore.MAGENTA + f"\r{s} Generating...", end="", flush=True)
            time.sleep(0.05)
    print("\r" + " " * 20 + "\r", end="")

def generate_passwords_loop():
    MAX_LENGTH = 64

    while True:
        while True:
            try:
                length = int(input(Fore.CYAN + f"\nEnter password length (6 - {MAX_LENGTH}): "))
                if length < 6 or length > MAX_LENGTH:
                    raise ValueError
                break
            except ValueError:
                slow_print(f"❌ Please enter a number between 6 and {MAX_LENGTH}", 0.03, Fore.RED)

        char_sets = []

        if input(Fore.GREEN + "Include lowercase letters? (y/n): ").lower() == "y":
            char_sets.append(string.ascii_lowercase)

        if input(Fore.BLUE + "Include uppercase letters? (y/n): ").lower() == "y":
            char_sets.append(string.ascii_uppercase)

        if input(Fore.YELLOW + "Include numbers? (y/n): ").lower() == "y":
            char_sets.append(string.digits)

        if input(Fore.MAGENTA + "Include special symbols? (y/n): ").lower() == "y":
            char_sets.append("!@#$%^&*()-_=+[]{};:,.<>/?")

        custom_chars = input(Fore.CYAN + "Add any custom characters? (leave empty if none): ")
        if custom_chars:
            char_sets.append(custom_chars)

        if not char_sets:
            slow_print("❌ You must select at least one character type", 0.03, Fore.RED)
            continue

        if length < len(char_sets):
            slow_print(f"❌ Length must be at least {len(char_sets)} to include all selected types", 0.03, Fore.RED)
            continue

        while True:
            try:
                num = int(input(Fore.CYAN + "How many passwords to generate? "))
                if num < 1:
                    raise ValueError
                break
            except ValueError:
                slow_print("❌ Please enter a valid number", 0.03, Fore.RED)

        slow_print("\nGenerating your passwords...", 0.05, Fore.CYAN)
        fancy_spinner(1)

        passwords = []
        for _ in range(num):
            pwd = generate_password(length, char_sets)
            passwords.append(pwd)

        for i, pwd in enumerate(passwords, start=1):
            strength = calculate_strength(pwd)
            slow_print(f"\n🎉 Password {i}:", 0.03, Fore.GREEN)
            slow_print(f"🔑 {pwd}", 0.03, Fore.WHITE)
            slow_print(f"📊 Strength Level: {strength}", 0.03)

        replay = input(Fore.CYAN + "\nGenerate another batch? (y/n): ").lower()
        if replay != "y":
            break

def main():
    clear_screen()
    show_banner()
    time.sleep(0.5)
    user = getpass.getuser()
    slow_print(f"\nHello {user}! Ready to generate passwords?", 0.03, Fore.MAGENTA)
    generate_passwords_loop()
    slow_print("\n🖥 System Info", 0.03, Fore.CYAN)
    slow_print(f"Platform: {platform.system()}", 0.02, Fore.WHITE)
    slow_print(f"Python Version: {sys.version.split()[0]}", 0.02, Fore.WHITE)
    slow_print("\nStay safe and keep your passwords secure! 🔒", 0.03, Fore.YELLOW)

if __name__ == "__main__":
    main()
