# Pâyidar

from tkinter import *
from tkinter import ttk
import tkinter

root = Tk()

payidar = StringVar()
label = Message(root, textvariable=payidar, relief=RAISED)

payidar.set("Pâyidar Code Tarafından Kodlanmıştır.")
label.pack()
root.mainloop()