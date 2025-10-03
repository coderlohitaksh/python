
import time
import pyfiglet
from colorama import init, Fore
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

def shutdown():
    while True:
        user_input = input(Fore.CYAN + "Do you want to shut down the system? (yes/no): ").strip().lower()
        
        if user_input == "yes":
            rainbow_big_text("S H U T D O W N\nP R O G R A M")
            print(Fore.GREEN + "\nShutting down in 3 seconds...\n")
            
            for i in range(3, 0, -1):
                color = colors[(3 - i) % len(colors)]
                print(color + f"{i}...")
                time.sleep(1)

            print(Fore.RED + "💀 System turned off successfully.")
            break

        elif user_input == "no":
            rainbow_big_text("A B O R T\nS H U T D O W N")
            print(Fore.YELLOW + "Shutdown aborted.")
            break

        else:
            rainbow_big_text("I N V A L I D\nI N P U T")
            print(Fore.RED + "❌ Invalid input. Please enter 'yes' or 'no'.")

shutdown()
