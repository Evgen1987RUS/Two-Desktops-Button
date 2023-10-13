from tkinter import *
from tkinter import ttk # such import needed to change Tk package to ttk package (newer widgets and nicer UI)
import socket
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates a new socket object

def sendMsg(msg): # sending message to 2nd desktop 
    if (msg == "ch"):
        print("Sent 'change' message. Changing background.")
        S.send(msg.encode())
    else:
        print("Sent 'exit' message. Terminating program and connection.")
        S.send(msg.encode())
        S.close()
        root.destroy()

def connectToHost(host, port): # connect after button press + change to new buttons
    S.connect((host, port))
    print("Connected with", host)
    hostEntry.destroy()
    portEntry.destroy()
    connectionBtn.destroy()

    ttk.Button(frame, text="Change background", command=lambda:[sendMsg("ch")]).place(relx=0.5, rely=0.5, anchor=CENTER)
    ttk.Button(frame, text="Exit", command=lambda:[sendMsg("e")]).place(relx=0.5, rely=0.53, anchor=CENTER)

def onHostEntryClick(event): # "ghost" text funcs
    if (hostEntry.get() == "Enter host name"):
        hostEntry.delete(0, "end")
        hostEntry.insert(0, "")
        hostEntry.config(foreground="black")

def onHostFocusOut(event):
    if (hostEntry.get() == ""):
        hostEntry.insert(0, "Enter host name")
        hostEntry.config(foreground="grey")

def onPortEntryClick(event):
    if (portEntry.get() == "Enter port value"):
        portEntry.delete(0, "end")
        portEntry.insert(0, "")
        portEntry.config(foreground="black")

def onPortFocusOut(event):
    if (portEntry.get() == ""):
        portEntry.insert(0, "Enter port value")
        portEntry.config(foreground='grey')
    
root = Tk() # desktop app (window)
root.state('zoomed')
frame = ttk.Frame(root, width=1920, height=1080).grid()

hostName = StringVar()
portVal = StringVar()

hostEntry = ttk.Entry(frame, text="Enter host name", textvariable=hostName) # requests name of the host and connects the client to the server
hostEntry.place(relx=0.5, rely=0.5, anchor=CENTER)
hostEntry.insert(0, "Enter host name")
hostEntry.config(foreground="grey")
hostEntry.bind('<FocusIn>', onHostEntryClick)
hostEntry.bind('<FocusOut>', onHostFocusOut)

portEntry = ttk.Entry(frame, text="Enter port value", textvariable=portVal) # requests port value
portEntry.place(relx=0.5, rely=0.53, anchor=CENTER)
portEntry.insert(0, "Enter port value")
portEntry.config(foreground="grey")
portEntry.bind('<FocusIn>', onPortEntryClick)
portEntry.bind('<FocusOut>', onPortFocusOut)

connectionBtn = ttk.Button(frame, text="Connect", command=lambda:[connectToHost(hostName.get(), int(portVal.get()))]) # connects to host #lambda required to not get a return from func (https://docs.python.org/2/tutorial/controlflow.html#lambda-expressions)
connectionBtn.place(relx=0.5, rely=0.56, anchor=CENTER)

#ttk.Label(frame, text="First WEB project task").grid(column=1, row=0)
#ttk.Button(frame, text="Change picture", command=S.SendMsg("ch")).grid(column=1, row=1) # this button sends a message from client to change the picture
#ttk.Button(frame, text="Exit", command=lambda:[SocketClient.client.SendMsg("e"), root.destroy]).grid(column=1, row=2) # lambda allows for multiple commands, sends a message to close second desktop
root.mainloop() # puts everything on display and responds to user's actions
