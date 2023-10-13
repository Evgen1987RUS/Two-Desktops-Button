from tkinter import *
from tkinter import ttk # such import needed to change Tk package to ttk package (newer widgets and nicer UI)
import socket
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates a new socket object

def connectToHost(host, port):
    S.connect((host, port))
    print("Connected with", host)

root = Tk() # desktop app (window)
frame = ttk.Frame(root, padding=100).grid() # TODO: width and height should depend on user's monitor aspects

hostName = StringVar()
portVal = IntVar()
ttk.Entry(frame, text="Enter host name", textvariable=hostName).grid(column=0, row=0) # requests name of the host and connects the client to the server
ttk.Entry(frame, text="Enter port value", textvariable=portVal).grid(column=0, row=1) # requests port value
ttk.Button(frame, text="Connect", command=lambda: connectToHost(hostName.get(), portVal.get())).grid(column=0, row=2) # connects to host #lambda required to construct a parameterless callable (https://docs.python.org/2/tutorial/controlflow.html#lambda-expressions)

#ttk.Label(frame, text="First WEB project task").grid(column=1, row=0) # TODO: make the button on center and this text on top + style
#ttk.Button(frame, text="Change picture", command=S.SendMsg("ch")).grid(column=1, row=1) # this button sends a message from client to change the picture
#ttk.Button(frame, text="Exit", command=lambda:[SocketClient.client.SendMsg("e"), root.destroy]).grid(column=1, row=2) # lambda allows for multiple commands, sends a message to close second desktop
root.mainloop() # puts everything on display and responds to user's actions
