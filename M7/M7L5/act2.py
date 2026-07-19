import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("💰 Denomination Counter")
root.geometry("850x700")
root.resizable(False, False)

title = ctk.CTkLabel(
    root,
    text="💰 DENOMINATION COUNTER",
    font=("Poppins", 30, "bold")
)
title.pack(pady=(20, 5))

subtitle = ctk.CTkLabel(
    root,
    text="Calculate Indian Currency Notes Instantly",
    font=("Arial", 16)
)
subtitle.pack()

try:
    img = ctk.CTkImage(
        light_image=Image.open("app_img.jpg"),
        dark_image=Image.open("app_img.jpg"),
        size=(260, 260)
    )

    image_label = ctk.CTkLabel(
        root,
        image=img,
        text=""
    )

    image_label.pack(pady=20)

except:
    ctk.CTkLabel(
        root,
        text="Image not found",
        font=("Arial", 16)
    ).pack(pady=30)

colors = [
    "#3B82F6",
    "#2563EB",
    "#1D4ED8",
    "#2563EB"
]

index = 0

def animate():
    global index
    start_button.configure(fg_color=colors[index])
    index = (index + 1) % len(colors)
    root.after(350, animate)

def open_calculator():
    messagebox.showinfo(
        "Welcome",
        "Let's calculate your denomination!"
    )
    calculator_window()

start_button = ctk.CTkButton(
    root,
    text="🚀 Get Started",
    width=240,
    height=55,
    corner_radius=12,
    font=("Arial", 18, "bold"),
    fg_color="#2563EB",
    hover_color="#1D4ED8",
    command=open_calculator
)

start_button.pack(pady=20)

animate()

def calculator_window():

    top = ctk.CTkToplevel(root)
    top.title("💵 Denomination Calculator")
    top.geometry("900x860")
    top.resizable(False, False)

    top.attributes("-alpha", 0)

    def fade(alpha=0):
        alpha += 0.05
        top.attributes("-alpha", alpha)
        if alpha < 1:
            top.after(20, lambda: fade(alpha))

    fade()

    title = ctk.CTkLabel(
        top,
        text="Indian Currency Calculator",
        font=("Poppins", 24, "bold")
    )

    title.pack(pady=(20,10))

    amount_entry = ctk.CTkEntry(
        top,
        width=320,
        height=42,
        placeholder_text="Enter Total Amount",
        font=("Arial",16)
    )

    amount_entry.pack(pady=10)

    denominations = [2000,500,200,100,50,20,10,5,2,1]

    entries = {}

    frame = ctk.CTkFrame(
        top,
        corner_radius=12
    )

    frame.pack(
        padx=25,
        pady=(20,15),
        fill="x"
    )

    for i, note in enumerate(denominations):

        lbl = ctk.CTkLabel(
            frame,
            text=f"₹ {note}",
            font=("Arial", 15, "bold")
        )

        lbl.grid(
            row=i,
            column=0,
            padx=(35,15),
            pady=8,
            sticky="w"
        )

        ent = ctk.CTkEntry(
            frame,
            width=150,
            height=34,
            justify="center",
            font=("Arial",15)
        )

        ent.grid(
            row=i,
            column=1,
            padx=(10,30),
            pady=8
        )

        entries[note] = ent

    remain = ctk.CTkLabel(
        top,
        text="Remaining Amount : ₹0",
        font=("Arial",16,"bold"),
        text_color="orange"
    )

    remain.pack(pady=(5,20))

    def animate(entry, target, current=0):

        if target == 0:
            entry.delete(0, "end")
            entry.insert(0, "0")
            return

        step = max(1, target // 20)

        current += step

        if current >= target:
            current = target

        entry.delete(0, "end")
        entry.insert(0, str(current))

        if current < target:
            top.after(
                20,
                lambda: animate(entry, target, current)
            )

    def calculate():
        try:
            amount = int(amount_entry.get())

            notes = {}

            for note in denominations:
                notes[note] = amount // note
                amount %= note

            for note in denominations:
                entries[note].delete(0, "end")
                animate(entries[note], notes[note])

            remain.configure(
                text=f"Remaining Amount : ₹{amount}"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter a valid amount."
            )

    def reset():
        amount_entry.delete(0, "end")

        for entry in entries.values():
            entry.delete(0, "end")

        remain.configure(
            text="Remaining Amount : ₹0"
        )

    button_frame = ctk.CTkFrame(
        top,
        fg_color="transparent"
    )

    button_frame.pack(
        pady=(10,25)
    )

    calculate_btn = ctk.CTkButton(
        button_frame,
        text="🧮 Calculate",
        width=180,
        height=48,
        corner_radius=10,
        font=("Arial",17,"bold"),
        fg_color="#2563EB",
        hover_color="#1D4ED8",
        command=calculate
    )

    calculate_btn.grid(
        row=0,
        column=0,
        padx=10
    )

    reset_btn = ctk.CTkButton(
        button_frame,
        text="🔄 Reset",
        width=180,
        height=48,
        corner_radius=10,
        font=("Arial",17,"bold"),
        fg_color="#F59E0B",
        hover_color="#D97706",
        command=reset
    )

    reset_btn.grid(
        row=0,
        column=1,
        padx=10
    )
    
    exit_btn = ctk.CTkButton(
        button_frame,
        text="❌ Exit",
        width=180,
        height=48,
        corner_radius=10,
        font=("Arial",17,"bold"),
        fg_color="#DC2626",
        hover_color="#B91C1C",
        command=top.destroy
    )

    exit_btn.grid(
        row=0,
        column=2,
        padx=10
    )

root.mainloop()