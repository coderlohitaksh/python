from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
from colorama import Fore, Style, init
import random
import time

init(autoreset=True)


class Animal(ABC):
    @abstractmethod
    def move(self) -> str:
        pass


@dataclass
class Creature(Animal):
    name: str
    actions: List[str]

    def move(self) -> str:
        return random.choice(self.actions)


def animate(text: str):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(0.01)
    print()


def show(animals: List[Creature]):
    colors = [Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.BLUE]
    for a in animals:
        msg = f"{a.name:<10} → {a.move()}"
        animate(random.choice(colors) + msg + Style.RESET_ALL)
        time.sleep(0.08)


if __name__ == "__main__":
    animals = [
        Creature("Human", ["walks 🚶", "runs 🏃"]),
        Creature("Snake", ["crawls 🐍"]),
        Creature("Dog", ["barks 🐶", "runs 🐕"]),
        Creature("Lion", ["roars 🦁"]),
        Creature("Cat", ["sneaks 🐈"]),
        Creature("Elephant", ["walks 🐘"]),
        Creature("Tiger", ["stalks 🐅"]),
        Creature("Bird", ["flies 🐦"]),
        Creature("Fish", ["swims 🐟"]),
        Creature("Frog", ["jumps 🐸"]),
        Creature("Kangaroo", ["hops 🦘"]),
        Creature("Horse", ["gallops 🐎"]),
        Creature("Monkey", ["climbs 🐒"]),
        Creature("Penguin", ["waddles 🐧"]),
        Creature("Dolphin", ["dives 🐬"]),
        Creature("Eagle", ["soars 🦅"]),
        Creature("Bear", ["lumbers 🐻"]),
        Creature("Wolf", ["hunts 🐺"]),
        Creature("Cheetah", ["sprints ⚡🐆"]),
        Creature("Turtle", ["moves slowly 🐢"])
    ]

    print(Fore.WHITE + "\n🌍 Animal Simulator 🌍\n")
    show(animals)