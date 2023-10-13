from tkinter import *
from tkinter import ttk # such import needed to change Tk package to ttk package (newer widgets and nicer UI)
from Sockets import SocketClient

root = Tk() # desktop app (window)
frame = ttk.Frame(root, padding=1000).grid() # TODO: width and height should depend on user's monitor aspects
ttk.Label(frame, text="First WEB project task").grid(column=1, row=0) # TODO: make the button on center and this text on top + style
ttk.Button(frame, text="Change picture", command=SocketClient.client.SendMsg("ch")).grid(column=1, row=1) # this button sends a message from client to change the picture
ttk.Button(frame, text="Exit", command=lambda:[SocketClient.client.SendMsg("e"), root.destroy]).grid(column=1, row=2) # lambda allows for multiple commands, sends a message to close second desktop
root.mainloop() # puts everything on display and responds to user's actions