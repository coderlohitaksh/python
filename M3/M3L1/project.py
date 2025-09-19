from colorama import Fore, Style, init
init(autoreset=True)
WIDTH = 110

title = "✨ 🎉 🎀 Welcome to the Circumference Calculator 🎀 🎉 ✨"
print(Style.BRIGHT + Fore.CYAN + title.center(WIDTH) + "\n")
radius = float(input(Fore.YELLOW + "Enter the radius of the circle: "))
circumference = 2 * 3.14159 * radius

msg = "✅ Calculation Complete!"
print("\n" + Fore.GREEN + Style.BRIGHT + msg.center(WIDTH) + "\n")

print(Fore.MAGENTA + Style.BRIGHT + "Formula: " 
      + Fore.WHITE + "C = 2 * π * r   (π ≈ 3.14159)")
print(Fore.CYAN + "Radius entered: " + Fore.YELLOW + f"{radius:.2f}")
print(Fore.CYAN + "Circumference: " + Fore.GREEN + f"{circumference:.2f}\n")
