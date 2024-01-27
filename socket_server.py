from socket import socket, AF_INET, SOCK_STREAM

class SocketServer():

    def __init__(self, host, port):
         self.host = host
         self.port = port
         self.server_socket = socket(AF_INET, SOCK_STREAM)
         self.client_sockets = {}
     
    def send_data_to_client_socket(self, client_socket, data):
        client_socket.sendall(data.encode())

    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        while True:
            client_socket, client_address = self.server_socket.accept()
            ip = client_address[0]
            self.client_sockets[ip] = client_socket
