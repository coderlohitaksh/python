from tkinter import *
from tkinter import ttk
import random
import time

root = Tk()
root.title("AURA CYBER TERMINAL")
root.geometry("1200x700")
root.configure(bg="black")
root.resizable(False, False)

GREEN = "#00ff41"
DARK = "#001500"

title = Label(
    root,
    text="AURA CYBER SECURITY ENGINE v5.0",
    font=("Consolas", 22, "bold"),
    fg=GREEN,
    bg="black"
)
title.pack(pady=5)

info = Label(
    root,
    text="STATUS : READY",
    font=("Consolas", 11),
    fg=GREEN,
    bg="black"
)
info.pack()

frame = Frame(root, bg="black")
frame.pack(fill=BOTH, expand=True)

matrix = Text(
    frame,
    width=30,
    bg="black",
    fg="#005500",
    bd=0,
    font=("Consolas", 9)
)
matrix.pack(side=LEFT, fill=Y)

terminal = Text(
    frame,
    bg="black",
    fg=GREEN,
    insertbackground=GREEN,
    bd=0,
    font=("Consolas", 11)
)
terminal.pack(side=LEFT, fill=BOTH, expand=True)

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

progress = ttk.Progressbar(
    root,
    length=900,
    style="green.Horizontal.TProgressbar",
    mode="determinate"
)
progress.pack(pady=5)

logs = [
    "Initializing kernel...",
    "Loading security modules...",
    "Checking BIOS...",
    "Verifying bootloader...",
    "Scanning RAM...",
    "Scanning Registry...",
    "Scanning System32...",
    "Scanning startup services...",
    "Checking firewall...",
    "Inspecting network sockets...",
    "Analyzing running processes...",
    "Searching rootkits...",
    "Searching trojans...",
    "Scanning browser extensions...",
    "Checking DNS cache...",
    "Checking encrypted payloads...",
    "Verifying signatures...",
    "Deep scan running...",
    "Checking USB devices...",
    "Final verification..."
]

cursor = True
running = False

def blink():
    global cursor
    if cursor:
        terminal.insert(END, "█")
    else:
        if terminal.index("end-1c") != "1.0":
            terminal.delete("end-2c", "end-1c")
    cursor = not cursor
    terminal.see(END)
    root.after(500, blink)

def rain():
    line = ""
    for i in range(35):
        if random.random() < 0.5:
            line += random.choice("01")
        else:
            line += " "
    matrix.insert(END, line + "\n")
    matrix.see(END)
    if float(matrix.index("end-1c").split(".")[0]) > 60:
        matrix.delete("1.0", "2.0")
    root.after(40, rain)

def type_text(text, delay=18):
    for ch in text:
        terminal.insert(END, ch)
        terminal.see(END)
        root.update()
        time.sleep(delay / 1000)

def scan(index=0):
    global running

    if index == 0:
        running = True
        terminal.delete("1.0", END)
        type_text("AURA SECURITY ENGINE ONLINE\n\n")
        info.config(text="STATUS : SCANNING", fg="yellow")
        progress["value"] = 0

    if index < len(logs):
        type_text("[+] " + logs[index] + "\n")
        progress["value"] = (index + 1) * 5

        ip = ".".join(str(random.randint(1, 255)) for _ in range(4))
        hexcode = "".join(random.choice("0123456789ABCDEF") for _ in range(8))

        type_text("    IP   : " + ip + "\n", 8)
        type_text("    HASH : 0x" + hexcode + "\n\n", 8)

        root.after(
            random.randint(250, 500),
            lambda: scan(index + 1)
        )

    else:
        progress["value"] = 100

        type_text("\n")
        type_text("[!] CRITICAL THREAT DETECTED\n", 20)
        type_text("[!] Trojan.Win32.Generic\n", 20)
        type_text("[!] Unauthorized Remote Access\n", 20)
        type_text("[!] Encryption Keys Compromised\n", 20)
        type_text("[!] Risk Level : CRITICAL\n\n", 20)

        info.config(
            text="STATUS : THREAT DETECTED",
            fg="red"
        )

        terminal.tag_add("alert", "end-8l", "end")
        terminal.tag_config(
            "alert",
            foreground="red"
        )

Button(
    root,
    text="START DEEP SCAN",
    command=scan,
    bg=GREEN,
    fg="black",
    activebackground="#66ff66",
    activeforeground="black",
    relief=FLAT,
    cursor="hand2",
    font=("Consolas", 13, "bold"),
    padx=20,
    pady=8
).pack(pady=10)

footer = Label(
    root,
    text="AURA Cyber Security Terminal | Build 5.0 | Secure Link Established",
    bg="black",
    fg=DARK,
    font=("Consolas", 9)
)
footer.pack(pady=5)

rain()
blink()

terminal.insert(
    END,
    "Welcome to AURA Cyber Security Engine\n"
)

terminal.insert(
    END,
    "Type: START DEEP SCAN\n\n"
)

root.mainloop()