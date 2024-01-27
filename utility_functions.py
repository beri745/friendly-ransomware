import os

class UtilityFunctions:

    @staticmethod
    def read_file(file):
        with open(file, "rb") as f:
            return f.read()

    @staticmethod    
    def write_file(file, content):
        with open(file, "wb") as f:
            f.write(content)
    
    @staticmethod
    def find_files():
        files = []
        important_files = ["client_socket.py", "decrypt.py", "encrypt.py", "main_client.py", "utility_functions.py", "main_server.py", "socket_server.py", "web_server.py",
                           "Capture.JPG", "README.txt", "requirements.txt", "static"]
        for file in os.listdir():
            if file not in important_files and os.path.isfile(file):
                files.append(file)
        return files