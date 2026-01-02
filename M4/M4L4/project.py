import pyfiglet
from colorama import Fore, init
import time
import threading
import sys
import shutil

init(autoreset=True)
spinner_running = False
history = []
user_name = ""

def spinner(duration=2):
    frames = ["⠁","⠃","⠇","⠧","⠷","⠿","⠟","⠯","⠷","⠾","⠽","⠻"]
    neon = [Fore.MAGENTA, Fore.CYAN, Fore.BLUE, Fore.YELLOW, Fore.GREEN]
    start_time = time.time()
    color_index = 0
    while time.time() - start_time < duration and spinner_running:
        for frame in frames:
            if not spinner_running:
                break
            term_width = shutil.get_terminal_size().columns
            color = neon[color_index % len(neon)]
            text = f"{color}Processing {frame}"
            sys.stdout.write("\r" + text.center(term_width))
            sys.stdout.flush()
            color_index += 1
            time.sleep(0.08)
    term_width = shutil.get_terminal_size().columns
    done_msg = Fore.LIGHTGREEN_EX + "Done!"
    sys.stdout.write("\r" + done_msg.center(term_width) + "\n")
    sys.stdout.flush()

def start_spinner(duration=2):
    global spinner_running
    spinner_running = True
    t = threading.Thread(target=spinner, args=(duration,))
    t.start()
    return t

def stop_spinner(thread):
    global spinner_running
    spinner_running = False
    thread.join()

def rainbow_ascii_letters(text):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    letters = list(text)
    ascii_letters = [pyfiglet.figlet_format(c, font="slant").splitlines() for c in letters]
    max_height = max(len(a) for a in ascii_letters)
    for i in range(len(ascii_letters)):
        while len(ascii_letters[i]) < max_height:
            ascii_letters[i].append(" " * len(ascii_letters[i][0]))
    final_lines = [""] * max_height
    for i, ascii_letter in enumerate(ascii_letters):
        for j in range(max_height):
            final_lines[j] += ascii_letter[j] + "  "
        sys.stdout.write("\033[H\033[J")
        for k, line in enumerate(final_lines):
            color = colors[(i + k) % len(colors)]
            print(color + line)
        time.sleep(0.2)
    print("\n")

def greet():
    global user_name
    user_name = input(Fore.CYAN + "What's your name? \n")
    print()
    rainbow_ascii_letters("Hello,")
    rainbow_ascii_letters(user_name)
    print(Fore.MAGENTA + "Welcome to the Symmetric Difference Finder! ✨\n")
    time.sleep(1)

def get_ordered_list(prompt):
    items = input(prompt).split(",")
    ordered = []
    for item in items:
        item = item.strip()
        try:
            ordered.append(int(item))
        except ValueError:
            ordered.append(item)
    return ordered

def print_one_by_one(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def symmetric_difference_demo():
    list1 = get_ordered_list("Enter elements of first set (comma-separated): ")
    list2 = get_ordered_list("Enter elements of second set (comma-separated): ")
    set1, set2 = set(list1), set(list2)
    t = start_spinner()
    time.sleep(1)
    stop_spinner(t)
    sym_diff_set = set1.symmetric_difference(set2)
    sym_diff_ordered = [x for x in list1 + list2 if x in sym_diff_set]
    formatted = "{ " + ", ".join(str(x) for x in sym_diff_ordered) + " }"
    history.append(formatted)
    print(Fore.GREEN + "\nSymmetric Difference: ", end='')
    print_one_by_one(formatted)
    print()

def view_history():
    if not history:
        print(Fore.RED + "\nNo previous results.\n")
        return
    print(Fore.CYAN + "\nHistory of Symmetric Differences:\n")
    for i, res in enumerate(history, 1):
        print_one_by_one(f"{i}. {res}")
    print()

def clear_history():
    global history
    history = []
    print(Fore.YELLOW + "\nHistory cleared!\n")

def print_menu():
    term_width = shutil.get_terminal_size().columns
    menu_width = 50
    print(Fore.CYAN + ("╔" + "═" * menu_width + "╗").center(term_width))
    print(Fore.CYAN + ("║" + "MAIN MENU".center(menu_width) + "║").center(term_width))
    print(Fore.CYAN + ("╠" + "═" * menu_width + "╣").center(term_width))
    print(Fore.YELLOW + ("║" + "1. Compute Symmetric Difference".ljust(menu_width) + "║").center(term_width))
    print(Fore.YELLOW + ("║" + "2. View History".ljust(menu_width) + "║").center(term_width))
    print(Fore.YELLOW + ("║" + "3. Clear History".ljust(menu_width) + "║").center(term_width))
    print(Fore.YELLOW + ("║" + "4. Exit".ljust(menu_width) + "║").center(term_width))
    print(Fore.CYAN + ("╚" + "═" * menu_width + "╝").center(term_width))

def main():
    greet()
    while True:
        print_menu()
        choice = input(Fore.CYAN + "\nChoose an option (1-4): ").strip()
        if choice == "1":
            symmetric_difference_demo()
        elif choice == "2":
            view_history()
        elif choice == "3":
            clear_history()
        elif choice == "4":
            rainbow_ascii_letters(f"Goodbye, {user_name}!")
            break
        else:
            print(Fore.RED + "Invalid choice, try again.")

main()
