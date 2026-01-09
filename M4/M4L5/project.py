import pyfiglet
from colorama import Fore, init
import time
import threading
import sys
import shutil
import random

init(autoreset=True)

spinner_running = False
score = 0
player = ""

def spinner(duration=1.5):
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    colors = [Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.GREEN]
    start = time.time()
    i = 0
    while time.time() - start < duration and spinner_running:
        frame = frames[i % len(frames)]
        color = colors[i % len(colors)]
        text = f"{color}Loading {frame}"
        sys.stdout.write("\r" + text.center(shutil.get_terminal_size().columns))
        sys.stdout.flush()
        i += 1
        time.sleep(0.08)
    sys.stdout.write("\r" + Fore.GREEN + "Ready!".center(shutil.get_terminal_size().columns) + "\n")

def start_spinner():
    global spinner_running
    spinner_running = True
    t = threading.Thread(target=spinner)
    t.start()
    return t

def stop_spinner(t):
    global spinner_running
    spinner_running = False
    t.join()

def slow(text, color=Fore.WHITE):
    text = str(text)
    for c in text:
        sys.stdout.write(color + c)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

def title(text):
    print(Fore.CYAN + pyfiglet.figlet_format(text, font="slant"))

def intro():
    global player
    title("P y t h o n\nG a m e")
    player = input(Fore.YELLOW + "Enter your name: ").strip().title()
    slow(f"Welcome {player}, prepare for the List Comprehension Trials!\n", Fore.MAGENTA)
    time.sleep(1)

def level_one():
    global score
    slow("LEVEL 1: Even & Odd Challenge", Fore.CYAN)
    while True:
        try:
            n = int(input(Fore.YELLOW + "Enter a number: "))
            if n < 0:
                slow("Enter a positive number only!", Fore.RED)
                continue
            break
        except ValueError:
            slow("Enter a valid number only!", Fore.RED)

    t = start_spinner()
    time.sleep(1)
    stop_spinner(t)

    even = [i for i in range(n) if i % 2 == 0]
    odd = [i for i in range(n) if i % 2 != 0]

    slow(f"Even Numbers → {even}", Fore.GREEN)
    slow(f"Odd Numbers  → {odd}", Fore.MAGENTA)
    score += 10

def level_two():
    global score
    n1 = int(input(Fore.YELLOW + "Enter your starting range : "))
    slow(n1)
    n2 = int(input(Fore.YELLOW + "Enter your ending range : "))
    slow(n2)
    slow("\nLEVEL 2: Odd Hunter", Fore.CYAN)

    t = start_spinner()
    time.sleep(1)
    stop_spinner(t)

    odd_list = [i for i in range(n1, n2) if i % 2 != 0]
    slow(f"Odd Numbers Found → {odd_list}", Fore.GREEN)
    score += 10

def level_three():
    global score
    slow("\nLEVEL 3: Word Power", Fore.CYAN)
    words = input(Fore.YELLOW + "Enter words (comma separated): ").split(",")
    slow(", ".join(words))

    t = start_spinner()
    time.sleep(1)
    stop_spinner(t)

    updated = [w.strip().capitalize() for w in words if w.strip()]
    slow(f"Upgraded Words → {updated}", Fore.GREEN)
    score += 10

def final_screen():
    title("Game Over")
    slow(f"Player: {player}", Fore.CYAN)
    slow(f"Score : {score}/30", Fore.GREEN)
    if score == 30:
        slow("PERFECT RUN! LIST MASTER 🏆", Fore.YELLOW)
    else:
        slow("Good job! Try again for perfection!", Fore.MAGENTA)

def main():
    intro()
    level_one()
    level_two()
    level_three()
    final_screen()

main()
