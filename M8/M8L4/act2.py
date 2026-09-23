from colorama import Fore, Style, init

init(autoreset=True)

def bits(n, width=16):
    return format(n & ((1 << width) - 1), f"0{width}b")

def pause(message):
    input(Fore.YELLOW + f"\n{message}")

print(Fore.CYAN + Style.BRIGHT + "\nBITWISE POWER OF 4")
print("Learn how binary numbers and bitwise operators work!")

pause("Press Enter to learn n & (n - 1)...")

print(Fore.MAGENTA + "\n1. CLEARING THE RIGHTMOST SET BIT")

print(Fore.CYAN + f"\n12 in binary : {bits(12)}")
print(Fore.CYAN + f"11 in binary : {bits(11)}")
print(Fore.GREEN + f"12 & 11      : {bits(12 & 11)}")
print(Fore.GREEN + f"12 & 11 = {12 & 11}")

print("\n12  = 1100")
print("11  = 1011")
print("     ----")
print("     1000  -> rightmost 1 is cleared")

print(Fore.MAGENTA + "\n2. POWERS OF 4")

for i in range(8):
    value = 4 ** i
    print(f"4^{i:<2} = {value:<6} Binary = {bits(value)}")

print(Fore.MAGENTA + "\n3. CHECK WHETHER A NUMBER IS A POWER OF 4")

n = int(input(Fore.GREEN + "\nEnter a number: "))

guess = input(
    Fore.GREEN + f"Is {n} a power of 4? (Yes/No): "
).strip().lower()

pause("Press Enter to check...")

is_power_of_4 = (
    n > 0
    and (n & (n - 1)) == 0
    and n % 3 == 1
)

print(Fore.CYAN + "\nNUMBER CHECK")
print(f"Number       : {n}")
print(f"Binary       : {bits(n)}")
print(f"n - 1        : {n - 1}")
print(f"n binary     : {bits(n)}")
print(f"n - 1 binary : {bits(n - 1)}")
print(f"n & (n - 1)  : {n & (n - 1)}")
print(f"n % 3        : {n % 3}")

if is_power_of_4:
    print(Fore.GREEN + f"\nYES! {n} IS A POWER OF 4!")

    exponent = 0
    temp = n

    while temp > 1:
        temp //= 4
        exponent += 1

    print(f"Because 4^{exponent} = {n}")
else:
    print(Fore.RED + f"\nNO! {n} IS NOT A POWER OF 4.")

correct_guess = (
    (guess == "yes" and is_power_of_4)
    or (guess == "no" and not is_power_of_4)
)

if correct_guess:
    print(Fore.GREEN + "Your guess is correct!")
else:
    print(Fore.RED + "Your guess is incorrect.")

print(Fore.MAGENTA + "\n4. WHY DOES THIS WORK?")

print("\nA number is a power of 4 when:")
print("1. It is positive.")
print("2. It is a power of 2.")
print("3. The exponent of 2 is even.")

print("\nExamples:")
print("4   = 2^2")
print("16  = 2^4")
print("64  = 2^6")
print("256 = 2^8")

print(Fore.YELLOW + "\nn & (n - 1) == 0")
print("Checks whether n is a power of 2.")

print(Fore.YELLOW + "\nn % 3 == 1")
print("Distinguishes powers of 4 from other powers of 2.")

print(Fore.GREEN + "\nTherefore:")
print("n > 0")
print("(n & (n - 1)) == 0.")
print("n % 3 == 1")
 
print(Fore.GREEN + "\n=> POWER OF 4") 