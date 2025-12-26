import os
import time
import shutil
import pyfiglet
from colorama import Fore, init

init(autoreset=True)

colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

SPCMcountry_code = {
    'India': '0091',
    'Australia': '0061',
    'Nepal': '00977'
}

all_countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
    "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain",
    "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
    "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
    "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada",
    "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros",
    "Congo", "Costa Rica", "Côte d'Ivoire", "Croatia", "Cuba",
    "Cyprus", "Czech Republic", "Democratic Republic of the Congo", "Denmark", "Djibouti",
    "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador",
    "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji",
    "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece",
    "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras",
    "Hungary", "Holy See - Observer State" ,"Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
    "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati",
    "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia",
    "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi",
    "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania",
    "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro",
    "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands",
    "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia",
    "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay",
    "Peru", "Philippines", "Poland", "Portugal", "Palestine — Observer State" ,"Qatar", "Romania", 
    "Russia", "Rwanda","St. Kitts and Nevis", "St. Lucia", "St. Vincent and the Grenadines", "Samoa",
    "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia",
    "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
    "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka",
    "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan",
    "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago",
    "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine",
    "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan",
    "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

def rainbow_banner(text, char_delay=0.002, line_delay=0.05):
    lines = pyfiglet.figlet_format(text, font="standard").split("\n")
    width = shutil.get_terminal_size().columns
    for line in lines:
        pad = max((width - len(line)) // 2, 0)
        print(" " * pad, end='')
        color_idx = 0
        for char in line:
            if char != " ":
                print(colors[color_idx % len(colors)] + char, end='', flush=True)
                color_idx += 1
            else:
                print(" ", end='', flush=True)
            time.sleep(char_delay)
        print()
        time.sleep(line_delay)

def rainbow_type(text, delay=0.05):
    color_idx = 0
    for c in text:
        if c != " ":
            print(colors[color_idx % len(colors)] + c, end='', flush=True)
            color_idx += 1
        else:
            print(" ", end='', flush=True)
        time.sleep(delay)
    print()

def country_code_finder():
    countries_list = list(SPCMcountry_code.keys())
    print(Fore.CYAN + "\nAvailable countries:\n")
    for idx, country in enumerate(countries_list, 1):
        color = colors[(idx-1) % len(colors)]
        print(color + f"{idx}. {country}")
    choice = input(Fore.GREEN + "\nEnter country name or number: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(countries_list):
        choice = countries_list[int(choice) - 1]
    code = SPCMcountry_code.get(choice)
    if code:
        rainbow_type(f"Country code for {choice} - {code}", delay=0.03)
    else:
        print(Fore.RED + "Country not found! Try again.")
        time.sleep(1)

def list_all_countries():
    print(Fore.CYAN + "\nAll countries in the world (A–Z):\n")
    for idx, country in enumerate(sorted(all_countries), 1):
        color = colors[(idx-1) % len(colors)]
        print(color + f"{idx}. {country}")
    input(Fore.GREEN + "\nPress Enter to return to main menu...")

def main_menu():
    menu_width = 44
    menu_items = ["Country code finder", "All countries name", "Exit"]
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        rainbow_banner("C O U N T R Y\nC O D E\nF I N D E R")
        print(Fore.CYAN + "╔" + "═" * menu_width + "╗")
        print(Fore.CYAN + "║" + "MAIN MENU".center(menu_width) + "║")
        print(Fore.CYAN + "╠" + "═" * menu_width + "╣")
        for idx, item in enumerate(menu_items, 1):
            color = colors[(idx-1) % len(colors)]
            print(Fore.CYAN + "║ " + color + f"{idx}. {item}" + " " * (menu_width - len(f"{idx}. {item}") - 1) + Fore.CYAN + "║")
        print(Fore.CYAN + "╚" + "═" * menu_width + "╝")
        choice = input(Fore.GREEN + "\nEnter your choice: ").strip()
        if choice == "1":
            country_code_finder()
            input(Fore.GREEN + "\nPress Enter to return to main menu...")
        elif choice == "2":
            list_all_countries()
        elif choice == "3":
            print(Fore.CYAN + "\nThank you for using the app ,Country Code Finder! Bye !")
            print(Fore.CYAN + "Exiting in 3 , 2 , 1")
            print(Fore.CYAN + "Exited!")
            break
        else:
            print(Fore.RED + "\nInvalid choice! Try again.\n")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
