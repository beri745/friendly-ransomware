from socket_server import SocketServer
import web_server
from threading import Thread


socket_server = SocketServer("127.0.0.1", 1337)
SocketServer.instance = socket_server
socket_thread = Thread(target = socket_server.start_server)
socket_thread.start()

web_server.start_server("127.0.0.1", 1338)