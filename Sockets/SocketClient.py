import socket # TODO: make it so client opens a socket once and is connected until server is terminated
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TODO: this is supposed to be in an infinite loop (unless we exit the desktop app)
host = socket.gethostname()
port = 65432
msgToServer = 'Y' # TODO: this should change depending on what button is pressed

s.connect((host, port))
print("Connected with", host)

s.send(msgToServer.encode())
print("Sent the following message to ", host, ": ", msgToServer, sep="")

# s.close()
