import socket

class SecondClient:
    def __init__(self):
        HOST = "192.168.20.177"  # The server's hostname or IP address
        PORT = 2001 # The port used by the server
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))
    
    def getDI(self, num):
        self.sock.send('getDI'.encode("ascii"))
        data = self.sock.recv(1024)
        print(data)
        data = self.sock.recv(1024).decode('utf-8')
        
        return data[num-1]

    def __del__(self):
        self.sock.close()