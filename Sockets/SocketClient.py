import socket # TODO: make it so client opens a socket once and is connected until server is terminated 
# TODO: this is supposed to be in an infinite loop (unless we exit the desktop app)
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # all are CONSTs
HOST = socket.gethostname()
PORT = 65432

class clientSide:
    def __init__(self):
        S.connect((HOST, PORT))
        print("Connected with", HOST)

    def SendMsg(msg): # message is taken from button to change the picture on another desktop
        if msg == "ch": # "ch" is for change
            S.send(msg.encode())
            print("Sent the following message to ", HOST, ": ", msg, sep="")
        else: # msg == "e", "e" is for exit
            S.send(msg.encode())
            S.close()     # sends the message to close the desktop and turns this desktop off
            print("Sent the following message to ", HOST, ": ", msg, sep="" "\n Process terminated")

client = clientSide()
