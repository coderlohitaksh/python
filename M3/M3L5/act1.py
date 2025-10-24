import sys
from colorama import Fore, Style
import shutil
import pyfiglet

colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def rainbow_big_text(text):
    ascii_banner = pyfiglet.figlet_format(text)
    lines = ascii_banner.split("\n")
    terminal_width = shutil.get_terminal_size().columns

    for line in lines:
        colored_line = ""
        color_index = 0
        for char in line:
            if char != " ":
                colored_line += colors[color_index % len(colors)] + char
                color_index += 1
            else:
                colored_line += " "
        print(colored_line.center(terminal_width))

rainbow_big_text("G U E S S I N G \n N U M B E R ")
import random

playing = True
num = str(random.randint(10 , 20))

print("I will generate a number from 10 to 20 and you have to guess the number one digit at a time.")
print("The game ends ehen you get one hero !!")

while playing:
    guess = int(input("Give me your best guess \n"))
    if num == guess :
        print("You win the game !!")
        print("The number was ",num)
        print("So you win the game !")
    
    else:
        print("Your guess isn't quite right , try again .")
