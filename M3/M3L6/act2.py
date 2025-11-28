import time
import shutil
import pyfiglet
import random
from colorama import init, Fore
init(autoreset=True)

colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
def rainbow_big_text(text):
    """Print big centered rainbow ASCII text"""
    terminal_width = shutil.get_terminal_size().columns

    ascii_banner = pyfiglet.figlet_format(text)
    lines = ascii_banner.split("\n")

    for line in lines:
        centered_line = line.center(terminal_width)

        colored_line = ""
        color_index = 0
        for char in centered_line:
            if char != " ":
                colored_line += colors[color_index % len(colors)] + char
                color_index += 1
            else:
                colored_line += " "
        print(colored_line)


def getRandomDate(startDate, endDate):
    """Return a random date between startDate and endDate (MM/DD/YYYY)"""
    print("Printing random date between", startDate, "and", endDate)
    dateFormat = '%m/%d/%Y'

    starttime = time.mktime(time.strptime(startDate, dateFormat))
    endtime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = starttime + random.random() * (endtime - starttime)

    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

rainbow_big_text("R A N D O M\nD A T E\nA N D\nT I M E")

print("Random Date = ", getRandomDate("1/1/2020", "12/12/2024"))
