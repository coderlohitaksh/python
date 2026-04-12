from colorama import Fore, Style, init
import time
import os
import sys

init(autoreset=True)

# ---------- Utils ----------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def type_text(text, speed=0.03):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# ---------- Title ----------
def cinematic_title():
    clear()

    title = [
"███████╗██╗      █████╗ ███████╗██╗  ██╗",
"██╔════╝██║     ██╔══██╗██╔════╝██║  ██║",
"█████╗  ██║     ███████║███████╗███████║",
"██╔══╝  ██║     ██╔══██║╚════██║██╔══██║",
"██║     ███████╗██║  ██║███████║██║  ██║",
"╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝"
    ]

    print(Fore.BLUE)
    for line in title:
        print(line)
        time.sleep(0.1)

    print(Fore.CYAN)
    type_text("\n        FLASHCARD TERMINAL\n", 0.04)

# ---------- Loading ----------
def loading():
    print(Fore.YELLOW)
    type_text("Loading flashcard system...\n", 0.03)

    for _ in range(25):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(0.02)

    print("\n")

# ---------- Class ----------
class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word + " ( " + self.meaning + " )"

# ---------- Storage ----------
flashcards = []

# ---------- Functions ----------
def add_flashcard():
    type_text(Fore.CYAN + "\nAdd New Flashcard\n")

    word = input(Fore.YELLOW + "Enter word: ")
    meaning = input(Fore.YELLOW + "Enter meaning: ")

    flashcards.append(flashcard(word, meaning))

    type_text(Fore.GREEN + "Flashcard added successfully!")

def view_flashcards():
    type_text(Fore.CYAN + "\nYour Flashcards:\n")

    if not flashcards:
        type_text(Fore.RED + "No flashcards available!")
        return

    for i in flashcards:
        print(Fore.WHITE + "> " + str(i))
        time.sleep(0.2)

def quiz():
    if not flashcards:
        type_text(Fore.RED + "No flashcards to quiz!")
        return

    type_text(Fore.CYAN + "\nQuiz Mode\n")

    for card in flashcards:
        answer = input(Fore.YELLOW + f"What is the meaning of '{card.word}'? ")

        if answer.lower() == card.meaning.lower():
            type_text(Fore.GREEN + "Correct!")
        else:
            type_text(Fore.RED + f"Wrong! Answer: {card.meaning}")

# ---------- Menu ----------
def menu():
    print(Fore.GREEN)
    print("\n====== MENU ======")
    print("1  Add Flashcard")
    print("2  View Flashcards")
    print("3  Quiz Mode")
    print("4  Exit")
    print("==================")

# ---------- Main ----------
def main():
    cinematic_title()
    loading()

    while True:
        menu()
        choice = input(Fore.YELLOW + "Choose option: ")

        if choice == "1":
            clear()
            cinematic_title()
            add_flashcard()
            input(Fore.YELLOW + "\nPress Enter to continue...")

        elif choice == "2":
            clear()
            cinematic_title()
            view_flashcards()
            input(Fore.YELLOW + "\nPress Enter to continue...")

        elif choice == "3":
            clear()
            cinematic_title()
            quiz()
            input(Fore.YELLOW + "\nPress Enter to continue...")

        elif choice == "4":
            type_text(Fore.RED + "Exiting program...", 0.04)
            break

        else:
            type_text(Fore.RED + "Invalid option!")

# ---------- Run ----------
if __name__ == "__main__":
    main()