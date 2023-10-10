from tkinter import *
from tkinter import ttk # such import needed to change Tk package to ttk package (newer widgets and nicer UI)

root = Tk() # desktop app (window)
frame = ttk.Frame(root, padding=100) # TODO: width and height should depend on user's monitor aspects
frame.grid()
ttk.Label(frame, text="First WEB project task").grid(column=1, row=0) # TODO: make the button on center and this text on top + style
ttk.Button(frame, text="Change picture").grid(column=1, row=1) # button init should contain command property which has to send a signal to change the picture
ttk.Button(frame, text="Exit", command=root.destroy).grid(column=1, row=2)
root.mainloop() # puts everything on display and responds to user's actions