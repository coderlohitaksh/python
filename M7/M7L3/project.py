from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import random

root=Tk()
root.title("Space Length Converter")
root.geometry("900x600")
root.resizable(False,False)

bg=ImageTk.PhotoImage(Image.open("space_bg.jpg").resize((900,600)))
rocket=ImageTk.PhotoImage(Image.open("001-rocket.png"))
ufo=ImageTk.PhotoImage(Image.open("ufo.png"))
shield=ImageTk.PhotoImage(Image.open("shield.png"))
bullet=ImageTk.PhotoImage(Image.open("bullet.png"))
boss=ImageTk.PhotoImage(Image.open("boss.png"))

canvas=Canvas(root,width=900,height=600,highlightthickness=0)
canvas.pack(fill="both",expand=True)

canvas.create_image(0,0,image=bg,anchor="nw")

stars=[]

for i in range(100):
    x=random.randint(0,900)
    y=random.randint(0,600)
    s=canvas.create_oval(x,y,x+2,y+2,fill="white",outline="")
    stars.append(s)

canvas.create_image(70,70,image=shield)
canvas.create_image(830,70,image=boss)
canvas.create_image(70,530,image=rocket)
canvas.create_image(830,530,image=ufo)
canvas.create_image(760,300,image=bullet)

rocket_x=120
rocket_y=180

ufo_x=760
ufo_y=420

rocket_id=canvas.create_image(
rocket_x,
rocket_y,
image=rocket
)

ufo_id=canvas.create_image(
ufo_x,
ufo_y,
image=ufo
)

canvas.create_text(
450,
50,
text="SPACE LENGTH CONVERTER",
font=("Arial",28,"bold"),
fill="cyan"
)

panel=Frame(
root,
bg="#0b1020",
bd=5,
relief=RIDGE
)

canvas.create_window(
450,
330,
window=panel,
width=430,
height=310
)

Label(
panel,
text="Enter Length (Inches)",
font=("Arial",16,"bold"),
bg="#0b1020",
fg="yellow"
).pack(pady=15)

entry=Entry(
panel,
font=("Arial",18),
justify="center",
width=15
)

entry.pack()

result=Label(
panel,
text="",
font=("Arial",17,"bold"),
bg="#0b1020",
fg="white"
)

result.pack(pady=20)

score=0

score_label=Label(
panel,
text="Score : 0",
font=("Arial",15,"bold"),
bg="#0b1020",
fg="lime"
)

score_label.pack()

footer=canvas.create_text(
450,
585,
text="Mission : Convert Inches Into Centimeters",
font=("Arial",12,"bold"),
fill="white"
)

def move_stars():
    for s in stars:
        canvas.move(s,-2,0)
        x1,y1,x2,y2=canvas.coords(s)
        if x2<0:
            y=random.randint(0,600)
            canvas.coords(s,900,y,902,y+2)
    root.after(40,move_stars)

def convert():
    global score
    try:
        inch=float(entry.get())
        cm=inch*2.54
        score+=10
        result.config(
            text=f"{inch:.2f} Inches = {cm:.2f} Centimeters",
            fg=random.choice([
                "cyan",
                "yellow",
                "lime",
                "orange",
                "white",
                "pink"
            ])
        )
        score_label.config(text=f"Score : {score}")
    except:
        messagebox.showerror(
            "Error",
            "Enter a valid number"
        )

def move_rocket():
    global rocket_x
    rocket_x+=3
    if rocket_x>950:
        rocket_x=-50
    canvas.coords(
        rocket_id,
        rocket_x,
        rocket_y
    )
    root.after(
        20,
        move_rocket
    )

direction=3

def move_ufo():
    global ufo_y,direction
    ufo_y+=direction
    if ufo_y>500:
        direction=-3
    if ufo_y<100:
        direction=3
    canvas.coords(
        ufo_id,
        ufo_x,
        ufo_y
    )
    root.after(
        35,
        move_ufo
    )

def flash():
    canvas.itemconfig(
        footer,
        fill=random.choice([
            "cyan",
            "yellow",
            "lime",
            "white",
            "orange"
        ])
    )
    root.after(
        300,
        flash
    )

Button(
    panel,
    text="CONVERT",
    font=("Arial",15,"bold"),
    bg="#00aa00",
    fg="white",
    width=16,
    command=convert
).pack(pady=10)

Button(
    panel,
    text="CLEAR",
    font=("Arial",15,"bold"),
    bg="#0066cc",
    fg="white",
    width=16,
    command=lambda:[
        entry.delete(0,END),
        result.config(text="")
    ]
).pack(pady=5)

Button(
    panel,
    text="EXIT",
    font=("Arial",15,"bold"),
    bg="#cc0000",
    fg="white",
    width=16,
    command=root.destroy
).pack(pady=10)

move_stars()
move_rocket()
move_ufo()
flash()

root.mainloop()