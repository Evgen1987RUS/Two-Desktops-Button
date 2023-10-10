from tkinter import *
import random

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    color = '#%02x%02x%02x' % (r, g, b)
    
    root.config(bg=color)
    
root = Tk()

button = Button(root, text="Change picture", command=change_color)
button.pack()

root.mainloop()
