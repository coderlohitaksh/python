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
difficulty = 5

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
        time.sleep(0.03)
    print()

def title(text):
    print(Fore.CYAN + pyfiglet.figlet_format(text, font="slant"))

def select_difficulty():
    global difficulty
    slow("Select Difficulty:", Fore.CYAN)
    choice = ""
    while choice not in ["1", "2", "3"]:
        choice = input(Fore.YELLOW + "1-Easy 2-Medium 3-Hard: ")
        if choice not in ["1", "2", "3"]:
            slow("Invalid choice. Pick 1, 2, or 3.", Fore.RED)
    if choice == "1":
        difficulty = 5
    elif choice == "2":
        difficulty = 10
    else:
        difficulty = 20
    slow(f"Difficulty set! You will count up to {difficulty} in Level 1.", Fore.MAGENTA)

def intro():
    global player
    title("C o u n t i n g\nG a m e")
    player = input(Fore.YELLOW + "Enter your name: ").strip().title()
    slow(f"Hello, {player}! Prepare for the Counting Adventure!\n", Fore.MAGENTA)
    t = start_spinner()
    time.sleep(2)
    stop_spinner(t)

def level_one():
    global score
    slow(f"\nLEVEL 1: Count UP to {difficulty}!", Fore.CYAN)
    for i in range(1, difficulty + 1):
        while True:
            try:
                user_input = int(input(Fore.YELLOW + f"Enter number {i}: "))
                if user_input == i:
                    slow(f"Good! {i} is correct. | Score: {score}", Fore.GREEN)
                    break
                else:
                    score = max(0, score - 1)
                    slow(f"Oops! That's not {i}. -1 point | Score: {score}", Fore.RED)
            except ValueError:
                slow("Please enter a valid number!", Fore.RED)
    slow(f"\nWell done {player}, you counted to {difficulty}!", Fore.YELLOW)
    score += 5

def level_two():
    global score
    slow(f"\nLEVEL 2: Count DOWN from {difficulty}!", Fore.CYAN)
    for i in range(difficulty, 0, -1):
        while True:
            try:
                user_input = int(input(Fore.YELLOW + f"Enter number: "))
                if user_input == i:
                    slow(f"Correct! {i} | Score: {score}", Fore.GREEN)
                    break
                else:
                    score = max(0, score - 1)
                    slow(f"Wrong! -1 point | Score: {score}", Fore.RED)
            except ValueError:
                slow("Enter a valid number!", Fore.RED)
    slow(f"\nAwesome {player}, you completed the countdown!", Fore.YELLOW)
    score += 5

def level_three():
    global score
    slow("\nLEVEL 3: Word Power!", Fore.CYAN)
    while True:
        words = input(Fore.YELLOW + "Enter 3 words, comma separated: ").split(",")
        updated = [w.strip().capitalize() for w in words if w.strip()]
        if len(updated) == 3:
            break
        else:
            score = max(0, score - 1)
            slow("Please enter exactly 3 words! -1 point | Score: {score}", Fore.RED)
    slow(f"Upgraded Words → {updated}", Fore.GREEN)
    score += 5

def final_screen():
    title("Game Over")
    slow(f"Player: {player}", Fore.CYAN)
    slow(f"Score : {score}/{5+5+5}", Fore.GREEN)
    if score == 15:
        slow("PERFECT RUN! COUNTING MASTER 🏆", Fore.YELLOW)
    else:
        slow("Good job! Try again for perfection!", Fore.MAGENTA)

def main():
    intro()
    select_difficulty()
    level_one()
    level_two()
    level_three()
    final_screen()

if __name__ == "__main__":
    main()
