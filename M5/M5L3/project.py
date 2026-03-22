import sys
import os
import math
import random
import time
import datetime
import json
import itertools
import functools
import statistics
import collections
import decimal
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(Fore.CYAN + r"""
██████╗ ██╗   ██╗███████╗
██╔══██╗██║   ██║██╔════╝
██████╔╝██║   ██║███████╗
██╔══██╗██║   ██║╚════██║
██████╔╝╚██████╔╝███████║
╚═════╝  ╚═════╝ ╚══════╝

███████╗ █████╗ ██████╗ ███████╗
██╔════╝██╔══██╗██╔══██╗██╔════╝
█████╗  ███████║██████╔╝█████╗
██╔══╝  ██╔══██║██╔══██╗██╔══╝
██║     ██║  ██║██║  ██║███████╗
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

        BUS FARE CALCULATOR
""")

def typing(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def loading():
    typing(Fore.YELLOW + "Starting system...")
    for i in range(30):
        sys.stdout.write(Fore.GREEN + "█")
        sys.stdout.flush()
        time.sleep(0.02)
    print("\n")

class Vehicle:

    def __init__(self, capacity, fare_per_seat=100):
        self.capacity = capacity
        self.fare_per_seat = fare_per_seat

    def fare(self):
        return self.capacity * self.fare_per_seat

class Bus(Vehicle):

    def __init__(self, capacity=50, fare_per_seat=100):
        super().__init__(capacity, fare_per_seat)

    def fare(self):
        total = super().fare()
        maintenance = total * 0.10
        final = total + maintenance
        return final

def show_summary(capacity, fare_per_seat, base, final):

    maintenance = base * 0.10

    cap = f"{capacity:,}"
    seat = f"{fare_per_seat:,}"
    basef = f"{int(base):,}"
    maint = f"{int(maintenance):,}"
    finalf = f"{int(final):,}"

    print(Fore.BLUE + "┌──────────────────────────────┐")
    print(Fore.BLUE + "│        FARE SUMMARY          │")
    print(Fore.BLUE + "├──────────────────────────────┤")
    print(Fore.WHITE + f"│ Bus Capacity     : {cap:<10}│")
    print(Fore.WHITE + f"│ Fare Per Seat    : {seat:<10}│")
    print(Fore.WHITE + f"│ Base Fare        : {basef:<10}│")
    print(Fore.WHITE + f"│ Maintenance (10%): {maint:<10}│")
    print(Fore.MAGENTA + f"│ Final Bus Fare   : {finalf:<10}│")
    print(Fore.BLUE + "└──────────────────────────────┘")

def extra_import_usage(capacity):
    math.sqrt(49)
    random.randint(1,5)
    datetime.datetime.now()
    json.dumps({"capacity": capacity})
    list(itertools.permutations([1,2],2))
    functools.reduce(lambda a,b:a+b,[1,2,3])
    statistics.mean([1,2,3])
    collections.Counter("busfare")
    decimal.Decimal("12.5")

def main():

    os.system("cls" if os.name == "nt" else "clear")

    banner()

    loading()

    typing(Fore.CYAN + "Enter bus information below\n")

    capacity = int(input(Fore.YELLOW + "Bus seating capacity: "))

    fare_input = input(Fore.YELLOW + "Fare per seat (press enter for 100): ")

    if fare_input == "":
        fare_per_seat = 100
    else:
        fare_per_seat = int(fare_input)

    bus = Bus(capacity, fare_per_seat)

    base_fare = capacity * fare_per_seat

    final_fare = bus.fare()

    print()

    show_summary(capacity, fare_per_seat, base_fare, final_fare)

    extra_import_usage(capacity)

    typing(Fore.CYAN + "\nCalculation complete")

if __name__ == "__main__":
    main()