from tkinter import *
from tkinter import ttk
import random
import time

root = Tk()
root.title("Length Converter App")
root.geometry("900x500")
root.configure(bg="black")
root.resizable(False, False)

GREEN="#00FF41"
LIGHT="#66FF66"
DARK="#003300"
RED="#FF3333"
YELLOW="#FFD700"

view=PhotoImage(file="001-view.png").subsample(2,2)
hide=PhotoImage(file="002-hide.png").subsample(2,2)

style=ttk.Style()
style.theme_use("clam")

style.configure(
    "green.Horizontal.TProgressbar",
    troughcolor="black",
    background=GREEN,
    bordercolor="black",
    lightcolor=GREEN,
    darkcolor=GREEN
)

title=Label(
    root,
    text="PASSWORD STRENGTH ANALYZER",
    bg="black",
    fg=GREEN,
    font=("Consolas",22,"bold")
)
title.pack(pady=10)

status=Label(
    root,
    text="SYSTEM STATUS : READY",
    bg="black",
    fg=LIGHT,
    font=("Consolas",11)
)
status.pack()

main=Frame(root,bg="black")
main.pack(fill=BOTH,expand=True)

matrix=Text(
    main,
    width=28,
    bg="black",
    fg=DARK,
    bd=0,
    font=("Consolas",9)
)
matrix.pack(side=LEFT,fill=Y)

panel=Frame(
    main,
    bg="black",
    highlightbackground=GREEN,
    highlightthickness=2
)
panel.pack(side=LEFT,padx=20,pady=20,fill=BOTH,expand=True)

Label(
    panel,
    text="ENTER PASSWORD",
    bg="black",
    fg=GREEN,
    font=("Consolas",16,"bold")
).grid(row=0,column=0,columnspan=3,pady=20)

password=Entry(
    panel,
    width=25,
    show="*",
    bg="black",
    fg=GREEN,
    insertbackground=GREEN,
    font=("Consolas",14)
)
password.grid(row=1,column=0,padx=10,pady=10)

show=False

def toggle():

    global show

    if show==False:
        password.config(show="")
        btn_show.config(image=hide)
        show=True

    else:
        password.config(show="*")
        btn_show.config(image=view)
        show=False

btn_show=Button(
    panel,
    image=view,
    command=toggle,
    bg="white",
    activebackground="white",
    bd=1,
    relief=SOLID,
    cursor="hand2"
)
btn_show.grid(row=1,column=1,padx=5)

progress=ttk.Progressbar(
    panel,
    length=350,
    style="green.Horizontal.TProgressbar",
    mode="determinate"
)
progress.grid(row=2,column=0,columnspan=3,pady=20)

result=Label(
    panel,
    text="",
    bg="black",
    fg=GREEN,
    font=("Consolas",18,"bold")
)
result.grid(row=3,column=0,columnspan=3,pady=10)

details=Text(
    panel,
    width=45,
    height=8,
    bg="black",
    fg=GREEN,
    font=("Consolas",11)
)
details.grid(row=5,column=0,columnspan=3,pady=20)

for i in range(60):
    line=""
    for j in range(30):
        line+=random.choice("01 ")
    matrix.insert(END,line+"\n")

def check():

    status.config(
        text="SYSTEM STATUS : SCANNING",
        fg=YELLOW
    )

    progress["value"]=0
    details.delete("1.0",END)

    for i in range(101):
        progress["value"]=i
        root.update()
        time.sleep(0.01)

    pwd=password.get()
    length=len(pwd)

    if length<=5:
        strength="WEAK"
        color="red"

    elif length>=6 and length<=8:
        strength="MEDIUM"
        color="yellow"

    elif length>8 and length<=12:
        strength="STRONG"
        color="light green"

    else:
        strength="VERY STRONG"
        color="dark green"

    result.config(
        text=strength,
        fg=color
    )

    details.insert(
        END,
        "PASSWORD ANALYSIS REPORT\n"
    )

    details.insert(
        END,
        "===========================\n"
    )
    details.insert(
        END,
        f"\nPassword : {pwd}\n"
    )

    details.insert(
        END,
        f"Length   : {length}\n"
    )

    details.insert(
        END,
        f"Strength : {strength}\n"
    )

    status.config(
        text="SYSTEM STATUS : COMPLETE",
        fg=GREEN
    )

def clear():

    password.delete(0,END)

    result.config(text="")

    details.delete("1.0",END)

    progress["value"]=0

    status.config(
        text="SYSTEM STATUS : READY",
        fg=LIGHT
    )

def matrix_rain():

    line=""

    for i in range(30):

        if random.random()>0.5:
            line+=random.choice("01")

        else:
            line+=" "

    matrix.insert(END,line+"\n")

    matrix.see(END)

    if float(matrix.index("end-1c").split(".")[0])>60:
        matrix.delete("1.0","2.0")

    root.after(60,matrix_rain)

Button(
    panel,
    text="CHECK",
    command=check,
    bg=GREEN,
    fg="black",
    font=("Consolas",12,"bold"),
    width=12
).grid(row=4,column=0,pady=10)

Button(
    panel,
    text="CLEAR",
    command=clear,
    bg="#ffaa00",
    fg="black",
    font=("Consolas",12,"bold"),
    width=12
).grid(row=4,column=1,pady=10)

Button(
    panel,
    text="EXIT",
    command=root.destroy,
    bg=RED,
    fg="white",
    font=("Consolas",12,"bold"),
    width=12
).grid(row=4,column=2,pady=10)

Label(
    root,
    text="Python Tkinter Password Strength Checker",
    bg="black",
    fg=DARK,
    font=("Consolas",10)
).pack(pady = 5)

matrix_rain()

root.mainloop()