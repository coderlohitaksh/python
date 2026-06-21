from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date

# ---------------- Function ----------------
def calculate_age():
    try:
        name = name_entry.get().strip()

        if not name:
            messagebox.showwarning("Input Error", "Please enter your name")
            return

        day = int(day_combo.get())
        month = int(month_combo.get())
        year = int(year_combo.get())

        today = date.today()

        birth_date = date(year, month, day)

        age = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(
            text=f"🎉 Hello {name}!\n\nYour current age is\n{age} Years",
            fg="#1B5E20"
        )

    except:
        messagebox.showerror(
            "Error",
            "Please enter valid date details."
        )


# ---------------- Main Window ----------------
root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.configure(bg="#E8F5E9")
root.resizable(False, False)

# ---------------- Heading ----------------
heading = Label(
    root,
    text="🎂 AGE CALCULATOR",
    font=("Segoe UI", 18, "bold"),
    bg="#E8F5E9",
    fg="#2E7D32"
)
heading.pack(pady=15)

# ---------------- Main Frame ----------------
main_frame = Frame(
    root,
    bg="white",
    bd=2,
    relief=RIDGE
)
main_frame.pack(padx=20, pady=10, fill=X)

# Name
Label(
    main_frame,
    text="Name",
    font=("Segoe UI", 11, "bold"),
    bg="white"
).grid(row=0, column=0, padx=10, pady=10, sticky=W)

name_entry = Entry(
    main_frame,
    font=("Segoe UI", 11),
    width=20
)
name_entry.grid(row=0, column=1, pady=10)

# Day
Label(
    main_frame,
    text="Day",
    font=("Segoe UI", 11, "bold"),
    bg="white"
).grid(row=1, column=0, padx=10, pady=10, sticky=W)

day_combo = ttk.Combobox(
    main_frame,
    values=list(range(1, 32)),
    width=18,
    state="readonly"
)
day_combo.grid(row=1, column=1)

# Month
Label(
    main_frame,
    text="Month",
    font=("Segoe UI", 11, "bold"),
    bg="white"
).grid(row=2, column=0, padx=10, pady=10, sticky=W)

month_combo = ttk.Combobox(
    main_frame,
    values=list(range(1, 13)),
    width=18,
    state="readonly"
)
month_combo.grid(row=2, column=1)

# Year
Label(
    main_frame,
    text="Year",
    font=("Segoe UI", 11, "bold"),
    bg="white"
).grid(row=3, column=0, padx=10, pady=10, sticky=W)

year_combo = ttk.Combobox(
    main_frame,
    values=list(range(1950, 2026)),
    width=18,
    state="readonly"
)
year_combo.grid(row=3, column=1, pady=10)

# Button
Button(
    root,
    text="Calculate Age",
    font=("Segoe UI", 11, "bold"),
    bg="#43A047",
    fg="white",
    activebackground="#2E7D32",
    cursor="hand2",
    command=calculate_age
).pack(pady=20)

# Result Card
result_frame = Frame(
    root,
    bg="#C8E6C9",
    bd=2,
    relief=GROOVE
)
result_frame.pack(
    padx=20,
    pady=10,
    fill=X
)

result_label = Label(
    result_frame,
    text="Enter details and click Calculate",
    font=("Segoe UI", 12, "bold"),
    bg="#C8E6C9"
)
result_label.pack(pady=15)

root.mainloop()