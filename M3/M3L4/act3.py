import pyfiglet
from colorama import init, Fore
import time

init(autoreset=True)

colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def rainbow_big_text(text):
    """Print big rainbow ASCII text"""
    ascii_banner = pyfiglet.figlet_format(text)
    lines = ascii_banner.split("\n")

    for line in lines:
        colored_line = ""
        color_index = 0
        for char in line:
            if char != " ":
                colored_line += colors[color_index % len(colors)] + char
                color_index += 1
            else:
                colored_line += " "
        print(colored_line)
        
rainbow_big_text("B Y E   B Y E\nP R O G R A M")

while True:
    try:
        abc = int(input(Fore.GREEN + "Enter a number: "))
        if abc % 2 == 0:
            while True:  # Infinite loop for bye message
                for i, char in enumerate("🎉🎀🎈------ Bye bye, see you soon ------🎈🎀🎉"): 
                    print(colors[i % len(colors)] + char, end="")
                print()
                time.sleep(0.5)
        else:
            print(Fore.CYAN + "That's an odd number, try again!")
    except ValueError:
        print(Fore.RED + "Invalid input, please enter a number.")
