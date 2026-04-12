import random
import time
from rich.console import Console
from rich.text import Text

console = Console()


# ⌨️ Typing effect (SAFE + WORKS WITH COLORS)
def type_effect(text, speed=0.02):
    plain = text.plain if isinstance(text, Text) else str(text)

    for char in plain:
        console.print(char, end="")
        time.sleep(speed)

    console.print()


class FruitQuiz:

    def __init__(self):
        self.fruits = {
            'apple': 'red',
            'orange': 'orange',
            'watermelon': 'green',
            'banana': 'yellow',
            'grapes': 'purple',
            'mango': 'yellow',
            'strawberry': 'red',
            'blueberry': 'blue',
            'pineapple': 'brown',
            'lemon': 'yellow'
        }

        self.score = 0
        self.total_questions = 0

    # 📜 Rules
    def show_rules(self):
        type_effect(Text("📜 Rules of the Game:", style="cyan"))
        type_effect(Text("1. You will be given a fruit name.", style="yellow"))
        type_effect(Text("2. You must guess its color.", style="yellow"))
        type_effect(Text("3. Each correct answer gives you 1 point.", style="yellow"))
        type_effect(Text("4. Type 'exit' anytime to quit.\n", style="yellow"))

    # 💡 Hint
    def get_hint(self, color):
        return Text(f"Hint: The color starts with '{color[0].upper()}'", style="cyan")

    # 📊 Score
    def show_score(self):
        type_effect(Text("\n📊 Quiz Summary:", style="cyan"))
        type_effect(Text(f"Total Questions: {self.total_questions}", style="yellow"))
        type_effect(Text(f"Correct Answers: {self.score}", style="green"))

        if self.total_questions > 0:
            percentage = (self.score / self.total_questions) * 100
            type_effect(Text(f"Score Percentage: {percentage:.2f}%", style="magenta"))

        type_effect(Text("Thank you for playing! 🎮", style="green"))

    # 🎚️ Difficulty
    def select_difficulty(self):
        type_effect(Text("\nChoose Difficulty Level:", style="magenta"))
        type_effect(Text("1. Easy (Hint available)", style="yellow"))
        type_effect(Text("2. Medium (Hint available)", style="yellow"))
        type_effect(Text("3. Hard (No hints)", style="yellow"))

        while True:
            try:
                choice = int(input("Enter choice (1/2/3): "))
                if choice in [1, 2, 3]:
                    return choice
                else:
                    console.print("[red]Invalid choice. Try again.[/red]")
            except ValueError:
                console.print("[red]Please enter a valid number.[/red]")

    # 🎮 Game loop
    def start_quiz(self):
        type_effect(Text("🎮 Starting Fruit Quiz Game!", style="magenta"))
        self.show_rules()

        difficulty = self.select_difficulty()

        while True:
            fruit, color = random.choice(list(self.fruits.items()))

            type_effect(Text(f"\nWhat is the color of {fruit}?", style="yellow"))

            if difficulty in [1, 2]:
                type_effect(self.get_hint(color))

            user_input = input("Your answer (or type 'exit'): ").strip().lower()

            if user_input == 'exit':
                break

            self.total_questions += 1

            if user_input == color:
                type_effect(Text("Correct! 🎉", style="green"))
                self.score += 1
            else:
                type_effect(Text(f"Wrong! Correct answer: {color}", style="red"))

            try:
                option = int(input("Enter 0 to continue or 1 to exit: "))
                if option == 1:
                    break
            except ValueError:
                console.print("[red]Invalid input, continuing game...[/red]")

        self.show_score()


# 🚀 Main Program
def main():
    type_effect(Text("🍎 Welcome to Fruit Quiz 🍌", style="green"))

    quiz = FruitQuiz()
    quiz.start_quiz()


if __name__ == "__main__":
    main()