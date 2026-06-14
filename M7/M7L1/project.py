from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from math import sqrt

def calculate():
    try:
        n1 = float(entry1.get())
        op = operation.get()

        if op in ["Square", "Cube", "Square Root"]:
            if op == "Square":
                result = n1 ** 2
                expression = f"{n1}² = {result}"

            elif op == "Cube":
                result = n1 ** 3
                expression = f"{n1}³ = {result}"

            elif op == "Square Root":
                result = sqrt(n1)
                expression = f"√{n1} = {result}"

        else:
            n2 = float(entry2.get())

            if op == "+":
                result = n1 + n2
            elif op == "-":
                result = n1 - n2
            elif op == "*":
                result = n1 * n2
            elif op == "/":
                result = n1 / n2
            elif op == "%":
                result = n1 % n2
            elif op == "^":
                result = n1 ** n2
            elif op == "//":
                result = n1 // n2
            elif op == "Max":
                result = max(n1, n2)
            elif op == "Min":
                result = min(n1, n2)
            elif op == "Average":
                result = (n1 + n2) / 2

            expression = f"{n1} {op} {n2} = {result}"

        result_box.delete("1.0", END)
        result_box.insert(END, expression)

        history.insert(END, expression)

        status.config(text=f"Last Operation: {op}")

    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def clear_inputs():
    entry1.delete(0, END)
    entry2.delete(0, END)
    result_box.delete("1.0", END)
    status.config(text="Ready")

def clear_history():
    if messagebox.askyesno("Confirm", "Delete all calculation history?"):
        history.delete(0, END)
        status.config(text="History Cleared")

root = Tk()
root.title("🚀 Smart Calculator")
root.geometry("700x550")
root.configure(bg="#222831")

try:
    icon = PhotoImage(file="001-rocket.png")
    root.iconphoto(True, icon)
except:
    pass

title = Label(
    root,
    text="🚀 Smart Calculator",
    font=("Segoe UI", 20, "bold"),
    bg="#222831",
    fg="#00ADB5"
)
title.pack(pady=10)

subtitle = Label(
    root,
    text="Basic and Advanced Calculator using Tkinter",
    font=("Segoe UI", 10),
    bg="#222831",
    fg="white"
)
subtitle.pack()

frame = Frame(root, bg="#222831")
frame.pack(pady=15)

Label(
    frame,
    text="First Number",
    font=("Segoe UI", 11),
    bg="#222831",
    fg="white"
).grid(row=0, column=0, padx=10, pady=8, sticky="w")

entry1 = Entry(frame, width=25, font=("Segoe UI", 11))
entry1.grid(row=0, column=1, padx=10)

Label(
    frame,
    text="Second Number",
    font=("Segoe UI", 11),
    bg="#222831",
    fg="white"
).grid(row=1, column=0, padx=10, pady=8, sticky="w")

entry2 = Entry(frame, width=25, font=("Segoe UI", 11))
entry2.grid(row=1, column=1, padx=10)

Label(
    frame,
    text="Operation",
    font=("Segoe UI", 11),
    bg="#222831",
    fg="white"
).grid(row=2, column=0, padx=10, pady=8, sticky="w")

operation = Combobox(
    frame,
    width=22,
    font=("Segoe UI", 11),
    state="readonly"
)

operation["values"] = (
    "+",
    "-",
    "*",
    "/",
    "%",
    "^",
    "//",
    "Max",
    "Min",
    "Average",
    "Square",
    "Cube",
    "Square Root"
)

operation.current(0)
operation.grid(row=2, column=1, padx=10)

button_frame = Frame(root, bg="#222831")
button_frame.pack(pady=10)

Button(
    button_frame,
    text="Calculate",
    command=calculate,
    bg="#00ADB5",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=15
).grid(row=0, column=0, padx=5)

Button(
    button_frame,
    text="Clear Inputs",
    command=clear_inputs,
    bg="#F96D00",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=15
).grid(row=0, column=1, padx=5)

Button(
    button_frame,
    text="Clear History",
    command=clear_history,
    bg="#6A5ACD",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=15
).grid(row=0, column=2, padx=5)

Button(
    button_frame,
    text="Exit",
    command=root.destroy,
    bg="#E84545",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=15
).grid(row=0, column=3, padx=5)

Label(
    root,
    text="Result",
    font=("Segoe UI", 12, "bold"),
    bg="#222831",
    fg="white"
).pack(pady=(15, 5))

result_box = Text(
    root,
    height=2,
    width=45,
    font=("Consolas", 12)
)
result_box.pack()

Label(
    root,
    text="Calculation History",
    font=("Segoe UI", 12, "bold"),
    bg="#222831",
    fg="white"
).pack(pady=(15, 5))

history = Listbox(
    root,
    width=70,
    height=10,
    font=("Consolas", 10),
    bg="#EEEEEE"
)
history.pack(pady=5)

status = Label(
    root,
    text="Ready",
    bd=1,
    relief=SUNKEN,
    anchor=W,
    bg="#393E46",
    fg="white"
)
status.pack(side=BOTTOM, fill=X)

root.mainloop() 