from colorama import Fore, init
init(autoreset=True)
sunny = 0
rainy = 0
weather = []

print("Enter weather for 7 days (1 for sunny, 0 for rainy):")
for i in range(7):
    while True:
        try:
            day = int(input(f"Day {i+1}: "))
            if day not in (0, 1):
                print(Fore.YELLOW + "Please enter 0 for rainy or 1 for sunny.")
                continue
            weather.append(day)
            break
        except ValueError:
            print(Fore.YELLOW + "Invalid input. Enter 0 or 1.")

print("\nWeather for the week:")
for i, day in enumerate(weather):
    if day == 1:
        print(f"Day {i+1}: " + Fore.YELLOW + "Sunny☀️")
        sunny += 1
    else:
        print(f"Day {i+1}: " + Fore.BLUE + "Rainy🌦️")
        rainy += 1

print("\nOverall weather:")
if sunny > rainy:
    print(Fore.GREEN + "Good weather")
else:
    print(Fore.RED + "Bad weather")
