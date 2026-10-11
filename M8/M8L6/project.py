from colorama import Fore, Style, init

init(autoreset=True)


def bits(n, width=8):
    return format(n & ((1 << width) - 1), f"0{width}b")


def title(text):
    print(Fore.CYAN + Style.BRIGHT + "╔" + "═" * 50 + "╗")
    print(Fore.CYAN + Style.BRIGHT + f"║{text.center(50)}║")
    print(Fore.CYAN + Style.BRIGHT + "╚" + "═" * 50 + "╝")


def section(text):
    print("\n" + Fore.YELLOW + Style.BRIGHT + f"▶ {text}")
    print(Fore.YELLOW + "─" * 52)


def pause(message="Press Enter to continue..."):
    input(Fore.LIGHTBLUE_EX + "\n" + message)


def reveal(message):
    pause("Let's reveal the answer. Press Enter...")
    print(Fore.LIGHTGREEN_EX + message)


title("Power Sets & Binary Masks")

print(Fore.WHITE + "\nLearning Goals:")
print(Fore.LIGHTGREEN_EX + "1. Understand power sets and all possible subsets.")
print(Fore.LIGHTGREEN_EX + "2. Represent selected items using binary masks.")
print(Fore.LIGHTGREEN_EX + "3. Use 1 << j to check the j-th bit.")
print(Fore.LIGHTGREEN_EX + "4. Generate every subset using nested while loops.")
print(Fore.LIGHTGREEN_EX + "5. Compare two masks to find differing bits.")
print(Fore.LIGHTGREEN_EX + "6. Solve selection-based programming problems.")

pause("Press Enter to begin learning...")


# 1. UNDERSTANDING A POWER SET
section("1. Understanding a Power Set")

items = ["A", "B", "C"]

print(Fore.LIGHTGREEN_EX + f"\nOriginal set: {items}")

n = len(items)
total = 1 << n

print(Fore.LIGHTGREEN_EX + f"Number of items: {n}")
print(Fore.LIGHTGREEN_EX + f"Number of subsets: 2^{n} = {total}")

mask = 0

while mask < total:
    subset = []
    j = 0

    while j < n:
        if mask & (1 << j):
            subset.append(items[j])
        j += 1

    print(Fore.LIGHTGREEN_EX + f"Mask {bits(mask, n)}: {subset}")
    mask += 1

print(Fore.WHITE + "\nEvery item has two choices: selected or not selected.")
print(Fore.WHITE + "Therefore, n items have 2^n possible subsets.")

pause()


# 2. BINARY MASKS
section("2. Representing Selection Using Binary Masks")

items = ["Pen", "Book", "Bag"]
mask = 5

print(Fore.LIGHTGREEN_EX + f"\nItems: {items}")
print(Fore.LIGHTGREEN_EX + f"Mask: {mask}")
print(Fore.LIGHTGREEN_EX + f"Binary mask: {bits(mask, len(items))}")

print(Fore.WHITE + "\nEach bit represents one item.")
print(Fore.WHITE + "1 means selected; 0 means not selected.")

j = 0

while j < len(items):
    selected = (mask & (1 << j)) != 0

    if selected:
        status = "SELECTED"
        color = Fore.LIGHTGREEN_EX
    else:
        status = "NOT SELECTED"
        color = Fore.LIGHTRED_EX

    print(color + f"{items[j]}: {status}")
    j += 1

pause()


# 3. BIT PROBE USING 1 << j
section("3. Bit Probe Using 1 << j")

mask = 5
n = 3

print(Fore.LIGHTGREEN_EX + f"\nMask: {mask}")
print(Fore.LIGHTGREEN_EX + f"Binary: {bits(mask, n)}")

j = 0

while j < n:
    probe = 1 << j
    result = mask & probe

    print(Fore.LIGHTGREEN_EX + f"\nChecking bit {j}:")
    print(Fore.WHITE + f"1 << {j} = {probe} ({bits(probe, n)})")
    print(Fore.WHITE + f"{mask} & {probe} = {result}")

    if result != 0:
        print(Fore.LIGHTGREEN_EX + f"Bit {j} is SET.")
    else:
        print(Fore.LIGHTRED_EX + f"Bit {j} is NOT SET.")

    j += 1

print(Fore.WHITE + "\nThe expression 1 << j creates a mask with only bit j set.")
print(Fore.WHITE + "Using mask & (1 << j), we can test that bit.")

pause()


# 4. GENERATE ALL SUBSETS USING NESTED WHILE LOOPS
section("4. Generate All Subsets")

items = ["Red", "Blue", "Green"]
n = len(items)

mask = 0
total = 1 << n

print(Fore.WHITE + "\nWe examine every possible mask from 0 to 2^n - 1.")

while mask < total:
    subset = []
    j = 0

    while j < n:
        if mask & (1 << j):
            subset.append(items[j])
        j += 1

    print(
        Fore.LIGHTGREEN_EX
        + f"Mask {bits(mask, n)} -> {subset}"
    )

    mask += 1

print(Fore.WHITE + "\nThe empty subset is included.")
print(Fore.WHITE + "The full set is also included.")
print(Fore.WHITE + f"Total subsets generated: {total}")

pause()


# 5. COMPARE TWO MASKS BIT BY BIT
section("5. Find Differences Between Two Masks")

mask_a = 5
mask_b = 3
n = 3

difference = mask_a ^ mask_b

print(Fore.LIGHTGREEN_EX + f"\nMask A: {mask_a} ({bits(mask_a, n)})")
print(Fore.LIGHTGREEN_EX + f"Mask B: {mask_b} ({bits(mask_b, n)})")
print(Fore.LIGHTGREEN_EX + f"A XOR B: {difference} ({bits(difference, n)})")

print(Fore.WHITE + "\nXOR gives 1 wherever the two bits differ.")
print(Fore.WHITE + "XOR gives 0 wherever the two bits are the same.")

j = 0

while j < n:
    bit_a = (mask_a & (1 << j)) != 0
    bit_b = (mask_b & (1 << j)) != 0

    if bit_a != bit_b:
        print(
            Fore.LIGHTYELLOW_EX
            + f"Item {j}: different selection"
        )
    else:
        print(
            Fore.LIGHTGREEN_EX
            + f"Item {j}: same selection"
        )

    j += 1

print(Fore.WHITE + f"\nNumber of differing items: {difference.bit_count()}")

pause()


# 6. REAL-WORLD SELECTION PROBLEM
section("6. Real-World Selection Problem")

items = ["Math", "Science", "English", "Computer"]
n = len(items)

print(Fore.WHITE + "\nSuppose you can choose any combination of subjects.")
print(Fore.WHITE + "Let's find every possible selection of subjects.")

mask = 0
total = 1 << n

while mask < total:
    chosen = []
    j = 0

    while j < n:
        if mask & (1 << j):
            chosen.append(items[j])
        j += 1

    if len(chosen) > 0:
        print(
            Fore.LIGHTGREEN_EX
            + f"{bits(mask, n)} -> {chosen}"
        )

    mask += 1

print(Fore.WHITE + "\nApplications:")
print(Fore.WHITE + "- Choosing subjects or courses")
print(Fore.WHITE + "- Selecting features in software")
print(Fore.WHITE + "- Finding combinations of products")
print(Fore.WHITE + "- Solving subset and optimization problems")

pause()


# 7. INTERACTIVE CHALLENGE
section("7. Your Turn!")

items = ["Apple", "Banana", "Mango"]
n = len(items)

mask = int(input(
    Fore.LIGHTRED_EX
    + "\nEnter a mask from 0 to 7: "
))

if 0 <= mask < (1 << n):
    print(Fore.LIGHTGREEN_EX + f"Binary mask: {bits(mask, n)}")

    print(Fore.WHITE + "\nWhich items are selected?")

    j = 0
    selected_items = []

    while j < n:
        if mask & (1 << j):
            selected_items.append(items[j])
            print(Fore.LIGHTGREEN_EX + f"{items[j]}: SELECTED")
        else:
            print(Fore.LIGHTRED_EX + f"{items[j]}: NOT SELECTED")

        j += 1

    guess = input(
        Fore.LIGHTRED_EX
        + "\nHow many items are selected? Enter your guess: "
    )

    reveal(f"The correct answer is {len(selected_items)}.")

    if guess.strip() == str(len(selected_items)):
        print(Fore.LIGHTGREEN_EX + "Correct! Excellent work!")
    else:
        print(
            Fore.LIGHTRED_EX
            + f"Not quite. The correct count is {len(selected_items)}."
        )

else:
    print(Fore.LIGHTRED_EX + "Invalid mask. Enter a number from 0 to 7.")

print(
    Fore.CYAN
    + Style.BRIGHT
    + "\nGreat job learning power sets and binary masks!"
)
