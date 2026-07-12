from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time

root = Tk()
root.title("AURA INTEREST CALCULATOR")
root.geometry("1200x700")
root.configure(bg="black")
root.resizable(False, False)

GREEN = "#00FF41"
LIGHT = "#66FF66"
DARK = "#001500"
RED = "#FF3333"

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "green.Horizontal.TProgressbar",
    troughcolor="black",
    background=GREEN,
    bordercolor="black",
    lightcolor=GREEN,
    darkcolor=GREEN
)

title = Label(
    root,
    text="AURA FINANCIAL ENGINE v2.0",
    font=("Consolas",24,"bold"),
    bg="black",
    fg=GREEN
)
title.pack(pady=8)

status = Label(
    root,
    text="SYSTEM STATUS : READY",
    font=("Consolas",11),
    bg="black",
    fg=LIGHT
)
status.pack()

clock = Label(
    root,
    font=("Consolas",11),
    bg="black",
    fg=LIGHT
)
clock.place(x=1080,y=15)

def update_clock():
    clock.config(text=time.strftime("%H:%M:%S"))
    root.after(1000,update_clock)

update_clock()

main = Frame(root,bg="black")
main.pack(fill=BOTH,expand=True)

matrix = Text(
    main,
    width=30,
    bg="black",
    fg="#005500",
    bd=0,
    font=("Consolas",9)
)
matrix.pack(side=LEFT,fill=Y)

panel = Frame(
    main,
    bg="black",
    highlightbackground=GREEN,
    highlightthickness=2
)
panel.pack(side=LEFT,padx=20,pady=20,fill=BOTH,expand=True)

Label(
    panel,
    text="ENTER DETAILS",
    bg="black",
    fg=GREEN,
    font=("Consolas",16,"bold")
).grid(row=0,column=0,columnspan=2,pady=20)

Label(
    panel,
    text="Principal Amount",
    bg="black",
    fg=GREEN,
    font=("Consolas",12)
).grid(row=1,column=0,padx=20,pady=10,sticky=W)

principal = Entry(
    panel,
    width=25,
    bg="black",
    fg=GREEN,
    insertbackground=GREEN,
    font=("Consolas",12)
)
principal.grid(row=1,column=1)

Label(
    panel,
    text="Time (Years)",
    bg="black",
    fg=GREEN,
    font=("Consolas",12)
).grid(row=2,column=0,padx=20,pady=10,sticky=W)

years = Entry(
    panel,
    width=25,
    bg="black",
    fg=GREEN,
    insertbackground=GREEN,
    font=("Consolas",12)
)
years.grid(row=2,column=1)

Label(
    panel,
    text="Rate (%)",
    bg="black",
    fg=GREEN,
    font=("Consolas",12)
).grid(row=3,column=0,padx=20,pady=10,sticky=W)

rate = Entry(
    panel,
    width=25,
    bg="black",
    fg=GREEN,
    insertbackground=GREEN,
    font=("Consolas",12)
)
rate.grid(row=3,column=1)

progress = ttk.Progressbar(
    panel,
    length=500,
    style="green.Horizontal.TProgressbar",
    mode="determinate"
)
progress.grid(row=4,column=0,columnspan=2,pady=20)

result = Text(
    panel,
    width=60,
    height=10,
    bg="black",
    fg=GREEN,
    bd=1,
    insertbackground=GREEN,
    font=("Consolas",11)
)
result.grid(row=6,column=0,columnspan=2,pady=20)

for i in range(70):
    line=""
    for j in range(35):
        line+=random.choice("01 ")
    matrix.insert(END,line+"\n")

def calculate():
    try:

        status.config(
            text="SYSTEM STATUS : PROCESSING",
            fg="yellow"
        )

        result.delete("1.0",END)

        for i in range(101):
            progress["value"]=i
            root.update()
            time.sleep(0.01)

        p=float(principal.get())
        t=float(years.get())
        r=float(rate.get())

        si=(p*r*t)/100
        amount=p*(1+r/100)**t
        ci=amount-p

        status.config(
            text="SYSTEM STATUS : COMPLETED",
            fg=GREEN
        )

        result.insert(
            END,
            "============================================\n"
        )

        result.insert(
            END,
            "      AURA FINANCIAL REPORT\n"
        )

        result.insert(
            END,
            "============================================\n\n"
        )

        result.insert(
            END,
            f"Principal Amount   : ₹ {p:,.2f}\n"
        )

        result.insert(
            END,
            f"Time Period        : {t} Years\n"
        )

        result.insert(
            END,
            f"Rate of Interest   : {r}%\n\n"
        )

        result.insert(
            END,
            f"Simple Interest    : ₹ {si:,.2f}\n"
        )

        result.insert(
            END,
            f"Compound Interest  : ₹ {ci:,.2f}\n"
        )

        result.insert(
            END,
            f"Final Amount       : ₹ {amount:,.2f}\n\n"
        )

        result.insert(
            END,
            "SCAN STATUS : SUCCESS\n"
        )

    except:

        messagebox.showerror(
            "Error",
            "Please enter valid numeric values."
        )


def clear():

    principal.delete(0,END)
    years.delete(0,END)
    rate.delete(0,END)

    result.delete("1.0",END)

    progress["value"]=0

    status.config(
        text="SYSTEM STATUS : READY",
        fg=LIGHT
    )


def matrix_rain():

    line=""

    for i in range(35):

        if random.random()>0.5:
            line+=random.choice("01")
        else:
            line+=" "

    matrix.insert(END,line+"\n")
    matrix.see(END)

    if float(matrix.index("end-1c").split(".")[0])>70:
        matrix.delete("1.0","2.0")

    root.after(60,matrix_rain)


calc = Button(
    panel,
    text="CALCULATE",
    command=calculate,
    bg=GREEN,
    fg="black",
    activebackground=LIGHT,
    activeforeground="black",
    font=("Consolas",12,"bold"),
    width=15,
    relief=FLAT,
    cursor="hand2"
)

calc.grid(row=5,column=0,pady=10)


clear_btn = Button(
    panel,
    text="CLEAR",
    command=clear,
    bg="#ffaa00",
    fg="black",
    font=("Consolas",12,"bold"),
    width=15,
    relief=FLAT,
    cursor="hand2"
)

clear_btn.grid(row=5,column=1,pady=10)


def enter(e):
    e.widget["bg"]=LIGHT

def leave(e):
    if e.widget==calc:
        e.widget["bg"]=GREEN
    else:
        e.widget["bg"]="#ffaa00"


calc.bind("<Enter>",enter)
calc.bind("<Leave>",leave)

clear_btn.bind("<Enter>",enter)
clear_btn.bind("<Leave>",leave)


Button(
    root,
    text="EXIT",
    command=root.destroy,
    bg=RED,
    fg="white",
    font=("Consolas",12,"bold"),
    width=12,
    relief=FLAT,
    cursor="hand2"
).pack(pady=10)


footer=Label(
    root,
    text="AURA Financial Engine | Version 2.0 | Python Tkinter Project",
    bg="black",
    fg=DARK,
    font=("Consolas",10)
)

footer.pack(pady=5)

matrix_rain()

root.mainloop()