from tkinter import *

root = Tk()
root.title("Number Pad")
root.geometry("400x500")

nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ['#', 0, '*']
]

display = Entry(root, font=("Arial", 24), justify="center")
display.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)

def button_click(value):
    display.insert(END, str(value))

root.rowconfigure(0, weight=1)

for i in range(1, 5):
    root.rowconfigure(i, weight=1)

for j in range(3):
    root.columnconfigure(j, weight=1)

for i in range(4):
    for j in range(3):
        btn = Button(
            root,
            text=str(nums[i][j]),
            font=("Arial", 20),
            bg="#8CA1FF",
            command=lambda value=nums[i][j]: button_click(value)
        )
        btn.grid(row=i+1, column=j, sticky="nsew", padx=5, pady=5)

root.mainloop()