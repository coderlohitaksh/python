from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
from colorama import Fore, Style, init
import time
import random

init(autoreset=True)


class Country(ABC):
    @abstractmethod
    def describe(self) -> List[str]:
        pass


@dataclass
class Nation(Country):
    name: str
    flag: str
    capital: str
    language: str
    status: str

    def describe(self) -> List[str]:
        return [
            f"{self.flag} Capital: {self.capital}",
            f"{self.flag} Language: {self.language}",
            f"{self.flag} Type: {self.status}"
        ]


def animate(text: str):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(0.01)
    print()


def show(countries: List[Nation]):
    colors = [Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.BLUE]

    for c in countries:
        animate(Fore.WHITE + f"\n🌍 {c.name} {c.flag} 🌍" + Style.RESET_ALL)
        time.sleep(0.1)

        for line in c.describe():
            animate(random.choice(colors) + "  → " + line + Style.RESET_ALL)
            time.sleep(0.05)


if __name__ == "__main__":
    countries = [
        Nation("India", "🇮🇳", "New Delhi", "Hindi", "Developing Country"),
        Nation("USA", "🇺🇸", "Washington, D.C.", "English", "Developed Country"),
        Nation("Japan", "🇯🇵", "Tokyo", "Japanese", "Developed Country"),
        Nation("Germany", "🇩🇪", "Berlin", "German", "Developed Country"),
        Nation("Brazil", "🇧🇷", "Brasília", "Portuguese", "Developing Country"),
        Nation("Australia", "🇦🇺", "Canberra", "English", "Developed Country"),
        Nation("China", "🇨🇳", "Beijing", "Mandarin", "Developing Country"),
        Nation("France", "🇫🇷", "Paris", "French", "Developed Country"),
        Nation("South Africa", "🇿🇦", "Pretoria", "Multiple", "Developing Country"),
        Nation("Canada", "🇨🇦", "Ottawa", "English/French", "Developed Country")
    ]

    print(Fore.WHITE + "\n🌎 Country Info Simulator 🌎\n")
    show(countries)