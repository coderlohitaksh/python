import numpy as np
import sounddevice as sd
import threading
import time
import sys
import shutil
import pyfiglet
from colorama import init, Fore, Style

init(autoreset=True)

stop_music = False

def play_chord(frequencies, duration=1, volume=0.5):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = sum([np.sin(2 * np.pi * f * t) for f in frequencies]) / len(frequencies)
    sd.play(volume * wave, samplerate=sample_rate)
    sd.wait()

def play_light_sound(duration=0.2, frequency=880, volume=0.3):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * frequency * t)
    sd.play(volume * wave, samplerate=sample_rate)
    sd.wait()

def type_text(text, color=Fore.WHITE, delay=0.05):
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()

colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def rainbow_big_text(text):
    ascii_banner = pyfiglet.figlet_format(text, font="slant")
    lines = ascii_banner.split("\n")
    terminal_width = shutil.get_terminal_size().columns
    centered_lines = [line.center(terminal_width) for line in lines]
    color_index = 0
    for line in centered_lines:
        colored_line = ""
        for char in line:
            if char != " ":
                colored_line += colors[color_index % len(colors)] + char
                color_index += 1
            else:
                colored_line += " "
        print(colored_line + Style.RESET_ALL)

def ending_scene():
    type_text("\n🎉 Congratulations! You've completed the Age Game! 🎉", Fore.MAGENTA, 0.05)
    for _ in range(3):
        print(Fore.RED + "*" + Fore.YELLOW + "*" + Fore.GREEN + "*" + Fore.CYAN + "*" + Fore.BLUE + "*" + Fore.MAGENTA + "*")
        time.sleep(0.3)
    type_text("\nThanks for playing! See you next time!", Fore.CYAN, 0.07)

def music_loop():
    c_major = [261.63, 329.63, 392.00]
    while not stop_music:
        play_chord(c_major, duration=1)
        play_light_sound(duration=0.2)
        time.sleep(0.1)

type_text("Hello!! Dear friends, I am making a game. Now you will play it!", Fore.CYAN, 0.07)
time.sleep(1)
rainbow_big_text("A G E\nC O U N T E R")

music_thread = threading.Thread(target=music_loop, daemon=True)
music_thread.start()

while True:
    age_input = input(Fore.LIGHTYELLOW_EX + "Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print(Fore.LIGHTRED_EX + "Invalid input. Please enter a valid integer.")

if age % 2 == 0:
    type_text(f"Your age {age} is even!", Fore.LIGHTGREEN_EX, 0.07)
else:
    type_text(f"Your age {age} is odd!", Fore.GREEN, 0.07)

time.sleep(1)
stop_music = True
ending_scene()
