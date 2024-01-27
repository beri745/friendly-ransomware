install dependencies: pip install requirements.txt

project: friendly ransomware
a malicious python script that encrypts all data files and decrypts them only upon paying

flow of the project:
main_server.py initializes both socket server and web server
clients runs main_client.py, the client connects by socket to a server socket
all the client's files in the same directory are being encrpyted with module fernet
an html page opens describing you what just happened and the offer, payment for decryption
once payment is achieved, a post method is being delievered with a message from the server to the client with a socket,
that the client indeed has paid, once that happens a decryption to all infected files is taking place

to start:
make sure main_server.py is running
and then run main_client.py

i have put 3 "important" txt files for testing ["INSTAGRAM_INFO.txt", "PC_INFO.txt", "PERSON_INFO.txt"]

the friendly ransomware should be affecting these files, you can more files as you like