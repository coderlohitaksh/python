import os
import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow(text, color=Fore.WHITE, delay=0.02):
    for i in text:
        sys.stdout.write(color + i)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def line():
    print(Fore.BLUE + "-" * 50)

class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display(self):
        line()
        slow("PERSON INFORMATION", Fore.CYAN, 0.03)
        line()
        slow(f"Name      : {self.name}", Fore.GREEN)
        slow(f"ID Number : {self.id_number}", Fore.YELLOW)
        line()

class Employee(Person):
    def __init__(self, name, id_number, salary, post):
        super().__init__(name, id_number)
        self.salary = salary
        self.post = post

    def extra(self):
        slow("EMPLOYEE DETAILS", Fore.MAGENTA, 0.03)
        line()
        slow(f"Post   : {self.post}", Fore.BLUE)
        slow(f"Salary : {self.salary}", Fore.RED)
        line()

clear()

slow("EMPLOYEE MANAGEMENT PROGRAM", Fore.CYAN, 0.04)
line()

name = input(Fore.GREEN + "Enter Name: ")
id_number = input(Fore.YELLOW + "Enter ID Number: ")
salary = input(Fore.RED + "Enter Salary per Annum: ")
post = input(Fore.BLUE + "Enter Post: ")

emp = Employee(name, id_number, salary, post)

clear()
slow("PROCESSING DATA...", Fore.CYAN, 0.05)
time.sleep(1)

emp.display()
emp.extra()

slow("PROGRAM COMPLETE", Fore.GREEN, 0.04)
print(Style.BRIGHT + "Thank You")