
from tkinter import *
root = Tk()
root.title = ("Main window")
root.geometry = ('800x600')

def topwin() :
    top = Toplevel()
    top.title = ("Topmost windows")
    top.geometry = ('600x400')

    l2 = Label(top , Text == 'This the topmost window')
    l2.pack()

    top.mainloop()


l = Label(root, text= 'This is root window')
btn = Button(root, text= "Click here to make a new window" , command=topwin)


l.pack()
btn.pack()

root.mainloop()
