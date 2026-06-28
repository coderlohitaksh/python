from tkinter import *
import random

window = Tk()
window.title("🎮 Clicker Game")
window.geometry("350x250")
window.config(bg="lightblue")

score = 0

colors = [
    "red", "green", "blue", "yellow",
    "orange", "purple", "pink", "cyan"
]

score_label = Label(
    window,
    text="Score: 0",
    font=("Arial", 18),
    bg="lightblue"
)
score_label.pack(pady=10)

message = Label(
    window,
    text="Click the button!",
    font=("Arial", 12),
    bg="lightblue"
)
message.pack()

def handle_keypress(event):
    message.config(text=f"You pressed: {event.char}")

window.bind("<Key>", handle_keypress)

def handle_click(event):
    global score

    score += 1
    score_label.config(text=f"Score: {score}")

    button.config(bg=random.choice(colors))

    if score % 10 == 0:
        message.config(text="🔥 Awesome! 10 clicks!")
    elif score % 5 == 0:
        message.config(text="😎 Keep Going!")
    else:
        message.config(text="🎉 Nice Click!")

button = Button(
    window,
    text="Click Me!",
    font=("Arial", 16),
    width=12,
    height=2
)

button.pack(pady=20)

button.bind("<Button-1>", handle_click)

window.mainloop()