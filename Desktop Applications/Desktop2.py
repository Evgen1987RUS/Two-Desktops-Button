from tkinter import *
from tkinter import ttk
import random

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    color = '#%02x%02x%02x' % (r, g, b)
    
    root.config(bg=color)
    
root = Tk()
frame = ttk.Frame(root, padding=100)
frame.grid()

button = ttk.Button(frame, text="Change picture", command=change_color)
button.grid()

root.mainloop()
