import time
import calendar
import shutil
import json
import os
import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)
COLORS = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def rainbow_big_text(text):
    banner = pyfiglet.figlet_format(text, font="standard")
    lines = banner.split("\n")
    width = shutil.get_terminal_size().columns
    max_len = max(len(line) for line in lines)
    pad = max((width - max_len) // 2, 0)
    idx = 0
    for line in lines:
        out = ""
        for ch in line:
            if ch != " ":
                out += COLORS[idx % len(COLORS)] + ch
                idx += 1
            else:
                out += " "
        print(" " * pad + out)

def spinner_loading(text="Loading...", duration=3):
    spinner = ["⠁","⠃","⠇","⠧","⠷","⠿","⠟","⠯","⠷","⠾","⠽","⠻"]
    width = shutil.get_terminal_size().columns
    msg = text + " "
    for _ in range(duration * 4):
        for frame in spinner:
            line = msg + frame
            pad = (width - len(line)) // 2
            print(" " * pad + Fore.CYAN + line, end="\r")
            time.sleep(0.09)
    print(" " * width, end="\r")

def progress_bar(text="Loading"):
    width = shutil.get_terminal_size().columns
    for i in range(0, 101, 2):
        bar = "#" * (i // 2) + "-" * ((100 - i) // 2)
        line = f"{text}: [{bar}] {i}%"
        pad = (width - len(line)) // 2
        print(" " * pad + Fore.MAGENTA + line, end="\r")
        time.sleep(0.04)
    print(" " * width, end="\r")

def hotel_cost(n):
    return 140 * n

def plane_cost(city):
    prices = {"Charlotte":180, "Tampa":220, "Pittsburgh":222, "Los Angeles":475}
    return prices.get(city, 0)

def car_cost(days):
    if days >= 7:
        return 40 * days - 50
    if days >= 3:
        return 40 * days - 20
    return 40 * days

def trip_cost(city, days, spend):
    return hotel_cost(days) + car_cost(days) + plane_cost(city) + spend

def save_trip(data):
    if not os.path.exists("trip_history.json"):
        with open("trip_history.json", "w") as f:
            f.write("[]")
    with open("trip_history.json", "r+") as f:
        hist = json.load(f)
        hist.append(data)
        f.seek(0)
        json.dump(hist, f, indent=4)

def load_history():
    if not os.path.exists("trip_history.json"):
        return []
    with open("trip_history.json", "r") as f:
        return json.load(f)

def show_trip_history():
    hist = load_history()
    if not hist:
        print(Fore.RED + "\nNo trip history found!\n")
        return
    spinner_loading("Retrieving trips", 2)
    print(Fore.YELLOW + "\n=== TRIP HISTORY ===\n")
    for i, t in enumerate(hist, 1):
        print(Fore.CYAN + f"{i}. {t['city']} | {t['days']} days | Cost: {t['total']}")

def delete_all_history():
    hist = load_history()
    if not hist:
        print(Fore.RED + "\nNo trip history to delete!\n")
        return
    confirm = input(Fore.RED + "\nAre you sure you want to delete ALL trip history? (yes/no): ").lower()
    if confirm == "yes":
        spinner_loading("Deleting history", 2)
        with open("trip_history.json", "w") as f:
            f.write("[]")
        print(Fore.GREEN + "\nAll trip history deleted!\n")
    else:
        print(Fore.YELLOW + "\nCancelled.\n")

def delete_specific_trip():
    hist = load_history()
    if not hist:
        print(Fore.RED + "\nNo trips to delete!\n")
        return
    show_trip_history()
    try:
        index = int(input(Fore.YELLOW + "\nEnter the trip number to delete: "))
        if 1 <= index <= len(hist):
            spinner_loading("Deleting trip", 2)
            hist.pop(index - 1)
            with open("trip_history.json", "w") as f:
                json.dump(hist, f, indent=4)
            print(Fore.GREEN + "\nTrip deleted successfully!\n")
        else:
            print(Fore.RED + "\nInvalid trip number!\n")
    except:
        print(Fore.RED + "\nInvalid input!\n")

def plan_trip():
    print(Fore.CYAN + "\nCities: Charlotte, Tampa, Pittsburgh, Los Angeles\n")
    city = input(Fore.YELLOW + "Enter destination: ").strip()
    spinner_loading("Checking availability", 2)
    if plane_cost(city) == 0:
        print(Fore.RED + "\nInvalid city!\n")
        return
    try:
        days = int(input(Fore.YELLOW + "Enter number of days: "))
        spend = float(input(Fore.YELLOW + "Enter spending money: "))
    except:
        print(Fore.RED + "\nInvalid numeric value!\n")
        return
    spinner_loading("Calculating cost", 3)
    total = trip_cost(city, days, spend)
    print(Fore.GREEN + f"\nTotal Trip Cost → {total}\n")
    progress_bar("Saving trip")
    save_trip({"city":city,"days":days,"spending":spend,"total":total})
    print(Fore.CYAN + "\nTrip saved successfully!\n")

def show_calendar():
    try:
        year = int(input(Fore.YELLOW + "Enter a year: "))
    except:
        print(Fore.RED + "\nInvalid year!\n")
        return
    progress_bar("Preparing calendar")
    print(Fore.GREEN + f"\n=== Calendar for {year} ===\n")
    print(calendar.calendar(year))

def show_time():
    spinner_loading("Fetching time", 2)
    print(Fore.CYAN + "\nCurrent Time:\n")
    print(Fore.GREEN + time.ctime())

def menu():
    rainbow_big_text("TRIP  CALCULATOR")
    while True:
        print(Fore.MAGENTA + """
==============================
            MAIN MENU
==============================
1. Plan a New Trip
2. View Trip History
3. Delete All Trip History
4. Delete Specific Trip
5. Display Calendar
6. Show Current Time
7. Exit
""")
        choice = input(Fore.YELLOW + "Enter choice: ")
        if choice == "1":
            progress_bar("Opening Planner")
            plan_trip()
        elif choice == "2":
            show_trip_history()
        elif choice == "3":
            delete_all_history()
        elif choice == "4":
            delete_specific_trip()
        elif choice == "5":
            show_calendar()
        elif choice == "6":
            show_time()
        elif choice == "7":
            spinner_loading("Closing Program", 2)
            print(Fore.CYAN + "\nGoodbye!\n")
            break
        else:
            print(Fore.RED + "\nInvalid choice!\n")

menu()
