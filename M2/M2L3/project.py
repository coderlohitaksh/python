import random
import time
import os
from colorama import init, Fore
from emoji import emojize

init( autoreset = True )

HIGHSCORE_FILE = "word_highscore.txt"

word_list = [
    "apple", "banana", "cat", "dog", "elephant", "flower", "giraffe", "hat",
    "ice", "jelly", "kite", "lion", "moon", "nest", "orange", "pencil", "queen",
    "rain", "star", "tree", "umbrella", "violin", "whale", "xray", "yarn", "zebra"
]

def play_game():
    score = 0
    rounds = 3

    print(Fore.CYAN + emojize("\n👋 Welcome to the Reverse EVERYTHING Game!"))
    print("You'll see 6 words. Type them in REVERSE order!")
    input(Fore.YELLOW + "Press ENTER when you're ready...")

    start = time.time()

    for i in range(1, rounds + 1):
        words = random.sample(word_list, 6)
        correct = ' '.join(words[::-1])
        
        print(Fore.MAGENTA + f"\nRound {i} 📝")
        print(Fore.GREEN + f"Words: {' '.join(words)}")
        answer = input(Fore.WHITE + "Type in reverse order: ").strip().lower()

        if answer == correct:
            print(Fore.GREEN + emojize("✅ Excellent!"))
            score += 1
        else:
            print(Fore.RED + emojize("❌ Not quite!"))
            print(Fore.YELLOW + f"The correct answer was: {correct}")

    end = time.time()
    total_time = round(end - start, 2)

    print(Fore.CYAN + f"\n🎯 Your Score: {score}/{rounds}")
    print(Fore.CYAN + f"⏱️ Time: {total_time} seconds")

    print(Fore.CYAN + emojize("Thanks for playing! 😊"))

while True:
    play_game()
    again = input(Fore.BLUE + "\nDo you want to play again? (y/n): ").lower()
    if again != 'y':
        print(Fore.MAGENTA + emojize("Bye-bye! 👋 Keep having fun!"))
        break
