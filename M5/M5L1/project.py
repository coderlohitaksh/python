import os
import sys
import time
import platform
import datetime
import shutil
from colorama import Fore, init
from dateutil.relativedelta import relativedelta

init(autoreset=True)

def slow_print(text, delay=0.03, color=Fore.WHITE):
    for ch in text:
        print(color + ch, end="", flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def spinner(duration=1.5):
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end = time.time() + duration
    while time.time() < end:
        for f in frames:
            print(Fore.MAGENTA + f"\rLoading...", end="", flush=True)
            time.sleep(0.05)
    print("\r" + " " * 30 + "\r", end="")

def show_banner():
    banner = """
██████╗  ██████╗  ██████╗     ██╗███╗   ██╗███████╗ ██████╗ 
██╔══██╗██╔═══██╗██╔════╝     ██║████╗  ██║██╔════╝██╔═══██╗
██║  ██║██║   ██║██║  ███╗    ██║██╔██╗ ██║█████╗  ██║   ██║
██║  ██║██║   ██║██║   ██║    ██║██║╚██╗██║██╔══╝  ██║   ██║
██████╔╝╚██████╔╝╚██████╔╝    ██║██║ ╚████║██║     ╚██████╔╝
╚═════╝  ╚═════╝  ╚═════╝     ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
"""
    width = shutil.get_terminal_size().columns
    for line in banner.splitlines():
        print(Fore.CYAN + line.center(width))
    slow_print("🐶 DOG INFO SYSTEM 🐶".center(width), 0.04, Fore.YELLOW)

class Dog:
    animal = "Dog"
    counter = 0
    ideal_weight_per_breed = {
        "Labrador Retriever": 30,
        "German Shepherd": 35,
        "Golden Retriever": 32,
        "Bulldog": 24,
        "Poodle": 20
    }

    def __init__(self, breed, color, birth_date, height_cm, weight_kg, temperament, owner):
        Dog.counter += 1
        self.dog_number = Dog.counter
        self.breed = breed
        self.color = color
        self.birth_date = birth_date
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.temperament = temperament
        self.owner = owner
        self.registered_on = datetime.datetime.now() - relativedelta(years=2)
        self.age = self.calculate_age()
        self.bmi = self.calculate_bmi()
        self.health_score = self.calculate_health_score()
        self.health_tag, self.tag_color = self.assign_health_tag()

    def calculate_age(self):
        today = datetime.date.today()
        return relativedelta(today, self.birth_date).years

    def calculate_bmi(self):
        bmi = self.weight_kg / ((self.height_cm / 100) ** 2)
        return round(bmi, 2)

    def calculate_health_score(self):
        ideal_weight = Dog.ideal_weight_per_breed.get(self.breed, 30)
        diff = abs(self.weight_kg - ideal_weight)
        score = round(max(0, 100 - diff * 5), 2)
        return score

    def assign_health_tag(self):
        if self.health_score >= 80:
            return "Healthy", Fore.GREEN
        elif self.health_score >= 50:
            return "OK", Fore.YELLOW
        else:
            return "Unhealthy", Fore.RED

    def health_bar(self, length=20):
        full_blocks = int(self.health_score / 100 * length)
        remainder_ratio = (self.health_score / 100 * length) - full_blocks
        partial_block = ''
        if remainder_ratio >= 0.75:
            partial_block = '▉'
        elif remainder_ratio >= 0.5:
            partial_block = '▊'
        elif remainder_ratio >= 0.25:
            partial_block = '▌'
        empty_blocks = length - full_blocks - (1 if partial_block else 0)
        color = Fore.GREEN if self.health_score >= 80 else Fore.YELLOW if self.health_score >= 50 else Fore.RED
        bar = color + '█' * full_blocks + partial_block + Fore.WHITE + ' ' * empty_blocks
        return bar

    def display(self):
        slow_print(f"\n🐾 DOG {self.dog_number} DETAILS", 0.03, Fore.GREEN)
        print("-" * 60)
        print(Fore.CYAN + f"Animal Type     : {Dog.animal}")
        print(Fore.WHITE + f"Breed           : {self.breed}")
        print(Fore.WHITE + f"Color           : {self.color}")
        print(Fore.WHITE + f"Birthday        : {self.birth_date.strftime('%d-%m-%Y')}")
        print(Fore.WHITE + f"Age             : {self.age} years")
        print(Fore.WHITE + f"Height          : {self.height_cm} cm")
        print(Fore.WHITE + f"Weight          : {self.weight_kg} kg")
        print(Fore.WHITE + f"Temperament     : {self.temperament}")
        print(Fore.WHITE + f"Owner Name      : {self.owner}")
        print(Fore.YELLOW + f"BMI             : {self.bmi}")
        print(Fore.YELLOW + f"Health Score    : {self.health_score}/100 " +
              self.tag_color + f"({self.health_tag})")
        print(Fore.YELLOW + f"Health Bar      : [{self.health_bar()}]")
        print(Fore.BLUE + f"Registered On   : {self.registered_on.strftime('%d-%m-%Y %H:%M:%S')}")
        print("-" * 60)

def main():
    clear_screen()
    show_banner()
    time.sleep(0.5)
    slow_print("\nInitializing dog records...", 0.04, Fore.CYAN)
    spinner()

    dogs = [
        Dog("Labrador Retriever", "Golden", datetime.date(2020, 1, 15), 60, 30, "Friendly and Active", "Rahul"),
        Dog("German Shepherd", "Black and Tan", datetime.date(2019, 6, 10), 65, 35, "Alert and Intelligent", "Ananya"),
        Dog("Golden Retriever", "Cream", datetime.date(2021, 3, 22), 58, 29, "Gentle and Loyal", "Amit"),
        Dog("Bulldog", "White and Brown", datetime.date(2018, 9, 5), 40, 24, "Calm and Brave", "Sneha"),
        Dog("Poodle", "White", datetime.date(2022, 11, 30), 45, 20, "Smart and Energetic", "Rohit")
    ]

    for dog in dogs:
        dog.display()
        time.sleep(0.4)

    slow_print("\n📊 SYSTEM INFORMATION", 0.04, Fore.CYAN)
    slow_print(f"Platform        : {platform.system()}", 0.02)
    slow_print(f"Python Version  : {sys.version.split()[0]}", 0.02)
    slow_print(f"Total Dogs      : {len(dogs)}", 0.02)
    slow_print("\n✅ Dog information displayed successfully", 0.04, Fore.GREEN)
    slow_print("🐾 Thank you for using Dog Info System 🐾", 0.04, Fore.YELLOW)

if __name__ == "__main__":
    main()
