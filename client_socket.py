from socket import socket, AF_INET, SOCK_STREAM

class ClientSocket():

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_address = (host, port)
        self.client_socket = socket(AF_INET, SOCK_STREAM)

    def start_client(self):
        self.client_socket.connect(self.server_address)
    
    def receive_payment_idication(self):
        return self.client_socket.recv(1024).decode()