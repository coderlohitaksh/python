from tkinter import *
from tkinter import messagebox
from datetime import date
import random
from PIL import Image, ImageTk

root = Tk()
root.title("Age Calculator Pro 🚀")
root.geometry("700x680")
root.configure(bg="#0F172A")
root.resizable(False, False)

try:
    root.iconphoto(True, PhotoImage(file="001-rocket.png"))
except:
    pass

bg = "#485D8D"
card = "#7C97C3"
accent = "#8B5CF6"
gold = "#DCB879"
white = "#FFFFFF"
green = "#008B5D"
light = "#FF5DA9"

secret_number = random.randint(1, 10)

def calculate_age():
    try:
        name = name_entry.get().strip()

        if name == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter your name."
            )
            return

        birth_date = date(
            int(year_entry.get()),
            month_names.index(month_var.get()) + 1, 
            int(day_entry.get())
        )

        today = date.today()

        age = today.year - birth_date.year

        if (today.month, today.day) < (
            birth_date.month,
            birth_date.day
        ):
            age -= 1

        days_lived = (today - birth_date).days

        next_birthday = date(
            today.year,
            birth_date.month,
            birth_date.day
        )

        if next_birthday < today:
            next_birthday = date(
                today.year + 1,
                birth_date.month,
                birth_date.day
            )

        birthday_countdown = (
            next_birthday - today
        ).days

        if age < 13:
            level = "Young Adventurer"
        elif age < 20:
            level = "Teen Challenger"
        elif age < 40:
            level = "Adult Explorer"
        elif age < 60:
            level = "Wise Warrior"
        else:
            level = "Legend Master"

        result_name.config(
            text=f"🎉 Welcome {name}"
        )

        result_age.config(
            text=str(age)
        )

        result_level.config(
            text=f"🏆 {level}"
        )

        result_days.config(
            text=f"📅 Days Lived : {days_lived:,}"
        )

        result_birthday.config(
            text=f"🎂 Next Birthday : {birthday_countdown} day(s)"
        )

        achievement.config(
            text=f"⭐ Achievement Unlocked : {level}"
        )

    except:
        messagebox.showerror(
            "Error",
            "Please enter a valid date."
        )

def play_game():
    global secret_number

    try:
        guess = int(game_entry.get())

        if guess == secret_number:
            game_result.config(
                text="🎉 Correct Guess!",
                fg=green
            )
            secret_number = random.randint(1, 10)

        elif guess < secret_number:
            game_result.config(
                text="⬆️ Try Higher",
                fg=gold
            )

        else:
            game_result.config(
                text="⬇️ Try Lower",
                fg=gold
            )

    except:
        game_result.config(
            text="❌ Enter a valid number",
            fg="red"
        )

def enter_btn(e):
    calc_btn.config(bg="#7C3AED")

def leave_btn(e):
    calc_btn.config(bg=accent)

header = Frame(root, bg=bg)
header.pack(pady=10)

try:
    img = Image.open("logo1.png")

    width = 520
    height = int(width * img.height / img.width)

    img = img.resize((width, height))

    logo = ImageTk.PhotoImage(img)

    logo_label = Label(
        header,
        image=logo,
        bg=bg
    )
    logo_label.pack(pady=(5, 10))

except Exception as e:
    print("Logo Error:", e)

Label(
    header,
    text="Calculate • Explore • Level Up",
    bg=bg,
    fg=light,
    font=("Segoe UI", 11, "bold")
).pack()

input_card = Frame(
    root,
    bg=card,
    padx=25,
    pady=20
)

input_card.pack(
    padx=20,
    pady=8,
    fill=X
)

Label(
    input_card,
    text="👤 Full Name",
    bg=card,
    fg=white,
    font=("Segoe UI", 11, "bold")
).grid(
    row=0,
    column=0,
    sticky=W,
    pady=10
)

name_entry = Entry(
    input_card,
    width=28,
    font=("Segoe UI", 11)
)

name_entry.grid(
    row=0,
    column=1,
    padx=15
)

Label(
    input_card,
    text="📅 Day",
    bg=card,
    fg=white,
    font=("Segoe UI", 11, "bold")
).grid(
    row=1,
    column=0,
    sticky=W,
    pady=10
)

day_entry = Spinbox(
    input_card,
    from_=1,
    to=31,
    width=25,
    font=("Segoe UI", 11)
)

day_entry.grid(
    row=1,
    column=1,
    padx=15
)

Label(
    input_card,
    text="📆 Month",
    bg=card,
    fg=white,
    font=("Segoe UI", 11, "bold")
).grid(
    row=2,
    column=0,
    sticky=W,
    pady=10
)

month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

month_var = StringVar()
month_var.set("January")

month_entry = OptionMenu(
    input_card,
    month_var,
    *month_names
)

month_entry.config(
    width=22,
    font=("Segoe UI", 10)
)

month_entry.grid(
    row=2,
    column=1,
    padx=15
)

Label(
    input_card,
    text="🗓 Year",
    bg=card,
    fg=white,
    font=("Segoe UI", 11, "bold")
).grid(
    row=3,
    column=0,
    sticky=W,
    pady=10
)

year_entry = Spinbox(
    input_card,
    from_=1900,
    to=2100,
    width=25,
    font=("Segoe UI", 11)
)

year_entry.grid(
    row=3,
    column=1,
    padx=15
)

calc_btn = Button(
    root,
    text="⚡ CALCULATE AGE",
    bg=accent,
    fg="white",
    activebackground="#7C3AED",
    activeforeground="white",
    font=("Segoe UI", 13, "bold"),
    bd=0,
    padx=25,
    pady=12,
    cursor="hand2",
    command=calculate_age
)

calc_btn.pack(pady=10)

calc_btn.bind("<Enter>", enter_btn)
calc_btn.bind("<Leave>", leave_btn)

result_card = Frame(
    root,
    bg=card,
    padx=20,
    pady=20
)

result_card.pack(
    padx=20,
    pady=8,
    fill=X
)

Label(
    result_card,
    text="🏆 AGE DASHBOARD",
    bg=card,
    fg=gold,
    font=("Segoe UI", 16, "bold")
).pack()

result_name = Label(
    result_card,
    text="",
    bg=card,
    fg=white,
    font=("Segoe UI", 15, "bold")
)

result_name.pack(pady=(15, 5))

result_age = Label(
    result_card,
    text="?",
    bg=card,
    fg=gold,
    font=("Segoe UI Black", 52)
)

result_age.pack()

result_level = Label(
    result_card,
    text="",
    bg=card,
    fg=green,
    font=("Segoe UI", 14, "bold")
)

result_level.pack()

achievement = Label(
    result_card,
    text="",
    bg=card,
    fg="#FBBF24",
    font=("Segoe UI", 12, "bold")
)

achievement.pack(pady=5)

result_days = Label(
    result_card,
    text="",
    bg=card,
    fg=white,
    font=("Segoe UI", 11)
)

result_days.pack(pady=5)

result_birthday = Label(
    result_card,
    text="",
    bg=card,
    fg=white,
    font=("Segoe UI", 11)
)

result_birthday.pack()

game_card = Frame(
    root,
    bg=card,
    padx=20,
    pady=20
)

game_card.pack(
    padx=20,
    pady=5,
    fill=X
)

Label(
    game_card,
    text="🎮 BONUS GAME",
    bg=card,
    fg=gold,
    font=("Segoe UI", 16, "bold")
).pack()

Label(
    game_card,
    text="Guess a number between 1 and 10",
    bg=card,
    fg=light,
    font=("Segoe UI", 10)
).pack(pady=5)

game_entry = Entry(
    game_card,
    width=10,
    justify="center",
    font=("Segoe UI", 14)
)

game_entry.pack(pady=10)

Button(
    game_card,
    text="🎯 GUESS",
    bg=gold,
    fg="white",
    bd=0,
    padx=20,
    pady=8,
    font=("Segoe UI", 11, "bold"),
    command=play_game
).pack()

game_result = Label(
    game_card,
    text="",
    bg=card,
    fg=white,
    font=("Segoe UI", 12, "bold")
)

game_result.pack(pady=10)

footer = Label(
    root,
    text="🚀 Powered by Python & Tkinter",
    bg=bg,
    fg="#94A3B8",
    font=("Segoe UI", 9)
)

footer.pack(side=BOTTOM, pady=8)

root.mainloop()