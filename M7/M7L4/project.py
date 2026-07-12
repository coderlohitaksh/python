from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os
import time

root = Tk()
root.title("Codingal's Text Editor")
root.geometry("900x600")
root.configure(bg="#f5f5f5")

current_file = ""


def new_file():
    global current_file
    text_area.delete("1.0", END)
    current_file = ""
    root.title("Codingal's Text Editor - New File")
    update_status()


def open_file():
    global current_file

    file = filedialog.askopenfilename(
        title="Open File",
        filetypes=[
            ("Text Files", "*.txt"),
            ("Python Files", "*.py"),
            ("All Files", "*.*")
        ]
    )

    if not file:
        return

    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

    text_area.delete("1.0", END)
    text_area.insert("1.0", text)

    current_file = file
    root.title(f"Codingal's Text Editor - {os.path.basename(file)}")
    update_status()


def save_file():
    global current_file

    file = filedialog.asksaveasfilename(
        title="Save File",
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("Python Files", "*.py"),
            ("All Files", "*.*")
        ]
    )

    if not file:
        return

    with open(file, "w", encoding="utf-8") as f:
        f.write(text_area.get("1.0", END))

    current_file = file
    root.title(f"Codingal's Text Editor - {os.path.basename(file)}")
    messagebox.showinfo("Saved", "File saved successfully.")
    update_status()


def clear_text():
    text_area.delete("1.0", END)
    update_status()


def exit_editor():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        root.destroy()


def update_status(event=None):
    text = text_area.get("1.0", "end-1c")

    words = len(text.split())
    chars = len(text)

    status.config(
        text=f"Words : {words}    Characters : {chars}"
    )


def update_clock():
    clock.config(text=time.strftime("%I:%M:%S %p"))
    root.after(1000, update_clock)


header = Label(
    root,
    text="Codingal's Text Editor",
    font=("Consolas", 22, "bold"),
    bg="#1f2937",
    fg="white",
    pady=10
)
header.pack(fill=X)

toolbar = Frame(root, bg="#d9d9d9")
toolbar.pack(fill=X)

Button(
    toolbar,
    text="New",
    width=10,
    command=new_file
).pack(side=LEFT, padx=5, pady=5)

Button(
    toolbar,
    text="Open",
    width=10,
    command=open_file
).pack(side=LEFT, padx=5)

Button(
    toolbar,
    text="Save As",
    width=10,
    command=save_file
).pack(side=LEFT, padx=5)

Button(
    toolbar,
    text="Clear",
    width=10,
    command=clear_text
).pack(side=LEFT, padx=5)

Button(
    toolbar,
    text="Exit",
    width=10,
    command=exit_editor
).pack(side=LEFT, padx=5)

clock = Label(
    toolbar,
    font=("Arial", 11, "bold"),
    bg="#d9d9d9"
)
clock.pack(side=RIGHT, padx=15)

editor_frame = Frame(root)
editor_frame.pack(fill=BOTH, expand=True)

scroll = Scrollbar(editor_frame)

text_area = Text(
    editor_frame,
    font=("Consolas", 13),
    wrap=WORD,
    undo=True,
    yscrollcommand=scroll.set
)

scroll.config(command=text_area.yview)

scroll.pack(side=RIGHT, fill=Y)
text_area.pack(fill=BOTH, expand=True)

status = Label(
    root,
    text="Words : 0    Characters : 0",
    bd=1,
    relief=SUNKEN,
    anchor=W,
    font=("Arial", 10)
)
status.pack(fill=X)

text_area.bind("<KeyRelease>", update_status)

root.bind("<Control-n>", lambda e: new_file())
root.bind("<Control-o>", lambda e: open_file())
root.bind("<Control-s>", lambda e: save_file())

update_clock()

root.mainloop()