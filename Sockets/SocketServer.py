import socket # TODO: server should run only when the desktop is booted up, on exit the server should be terminated

S = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET, SOCK_STREAM - constants, represent adress families and represent the socket types respectively
HOST = socket.gethostname()
PORT = 65432

class socketServer:        
    def __init__(self):
        S.bind((HOST, PORT)) # binds the socket with the address, requests tuple type
        print("Binded with", HOST, PORT)
        
        S.listen(1) # listens until a limit of connections has been reached # FIXME: maybe add another listening faction if a client is terminated, so the server can accept the next one
        self.con, self.addr = S.accept() # accept a connection
        print("Connected with", self.addr)

    def ActiveServer():
        while 1:
            data = server.con.recv(1024).decode() # recieves signal # FIXME: check whether less than 1024 can be supported
            if data == "e": # if an exit is signaled -> closes connection and server socket
                server.con.close() 
                S.close()
                print("Message from client:", data, "\n Connection and server were terminated")
                break
            elif data == "ch":
                # FIXME: send the signal to 2nd desktop
                print("Message from client:", data, "\n Changed the background on 2nd desktop")
        
server = socketServer()
