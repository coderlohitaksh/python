import pyfiglet
from colorama import Fore, init
import random
import time

init(autoreset=True)

def rainbow_text(text):
    ascii_banner = pyfiglet.figlet_format(text, font="slant")
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    for i, line in enumerate(ascii_banner.splitlines()):
        print(colors[i % len(colors)] + line)

def pause(seconds=1):
    time.sleep(seconds)

def show_rules():
    rainbow_text("Mystical Library of Codes")
    print(Fore.YELLOW + "\nWelcome, Adventurer!")
    print(Fore.CYAN + """
Rules & How to Play:

1. Collect Artifacts:
   - Add artifacts with integer powers.
   - Powers affect your battle strength.

2. View Inventory:
   - Check what artifacts you have collected.

3. Check Artifact Power Frequency:
   - See how many times a specific power appears.
   - Certain power combinations can unlock SECRET ENDINGS!

4. Add or Remove Artifacts:
   - Customize your inventory anytime.

5. Explore Random Events / Battles:
   - Face Guardians in battle.
   - Win battles to gain gold.
   - Random events may add or remove artifacts.

6. Secret Endings:
   - Unlock special endings by collecting artifacts with certain power patterns:
     * Three of the same power → Codex of Triads
     * Four of the same power → Quadrant Relic
     * All powers the same (≥5) → Master of Codes

7. Exit Adventure:
   - Choose this to end your journey.
""")
    input(Fore.MAGENTA + "Press Enter to start your adventure...")
    pause(1)

def create_inventory():
    inventory = {}
    print(Fore.YELLOW + "\nAdd artifacts with integer powers. Type 'done' when finished.\n")
    while True:
        key = input(Fore.CYAN + "Artifact name: ")
        if key.lower() == 'done':
            break
        value = input(Fore.CYAN + "Artifact power (integer): ")
        try:
            value = int(value)
            inventory[key] = value
            print(Fore.GREEN + f"'{key}' with power {value} added!")
        except ValueError:
            print(Fore.RED + "Power must be an integer!")
    return inventory

def show_inventory(inventory):
    if not inventory:
        print(Fore.RED + "Your inventory is empty!")
    else:
        print(Fore.MAGENTA + "\nCurrent Inventory:")
        for k, v in inventory.items():
            print(f"{Fore.YELLOW}{k}: {Fore.CYAN}{v}")

def check_frequency(inventory):
    if not inventory:
        print(Fore.RED + "Inventory empty! Collect artifacts first.")
        return 0
    while True:
        val = input(Fore.YELLOW + "\nEnter power to check frequency: ")
        try:
            val = int(val)
            break
        except ValueError:
            print(Fore.RED + "Enter a valid integer!")
    freq = list(inventory.values()).count(val)
    print(Fore.CYAN + f"The power {val} appears {freq} time(s).")
    return freq

def battle(inventory):
    if not inventory:
        print(Fore.RED + "No artifacts to fight with! Collect some first.")
        return
    print(Fore.YELLOW + "\nA wild Guardian appears!")
    pause(1)
    enemy_power = random.randint(5, 20)
    print(Fore.RED + f"Guardian's strength: {enemy_power}")
    pause(1)
    player_power = sum(inventory.values())
    freq_bonus = sum(list(inventory.values()).count(v) for v in inventory.values() if list(inventory.values()).count(v) > 1)
    player_power += freq_bonus
    print(Fore.CYAN + f"Your artifact power plus frequency bonus: {player_power}")
    pause(1)
    if player_power >= enemy_power:
        print(Fore.GREEN + "You defeated the Guardian!")
        treasure = random.randint(10, 25)
        print(Fore.YELLOW + f"You gained {treasure} gold!")
        return True
    else:
        print(Fore.RED + "The Guardian overpowered you. Retreat!")
        return False

def check_secret_ending(inventory):
    powers = list(inventory.values())
    unique_counts = set(powers.count(v) for v in powers)
    if 3 in unique_counts:
        rainbow_text("SECRET ENDING UNLOCKED!")
        print(Fore.MAGENTA + "The Codex of Triads awakens, granting you ultimate knowledge!")
        pause(2)
    elif 4 in unique_counts:
        rainbow_text("SECRET ENDING UNLOCKED!")
        print(Fore.MAGENTA + "The Quadrant Relic shines, blessing your artifacts with infinite power!")
        pause(2)
    elif len(powers) >= 5 and len(set(powers)) == 1:
        rainbow_text("SECRET ENDING UNLOCKED!")
        print(Fore.MAGENTA + "All artifacts resonate in perfect harmony. You ascend as a Master of Codes!")
        pause(2)

def random_event(inventory):
    event_type = random.choice(["artifact_gain", "artifact_loss", "challenge"])
    if event_type == "artifact_gain":
        new_artifact = f"Artifact_{random.randint(1,100)}"
        power = random.randint(1,10)
        inventory[new_artifact] = power
        print(Fore.GREEN + f"\nYou discovered a new artifact: {new_artifact} with power {power}!")
    elif event_type == "artifact_loss" and inventory:
        lost_artifact = random.choice(list(inventory.keys()))
        del inventory[lost_artifact]
        print(Fore.RED + f"\nOh no! The artifact {lost_artifact} vanished!")
    else:
        print(Fore.CYAN + "\nA mystical challenge appears!")
        battle(inventory)
    check_secret_ending(inventory)

def adventure_menu():
    inventory = {}
    show_rules()
    while True:
        print(Fore.BLUE + "\n" + "-" * 50)
        print(Fore.MAGENTA + "Mystical Library of Codes - Adventure Menu")
        print(Fore.BLUE + "-" * 50)
        print(Fore.YELLOW + "1. Collect Artifacts")
        print(Fore.YELLOW + "2. View Inventory")
        print(Fore.YELLOW + "3. Check Artifact Power Frequency")
        print(Fore.YELLOW + "4. Add Artifact")
        print(Fore.YELLOW + "5. Remove Artifact")
        print(Fore.YELLOW + "6. Explore Random Event / Battle")
        print(Fore.YELLOW + "7. Exit Adventure")
        choice = input(Fore.CYAN + "\nChoose your action (1-7): ")

        if choice == '1':
            new_items = create_inventory()
            inventory.update(new_items)
        elif choice == '2':
            show_inventory(inventory)
        elif choice == '3':
            check_frequency(inventory)
            check_secret_ending(inventory)
        elif choice == '4':
            key = input(Fore.CYAN + "Artifact name: ")
            value = input(Fore.CYAN + "Artifact power (integer): ")
            try:
                value = int(value)
                inventory[key] = value
                print(Fore.GREEN + f"'{key}' added!")
            except ValueError:
                print(Fore.RED + "Power must be integer!")
            check_secret_ending(inventory)
        elif choice == '5':
            key = input(Fore.CYAN + "Artifact to remove: ")
            if key in inventory:
                del inventory[key]
                print(Fore.GREEN + f"'{key}' removed!")
            else:
                print(Fore.RED + "Artifact not found!")
        elif choice == '6':
            random_event(inventory)
        elif choice == '7':
            rainbow_text("Farewell, Adventurer!")
            break
        else:
            print(Fore.RED + "Invalid choice! Try again.")

adventure_menu()

