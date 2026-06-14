from tkinter import *
from random import randint

root = Tk()
root.title("Galaxy Rocket")
root.geometry("800x650")
root.resizable(False, False)

canvas = Canvas(root, width=800, height=600, bg="#020617")
canvas.pack()

score = 0

stars = []

for i in range(180):
    x = randint(0, 800)
    y = randint(0, 600)
    size = randint(1, 3)

    star = canvas.create_oval(
        x,
        y,
        x + size,
        y + size,
        fill="white",
        outline=""
    )

    stars.append(star)

canvas.create_oval(
    560,
    70,
    700,
    210,
    fill="#3b82f6",
    outline=""
)

canvas.create_oval(
    90,
    100,
    170,
    180,
    fill="#f97316",
    outline=""
)

canvas.create_text(
    402,
    42,
    text="GALAXY ROCKET",
    fill="#00ffff",
    font=("Arial", 28, "bold")
)

canvas.create_text(
    400,
    40,
    text="GALAXY ROCKET",
    fill="white",
    font=("Arial", 28, "bold")
)

rocket_img = PhotoImage(file="001-rocket.png")

rocket = canvas.create_image(
    400,
    500,
    image=rocket_img
)

flame = canvas.create_polygon(
    390,
    520,
    400,
    560,
    410,
    520,
    fill="orange",
    outline=""
)

score_text = canvas.create_text(
    90,
    30,
    text="Score : 0",
    fill="white",
    font=("Arial", 16, "bold")
)

def animate_stars():
    for star in stars:
        canvas.move(star, 0, 3)

        x1, y1, x2, y2 = canvas.coords(star)

        if y1 > 600:
            x = randint(0, 800)

            canvas.coords(
                star,
                x,
                0,
                x + 2,
                2
            )

    root.after(40, animate_stars)

def animate_flame():
    x, y = canvas.coords(rocket)

    size = randint(25, 45)

    canvas.coords(
        flame,
        x - 10,
        y + 20,
        x,
        y + size,
        x + 10,
        y + 20
    )

    root.after(80, animate_flame)

def move_left(event):
    x, y = canvas.coords(rocket)

    if x > 40:
        canvas.move(rocket, -20, 0)
        canvas.move(flame, -20, 0)

def move_right(event):
    x, y = canvas.coords(rocket)

    if x < 760:
        canvas.move(rocket, 20, 0)
        canvas.move(flame, 20, 0)

def move_up(event):
    x, y = canvas.coords(rocket)

    if y > 100:
        canvas.move(rocket, 0, -20)
        canvas.move(flame, 0, -20)

def move_down(event):
    x, y = canvas.coords(rocket)

    if y < 560:
        canvas.move(rocket, 0, 20)
        canvas.move(flame, 0, 20)

def move_bullet(bullet):
    canvas.move(bullet, 0, -15)

    glow = canvas.create_oval(
        canvas.coords(bullet),
        outline="#00ffff"
    )

    canvas.after(50, lambda: canvas.delete(glow))

    x1, y1, x2, y2 = canvas.coords(bullet)

    if y2 > 0:
        root.after(25, lambda: move_bullet(bullet))
    else:
        canvas.delete(bullet)

def shoot():
    global score

    x, y = canvas.coords(rocket)

    bullet = canvas.create_oval(
        x - 5,
        y - 35,
        x + 5,
        y - 15,
        fill="#00ffff",
        outline="white",
        width=2
    )

    score += 1

    canvas.itemconfig(
        score_text,
        text=f"Score : {score}"
    )

    move_bullet(bullet)

shoot_button = Button(
    root,
    text="🚀 SHOOT",
    command=shoot,
    bg="#dc2626",
    fg="white",
    font=("Arial", 14, "bold"),
    width=15
)

shoot_button.pack(pady=10)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<space>", lambda e: shoot())

animate_stars()
animate_flame()

root.mainloop()