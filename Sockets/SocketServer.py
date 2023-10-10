import socket # TODO: server should run only when the desktop is booted up, on exit the server should be terminated

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET, SOCK_STREAM - constants, represent adress families and represent the socket types respectively
host = socket.gethostname()
port = 65432

s.bind((host, port)) # binds the socket with the address, requests tuple type
print("Binded with", host, port)
s.listen(1) # listens for number of connections
connection, address = s.accept() # accept a connection
print("Connected with", address)
while 1:
    data = connection.recv(1024) # socket recieves data from client. Only recieves a Y / N signal in this instance
    if data.decode() == 'N' or data.decode() == "":
        break
    print("Message from client:", data.decode())

#connection.close() # terminate client connection
#socket.close() # terminate server
# both are not needed in this instance as this will be the end of the socket in this project
