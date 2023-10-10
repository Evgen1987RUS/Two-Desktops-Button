import sys
sys.path.append("..")
from tkinter import *
from tkinter import ttk
import random
from Sockets import SocketServer

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    color = '#%02x%02x%02x' % (r, g, b)
    
    root.config(bg=color)

root = Tk()
frame = ttk.Frame(root, padding=100).grid()

root.mainloop()