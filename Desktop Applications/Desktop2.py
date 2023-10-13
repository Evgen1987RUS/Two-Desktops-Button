from tkinter import *
from tkinter import ttk
import socket
import threading # threading required to prevent freezes
import random
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname()
PORT = 56432

def changeColor(): # background change
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = '#%02x%02x%02x' % (r, g, b)
    
    style.configure("TFrame", background=color)

def hostServer():
    hostBtn.config(state=DISABLED)

    S.bind((HOST, PORT)) # binds the socket with the address, requests tuple type
    print("Binded with: ", HOST, ". Awaiting connection..." ,sep="")
    clientMsg = "NONE"

    while True: # Continiously waiting for socket commands
        if (clientMsg == "0" or clientMsg == "NONE"):
            S.listen(1) # if client is yet to connect or socket was terminated accidentally
            conn, addr = S.accept()
            print("Connected with:", conn, addr)

        clientMsg = conn.recv(1024).decode()
        if (clientMsg == "ch"): # 'ch' for change
            print("Changing background color")
            changeColor()
        elif (clientMsg == "e"): # 'e' for exit
            print("Terminating program and server")
            root.after(10, root.destroy) # 10ms after this line to allow for breaking out of loop
            break
        
def newHostServerThread():
    hostServerThread = threading.Thread(target=hostServer)
    hostServerThread.daemon = True # daemon so it stops after main threaad is stopped
    hostServerThread.start()

root = Tk() # desktop app (window)
root.state('zoomed')
style = ttk.Style(root)
frame = ttk.Frame(root, width=1920, height=1080)
frame.grid()

# bgChangeBtn = ttk.Button(frame, text="Change color", command=changeColor)
# bgChangeBtn.place(relx=0.5, rely=0.4, anchor=CENTER)

hostBtn = ttk.Button(frame, text="Host server", command=newHostServerThread) # connects to host #lambda required to not get a return from func (https://docs.python.org/2/tutorial/controlflow.html#lambda-expressions)
hostBtn.place(relx=0.5, rely=0.5, anchor=CENTER)

exitBtn = ttk.Button(frame, text="Exit", command=root.destroy) # connects to host #lambda required to not get a return from func (https://docs.python.org/2/tutorial/controlflow.html#lambda-expressions)
exitBtn.place(relx=0.5, rely=0.53, anchor=CENTER)

root.mainloop()