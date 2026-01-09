from colorama import Fore, init
import random
import time
import shutil

init(autoreset=True)

def intro():
    name = input(Fore.CYAN + "What is your name: ")
    print(Fore.GREEN + f"\nHello {name}! 🧠")
    print("Welcome to the Number Guessing Game!\n")
    time.sleep(1)
    return name

def difficulty_box():
    term_width = shutil.get_terminal_size().columns

    box_lines = [
        "╔════════════════════════════════════╗",
        "║        SELECT DIFFICULTY           ║",
        "╠════════════════════════════════════╣",
        "║  1. Easy   | 1 to 50   | 10 tries  ║",
        "║  2. Medium | 1 to 100  | 7 tries   ║",
        "║  3. Hard   | 1 to 200  | 5 tries   ║",
        "╚════════════════════════════════════╝"
    ]

    for line in box_lines:
        print(Fore.YELLOW + line.center(term_width))

    while True:
        choice = input("\nEnter 1, 2, or 3: ")
        if choice == "1":
            return 50, 10
        elif choice == "2":
            return 100, 7
        elif choice == "3":
            return 200, 5
        else:
            print(Fore.RED + "Invalid choice. Try again.")

def play_game(name, max_number, max_attempts):
    number = random.randint(1, max_number)
    attempts = 0

    print(Fore.CYAN + f"\nI am thinking of a number between 1 and {max_number}")
    print(f"You have {max_attempts} attempts\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > max_number:
                print(Fore.RED + "Out of range!")
                continue

            if guess < number:
                print(Fore.BLUE + "Too low!")
            elif guess > number:
                print(Fore.MAGENTA + "Too high!")
            else:
                print(Fore.GREEN + f"\n🎉 Congrats {name}! You guessed it in {attempts} attempts!")
                return

        except ValueError:
            print(Fore.RED + "That is not a number!")

        print(f"Attempts left: {max_attempts - attempts}\n")
        time.sleep(0.5)

    print(Fore.RED + f"\nGame Over 😢 The number was {number}")

def main():
    name = intro()
    max_number, max_attempts = difficulty_box()
    play_game(name, max_number, max_attempts)

main()
