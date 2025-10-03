import time
import sys
import shutil
from colorama import Fore, Style, init
import pyfiglet
init(autoreset=True)

money_bag = "💰"
shop = "🏪"
person = "🧑"
arrow = "➡️"
check = "✅"
cross = "❌"
sparkle = "✨"
story_end = "🎉"

colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def type_text(text, color=Fore.WHITE, delay=0.05):
    terminal_width = shutil.get_terminal_size().columns
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()

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

type_text(f"\n{person} Vishal wakes up and decides to buy some household items {shop}...\n", Fore.CYAN, 0.07)
time.sleep(1)

while True:
    try:
        bill = float(input(Fore.YELLOW + f"{arrow}  Enter the total bill amount ($): " + Style.RESET_ALL))
        paid = float(input(Fore.YELLOW + f"{arrow}  Enter the amount Vishal paid ($): " + Style.RESET_ALL))
        break
    except ValueError:
        type_text(f"{cross} Please enter valid numbers!", Fore.RED, 0.07)

time.sleep(1)
type_text("\nCalculating change... " + sparkle, Fore.MAGENTA, 0.1)
time.sleep(1)

while paid < bill:
    type_text(f"\n{cross} Uh oh! Vishal didn't pay enough.", Fore.RED, 0.07)
    type_text(f"He still owes ${bill - paid:.2f} {money_bag}\n", Fore.RED, 0.07)
    additional = float(input(Fore.YELLOW + f"{arrow}  Enter additional amount to pay: " + Style.RESET_ALL))
    paid += additional

return_money = paid - bill
type_text(f"\n{check} The total bill was ${bill:.2f}", Fore.GREEN, 0.07)
type_text(f"{person} Vishal paid ${paid:.2f}", Fore.BLUE, 0.07)
type_text(f"{shop} The shopkeeper should return ${return_money:.2f} {money_bag}\n", Fore.MAGENTA, 0.07)

time.sleep(1)
type_text(f"{story_end} Story complete! Thanks for playing! {story_end}\n", Fore.CYAN, 0.09)
rainbow_big_text("T H E     E N D")
